from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Mapping job roles to PDF files
ROADMAP_FILES = {
    "software engineer": "software_engineer.pdf",
    "data scientist": "data_scientist.pdf",
    "web developer": "web_developer.pdf"
}

@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    selected_job = None
    pdf_file = None

    if request.method == 'POST':
        selected_job = request.form['job_role'].lower()

        if selected_job in ROADMAP_FILES:
            pdf_file = ROADMAP_FILES[selected_job]

    return render_template('roadmap.html', pdf_file=pdf_file, job=selected_job)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/roadmaps', filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)