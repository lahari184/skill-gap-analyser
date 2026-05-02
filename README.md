# Setup Instructions for Skill Gap Analyzer

Follow these steps to set up the project on your machine:

## Prerequisites
- Python 3.7 or higher
- MySQL Server installed and running
- Git

## Step 1: Clone/Download the Project
```bash
git clone [repository-url]
cd backend
```

## Step 2: Create Virtual Environment
```bash
python -m venv .venv
```

### Activate Virtual Environment:
- **Windows (PowerShell):**
  ```bash
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```bash
  .venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source .venv/bin/activate
  ```

## Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 4: Set Up Dataset

### Option A: Using the setup script
If available, run:
```bash
python setup_db.py
```

### Option B: Manual Setup
1. Open MySQL command line or MySQL Workbench:
   ```bash
   mysql -u root -p
   ```

2. Create the dataset:
   ```sql
   CREATE DATABASE skill_gap_analyzer;
   ```

3. Run the schema file:
   ```bash
   mysql -u root -p skill_gap_analyzer < schema.sql
   ```

## Step 5: Create .env File

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   or on Windows:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` and add your dataset credentials:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_NAME=skill_gap_analyzer
   DB_PORT=3306
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   ```

## Step 6: Run the Application
```bash
python app.py
```

The application will be available at: `http://localhost:5000`

## Troubleshooting

### "Dataset connection failed"
- Check if MySQL is running
- Verify credentials in `.env` file match your MySQL setup
- Ensure dataset `skill_gap_analyzer` exists

### "Module not found" error
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Port already in use
- Change the port in `app.py` or close the application using port 5000

## Project Structure
```
backend/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings (reads from .env)
├── db_connection.py      # Dataset connection function
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── schema.sql           # Dataset schema (for new setups)
├── templates/           # HTML templates
├── static/              # CSS, images, PDFs
└── README.md            # This file
```

## Dataset Credentials Management

**IMPORTANT:** Never commit `.env` file to Git!
- The `.env` file is already in `.gitignore`
- Share `.env.example` with your team
- Each developer creates their own `.env` with their credentials

---

For more information, contact the project maintainer.
