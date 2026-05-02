# NLP Processing Module for Skill Gap Analyzer

def preprocess_text(text):
    """
    Clean and normalize input text.
    Used for both user skills and job required skills.
    """
    if not text:
        return ""

    # convert to lowercase
    text = text.lower()

    # remove extra spaces
    text = text.strip()

    return text


def extract_skills(skill_text):
    """
    Convert comma-separated skills into a clean list.
    Example input: "Python, Machine Learning, SQL"
    Output: ['python', 'machine learning', 'sql']
    """
    if not skill_text:
        return []

    # normalize text
    skill_text = preprocess_text(skill_text)

    # split by comma
    skills = skill_text.split(',')

    # remove extra spaces
    skills = [skill.strip() for skill in skills if skill.strip() != ""]

    return skills


def skills_to_string(skills_list):
    """
    Convert skill list back to string for TF-IDF processing.
    """
    return " ".join(skills_list)