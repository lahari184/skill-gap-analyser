from flask import Flask, render_template, request, redirect, session, jsonify, send_file
import sqlite3
from functools import wraps
from contextlib import contextmanager
import os

# Configuration
from config import Config

# AI Modules
from nlp_processor import extract_skills, skills_to_string
from skill_matcher import calculate_similarity, find_missing_skills

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.debug = Config.DEBUG

# SQLite Database Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'sga.db')
SQLITE_TIMEOUT = 30

@contextmanager
def db_connection():
    conn = get_db_connection()
    try:
        yield conn
    finally:
        if conn:
            conn.close()


def init_db():
    """Initialize SQLite database with required tables"""
    conn = sqlite3.connect(DB_FILE, timeout=SQLITE_TIMEOUT, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            skills TEXT,
            desired_job TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create jobs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_role TEXT UNIQUE NOT NULL,
            required_skills TEXT NOT NULL,
            description TEXT
        )
    """)
    
    # Create resources table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT NOT NULL,
            resource_title TEXT NOT NULL,
            resource_link TEXT NOT NULL
        )
    """)
    
    # Create questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT NOT NULL,
            question_type TEXT NOT NULL, -- 'mcq' or 'code'
            question_text TEXT NOT NULL,
            options TEXT, -- JSON string for MCQ options
            correct_answer TEXT NOT NULL,
            explanation TEXT,
            difficulty TEXT DEFAULT 'beginner' -- beginner, intermediate, advanced
        )
    """)
    
    # Create user_test_results table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            skill_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    
    conn.commit()
    conn.close()


def seed_jobs():
    """Seed the jobs table with default roles if it is empty."""
    conn = sqlite3.connect(DB_FILE, timeout=SQLITE_TIMEOUT, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM jobs")
    count = cursor.fetchone()[0]
    if count == 0:
        jobs = [
            ('frontend developer', 'HTML, CSS, JavaScript, React', 'Build user interfaces and client-side applications.'),
            ('backend developer', 'Python, SQL, APIs, Flask', 'Develop server-side application logic and databases.'),
            ('full stack developer', 'HTML, CSS, JavaScript, Python, SQL', 'Work on both frontend and backend parts of web applications.'),
            ('data scientist', 'Python, Pandas, Machine Learning, SQL', 'Analyze data and build predictive models.'),
            ('data analyst', 'SQL, Excel, Python, Data Visualization', 'Interpret data and create reports to support decisions.'),
            ('devops engineer', 'Linux, Docker, AWS, CI/CD', 'Manage deployment pipelines and infrastructure.'),
            ('software engineer', 'Python, Algorithms, Data Structures, Git', 'Design and build software applications.'),
            ('web developer', 'HTML, CSS, JavaScript, Web APIs', 'Create responsive websites and web applications.'),
            ('mobile developer', 'React Native, Flutter, Kotlin, Swift', 'Build mobile applications for iOS and Android.'),
            ('cloud engineer', 'AWS, Docker, Kubernetes, Linux', 'Design and manage cloud infrastructure.'),
        ]

        for job_role, required_skills, description in jobs:
            cursor.execute(
                "INSERT INTO jobs (job_role, required_skills, description) VALUES (?, ?, ?)",
                (job_role, required_skills, description)
            )

        conn.commit()
    cursor.close()
    conn.close()


def seed_resources():
    """Seed the resources table with default learning materials and add any missing defaults."""
    conn = sqlite3.connect(DB_FILE, timeout=SQLITE_TIMEOUT, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    resources = [
        ('Python', 'Python Official Documentation', 'https://docs.python.org'),
        ('Python', 'Python Tutorials - W3Schools', 'https://www.w3schools.com/python'),
        ('SQL', 'SQL Tutorial - W3Schools', 'https://www.w3schools.com/sql'),
        ('SQL', 'Mode SQL Tutorial', 'https://mode.com/sql-tutorial/'),
        ('HTML', 'Mozilla Developer Network HTML Guide', 'https://developer.mozilla.org/en-US/docs/Web/HTML'),
        ('CSS', 'Mozilla Developer Network CSS Guide', 'https://developer.mozilla.org/en-US/docs/Web/CSS'),
        ('JavaScript', 'JavaScript MDN Docs', 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'),
        ('React', 'React Official Documentation', 'https://react.dev/'),
        ('Flask', 'Flask Quickstart', 'https://flask.palletsprojects.com/en/latest/quickstart/'),
        ('Pandas', 'Pandas Documentation', 'https://pandas.pydata.org/docs/'),
        ('Machine Learning', 'Scikit-Learn Tutorials', 'https://scikit-learn.org/stable/tutorial/index.html'),
        ('Data Visualization', 'Data Visualization with Python', 'https://realpython.com/python-data-visualization/'),
        ('Docker', 'Docker Get Started', 'https://www.docker.com/get-started'),
        ('AWS', 'AWS Training and Certification', 'https://aws.amazon.com/training/'),
        ('Linux', 'Linux Journey', 'https://linuxjourney.com/'),
        ('CI/CD', 'GitHub Actions Documentation', 'https://docs.github.com/en/actions'),
        ('Algorithms', 'GeeksforGeeks Algorithms', 'https://www.geeksforgeeks.org/fundamentals-of-algorithms/'),
        ('Data Structures', 'GeeksforGeeks Data Structures', 'https://www.geeksforgeeks.org/data-structures/'),
        ('Git', 'Git Documentation', 'https://git-scm.com/doc'),
        ('Web APIs', 'MDN Web APIs', 'https://developer.mozilla.org/en-US/docs/Web/API'),
        ('RESTful API', 'Introduction to REST APIs', 'https://restfulapi.net/'),
        ('Java', 'Java Tutorials - Oracle', 'https://docs.oracle.com/javase/tutorial/'),
        ('React Native', 'React Native Docs', 'https://reactnative.dev/docs/getting-started'),
        ('Flutter', 'Flutter Documentation', 'https://flutter.dev/docs'),
        ('Kotlin', 'Kotlin Lang', 'https://kotlinlang.org/docs/home.html'),
        ('Swift', 'Swift.org Documentation', 'https://swift.org/documentation/'),
        ('Kubernetes', 'Kubernetes Basics', 'https://kubernetes.io/docs/tutorials/kubernetes-basics/'),
    ]

    for skill_name, resource_title, resource_link in resources:
        cursor.execute(
            "SELECT 1 FROM resources WHERE LOWER(skill_name)=LOWER(?) AND LOWER(resource_title)=LOWER(?) LIMIT 1",
            (skill_name, resource_title)
        )
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO resources (skill_name, resource_title, resource_link) VALUES (?, ?, ?)",
                (skill_name, resource_title, resource_link)
            )

    conn.commit()
    cursor.close()
    conn.close()

# Initialize database on startup
init_db()
seed_jobs()
seed_resources()

# Roadmap mapping
ROADMAP_FILES = {
    "frontend developer": "frontend-roadmap-v2.pdf",
    "frontend": "frontend-roadmap-v2.pdf",
    "backend developer": "backend-roadmap-v2.pdf",
    "backend": "backend-roadmap-v2.pdf",
    "software developer": "backend-roadmap-v2.pdf",
    "data scientist": "data-science-roadmap.pdf",
    "data science": "data-science-roadmap.pdf",
    "data analyst": "data-analyst-roadmap.pdf",
    "devops engineer": "devops-roadmap.pdf",
    "devops": "devops-roadmap.pdf",
    "software engineer": "softwareengineer2.pdf",
    "web developer": "web-roadmap.pdf",
    "web development": "web-roadmap.pdf",
    "full stack": "full-stack.pdf",
    "full-stack": "full-stack.pdf",
    "mobile developer": "mobile-roadmap-v2.pdf",
    "mobile development": "mobile-roadmap-v2.pdf",
    "machine learning": "machine-learning-roadmap-v2.pdf",
    "ai engineer": "ai-engineer.pdf",
    "ux designer": "ux-design.pdf",
    "ux design": "ux-design.pdf",
    "postgresql dba": "postgresql-dba.pdf",
    "cloud computing": "Develop a cloud computing roadmap..pdf"
}

# ================= DATABASE CONNECTION =================

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_FILE, timeout=SQLITE_TIMEOUT, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    except sqlite3.Error as e:
        app.logger.error(f"Database connection failed: {e}")
        return None


# ================= LOGIN REQUIRED =================

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# ================= HOME =================

@app.route("/")
def home():
    return render_template("index.html")

# ================= REGISTER =================

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip()
        password = (request.form.get("password") or "").strip()

        if not name or not email or not password:
            return "Please fill all required fields", 400

        try:
            with db_connection() as conn:
                if conn is None:
                    return "Database connection failed"
                
                cursor = conn.cursor()
                query = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)"
                cursor.execute(query, (name, email, password))
                
                # Get the last inserted ID
                user_id = cursor.lastrowid
                
                conn.commit()
                cursor.close()

            # Auto-login new user and redirect to onboarding for profile completion
            session["user_id"] = user_id
            session["user_name"] = name
            session["user_email"] = email

            return redirect("/onboarding")
        
        except sqlite3.IntegrityError:
            return "Email already exists", 400
        except sqlite3.Error as e:
            return f"Registration error: {e}"

    return render_template("register.html")

# ================= LOGIN =================

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = (request.form.get("email") or "").strip()
        password = (request.form.get("password") or "").strip()

        if not email or not password:
            return "Please provide email and password", 400

        try:
            with db_connection() as conn:
                if conn is None:
                    return "Database connection failed"
                    
                cursor = conn.cursor()

                query = "SELECT * FROM users WHERE email=? AND password=?"
                cursor.execute(query, (email, password))

                user = cursor.fetchone()

                cursor.close()

            if user:
                session["user_id"] = user[0]
                session["user_name"] = user[1]
                session["user_email"] = user[2]

                return redirect("/dashboard")
            else:
                return "Invalid Login"
        
        except sqlite3.Error as e:
            return f"Login error: {e}"

    return render_template("login.html")

# ================= ONBOARDING =================

@app.route("/onboarding")
@login_required
def onboarding():
    return render_template("onboarding.html", user_name=session["user_name"])

@app.route("/save-onboarding", methods=["POST"])
@login_required
def save_onboarding():
    skills = request.form.get("skills")
    desired_job = request.form.get("desired_job")

    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
            
            cursor = conn.cursor()
            query = "UPDATE users SET skills=?, desired_job=? WHERE id=?"
            cursor.execute(query, (skills, desired_job, session["user_id"]))
            
            conn.commit()
            cursor.close()
        
        return redirect("/dashboard")
    
    except sqlite3.Error as e:
        return f"Error saving profile: {e}"

# ================= DASHBOARD =================

@app.route("/dashboard")
@login_required
def dashboard():

    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
            
            cursor = conn.cursor()

            cursor.execute("SELECT job_role FROM jobs")
            jobs = cursor.fetchall()

            cursor.execute("SELECT skills, desired_job FROM users WHERE id=?", (session["user_id"],))
            user_data = cursor.fetchone()
            
            user_skills = user_data[0] if user_data else ""
            user_desired_job = user_data[1] if user_data else ""

            analysis_started = session.pop("analysis_started", False)

            cursor.close()

        return render_template("dashboard.html",
                               jobs=jobs,
                               user_name=session["user_name"],
                               user_skills=user_skills,
                               user_desired_job=user_desired_job,
                               analysis_started=analysis_started)
    
    except sqlite3.Error as e:
        return f"Error loading dashboard: {e}"

# ================= PROFILE =================

@app.route("/profile", methods=["GET","POST"])
@login_required
def profile():

    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
            
            cursor = conn.cursor()

            if request.method == "POST":

                skills = request.form.get("skills")
                desired_job = request.form.get("desired_job")

                query = "UPDATE users SET skills=?, desired_job=? WHERE id=?"
                cursor.execute(query, (skills, desired_job, session["user_id"]))

                conn.commit()
                cursor.close()

                return redirect("/dashboard")

            cursor.execute("SELECT skills, desired_job FROM users WHERE id=?",
                           (session["user_id"],))

            data = cursor.fetchone()

            cursor.close()

        return render_template("profile.html",
                               skills=data[0] if data else "",
                               desired_job=data[1] if data else "")
    
    except sqlite3.Error as e:                                                
        return f"Error loading profile: {e}"

# ================= SKILL GAP ANALYSIS =================

@app.route("/analyze", methods=["POST"])
@login_required
def analyze():

    job_role = (request.form.get("job_role") or "").strip()
    user_input = (request.form.get("skills") or "").strip()

    if not job_role:
        return "Job role is required", 400

    if not user_input:
        return "Please enter your skills", 400

    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
            
            cursor = conn.cursor()

            cursor.execute("SELECT required_skills FROM jobs WHERE job_role=?", (job_role,))
            job_row = cursor.fetchone()

            cursor.close()

        if not job_row:
            return "Job not found"

        job_required = job_row[0]

        # ===== NLP Skill Extraction =====

        user_list = extract_skills(user_input)
        job_list = extract_skills(job_required)

        user_text = skills_to_string(user_list)
        job_text = skills_to_string(job_list)

        # ===== TF-IDF Similarity =====

        similarity_score = calculate_similarity(user_text, job_text)

        # ===== Missing Skills =====

        matched, missing = find_missing_skills(user_list, job_list)

        # Store results in session
        session["analysis_job"] = job_role
        session["analysis_similarity"] = round(similarity_score*100, 2)
        session["analysis_matched"] = matched
        session["analysis_missing"] = missing

        # Flag dashboard that a skill analysis happened
        session["analysis_started"] = True

        return redirect("/results")
    
    except sqlite3.Error as e:
        return f"Error analyzing: {e}"

# ================= RESULTS PAGE =================

@app.route("/results")
@login_required
def results():
    # Get analysis results from session
    analysis_job = session.pop("analysis_job", None)
    analysis_similarity = session.pop("analysis_similarity", None)
    analysis_matched = session.pop("analysis_matched", None)
    analysis_missing = session.pop("analysis_missing", None)

    return render_template("result.html",
                           job=analysis_job,
                           similarity=analysis_similarity,
                           matched_skills=analysis_matched if analysis_matched else [],
                           missing_skills=analysis_missing if analysis_missing else [])

# ================= ROADMAP DOWNLOAD =================

def resolve_roadmap_file(job_role):
    """Return roadmap file for the given role (flexible matching)."""
    if not job_role:
        return None

    key = job_role.strip().lower()

    if key in ROADMAP_FILES:
        return ROADMAP_FILES[key]

    # Fallback matching (partial/close matches)
    for existing, filepath in ROADMAP_FILES.items():
        if existing in key or key in existing:
            return filepath

    # Split-based fallback (e.g., 'backend engineer' -> 'backend')
    tokens = [t for t in key.split() if t]
    for token in tokens:
        if token in ROADMAP_FILES:
            return ROADMAP_FILES[token]

    return None


@app.route("/roadmap", methods=["GET", "POST"])
def roadmap_selection():
    selected_job = None
    roadmap_file = None
    error = None

    if request.method == "POST":
        selected_job = request.form.get("job_role", "").strip()
        roadmap_file = resolve_roadmap_file(selected_job)
        if not roadmap_file:
            error = "Roadmap not found for selected role."

    return render_template(
        "roadmap.html",
        job=selected_job,
        pdf_file=roadmap_file,
        error=error
    )


@app.route("/roadmap/<job_role>")
def roadmap(job_role):
    roadmap_file = resolve_roadmap_file(job_role)
    if roadmap_file:
        return render_template("display_roadmap.html", job_role=job_role, roadmap_file=roadmap_file)
    return "Roadmap not found", 404

@app.route("/download_roadmap/<job_role>")
def download_roadmap(job_role):
    roadmap_file = resolve_roadmap_file(job_role)
    if roadmap_file:
        filepath = os.path.join("static", "roadmaps", roadmap_file)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        return "Roadmap file missing", 404
    return "Roadmap not found", 404

# ================= RESOURCES PAGE & API =================

@app.route('/resources', methods=['GET', 'POST'])
@login_required
def resources_page():
    resources = None
    searched_job = None
    
    if request.method == 'POST':
        job_role = request.form.get('job', '').strip()
        searched_job = job_role
        
        if not job_role:
            return render_template('resource.html', resources={}, searched_job=searched_job)
        
        try:
            with db_connection() as conn:
                if conn is None:
                    return "Database connection failed"
                    
                cursor = conn.cursor()
                
                # Get required skills for the job
                query = "SELECT required_skills FROM jobs WHERE LOWER(job_role)=LOWER(?)"
                cursor.execute(query, (job_role,))
                job_row = cursor.fetchone()
                
                if not job_row or not job_row[0]:
                    cursor.close()
                    return render_template('resource.html', resources={}, searched_job=searched_job, no_job=True)
                
                # Extract skills from required_skills
                required_skills = job_row[0]
                skills_list = [skill.strip() for skill in required_skills.split(',')]


             
                
                # Fetch resources for each skill
                resources = {}
                for skill in skills_list:
                    query = "SELECT resource_title, resource_link FROM resources WHERE LOWER(skill_name) LIKE LOWER(?)"
                    cursor.execute(query, (f"%{skill}%",))
                    skill_resources = cursor.fetchall()
                    if skill_resources:
                        resources[skill] = [{'resource_title': res[0], 'resource_link': res[1]} for res in skill_resources]
                
                cursor.close()
        
        except sqlite3.Error as e:
            return f"Error fetching resources: {e}"
    
    return render_template('resource.html', resources=resources, searched_job=searched_job)

@app.route('/api/resources', methods=['POST'])
def get_resources():
    try:
        data = request.json
        skills = data.get('skills', [])

        with db_connection() as conn:
            if conn is None:
                return jsonify({"error": "Database connection failed"}), 500
            
            cursor = conn.cursor()

            resources = []

            for skill in skills:
                skill_search = f"%{skill.strip()}%"
                query = "SELECT resource_title, resource_link FROM resources WHERE LOWER(skill_name) LIKE LOWER(?)"
                cursor.execute(query, (skill_search,))
                result = cursor.fetchall()
                for r in result:
                    resources.append({"resource_title": r[0], "resource_link": r[1]})

            cursor.close()

        return jsonify(resources)
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500

# ================= TESTS =================

@app.route('/tests')
@login_required
def tests():
    """Display available skill tests"""
    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
                
            cursor = conn.cursor()
            
            # Get all unique skills that have questions
            cursor.execute("SELECT DISTINCT skill_name FROM questions ORDER BY skill_name")
            skills = [row[0] for row in cursor.fetchall()]
            
            # Get user's previous test results
            cursor.execute("""
                SELECT skill_name, score, total_questions, completed_at 
                FROM user_test_results 
                WHERE user_id = ? 
                ORDER BY completed_at DESC
            """, (session["user_id"],))
            results = cursor.fetchall()
            
            cursor.close()
        
        return render_template('tests.html', skills=skills, results=results)
    
    except sqlite3.Error as e:
        return f"Error loading tests: {e}"

@app.route('/test/<skill_name>')
@login_required
def take_test(skill_name):
    """Display test questions for a specific skill"""
    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
            
            cursor = conn.cursor()
        
        # Get questions for this skill
        cursor.execute("""
            SELECT id, question_type, question_text, options, difficulty 
            FROM questions 
            WHERE skill_name = ? 
            ORDER BY difficulty, id
        """, (skill_name,))
        
        questions = []
        for row in cursor.fetchall():
            question = {
                'id': row[0],
                'type': row[1],
                'text': row[2],
                'difficulty': row[4]
            }
            
            if row[1] == 'mcq' and row[3]:
                import json
                try:
                    question['options'] = json.loads(row[3])
                except:
                    question['options'] = []
            else:
                question['options'] = []
                
            questions.append(question)
        
        cursor.close()
        
        if not questions:
            return f"No questions available for {skill_name}", 404
        
        return render_template('take_test.html', 
                             skill_name=skill_name, 
                             questions=questions)
    
    except sqlite3.Error as e:
        return f"Error loading test: {e}"

@app.route('/submit_test/<skill_name>', methods=['POST'])
@login_required
def submit_test(skill_name):
    """Process test submission and calculate score"""
    try:
        with db_connection() as conn:
            if conn is None:
                return "Database connection failed"
                
            cursor = conn.cursor()
        
        # Get all questions for this skill
        cursor.execute("""
            SELECT id, question_type, correct_answer 
            FROM questions 
            WHERE skill_name = ?
        """, (skill_name,))
        
        questions = {str(row[0]): {'type': row[1], 'answer': row[2]} for row in cursor.fetchall()}
        
        score = 0
        total_questions = len(questions)
        
        # Check answers
        for q_id, question_data in questions.items():
            user_answer = request.form.get(f'question_{q_id}', '').strip()
            
            if question_data['type'] == 'mcq':
                # For MCQ, compare directly
                if user_answer.lower() == question_data['answer'].lower():
                    score += 1
            elif question_data['type'] == 'code':
                # For code questions, we could add more sophisticated checking
                # For now, just check if they provided an answer
                if user_answer:
                    score += 1
        
        # Save result
        cursor.execute("""
            INSERT INTO user_test_results (user_id, skill_name, score, total_questions)
            VALUES (?, ?, ?, ?)
        """, (session["user_id"], skill_name, score, total_questions))
        
        conn.commit()
        cursor.close()
        
        # Store result in session for display
        session['test_result'] = {
            'skill_name': skill_name,
            'score': score,
            'total': total_questions,
            'percentage': round((score / total_questions) * 100, 1) if total_questions > 0 else 0
        }
        
        return redirect('/test_result')
    
    except sqlite3.Error as e:
        return f"Error submitting test: {e}"

@app.route('/test_result')
@login_required
def test_result():
    """Display test result"""
    result = session.pop('test_result', None)
    if not result:
        return redirect('/tests')
    
    return render_template('test_result.html', **result)

# ================= LOGOUT =================

@app.route("/logout")
def logout():
    user_id = session.get("user_id")
    if user_id:
        try:
            with db_connection() as conn:
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
                    conn.commit()
                    cursor.close()
        except sqlite3.Error as e:
            app.logger.error(f"Error deleting user: {e}")
    
    session.clear()
    return redirect("/")

# ================= RUN APP =================

if __name__ == "__main__":
    app.run(debug=True)