# TF-IDF Skill Matching Module
# Used to compare user skills with job required skills

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(user_skill_text, job_skill_text):
    """
    Compare user skills and job required skills using TF-IDF + Cosine Similarity

    Parameters:
        user_skill_text (str): cleaned user skills
        job_skill_text (str): cleaned job required skills from dataset

    Returns:
        float: similarity score between 0 and 1
    """

    if not user_skill_text or not job_skill_text:
        return 0.0

    texts = [user_skill_text, job_skill_text]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(vectors[0], vectors[1])

    return float(similarity[0][0])


def find_missing_skills(user_skills_list, job_skills_list):
    """
    Identify skills required for job but not present in user skills
    """

    user_set = set(user_skills_list)
    job_set = set(job_skills_list)

    missing = list(job_set - user_set)
    matched = list(user_set.intersection(job_set))

    return matched, missing