import re

import re

CATEGORY_RULES = [

    # Programming Languages
    ("Language", re.compile(r"\b(python|r|java|c\+\+|c#|javascript|typescript|scala|go|rust|php)\b", re.I)),

    # Databases / SQL
    ("Database", re.compile(r"\b(sql|postgres|mysql|sqlite|oracle|snowflake|redshift|bigquery|mongodb|nosql|sql server)\b", re.I)),

    # Cloud / Infrastructure
    ("Cloud", re.compile(r"\b(aws|azure|gcp|cloud computing|databricks)\b", re.I)),

    # Visualization / BI
    ("Visualization", re.compile(r"\b(tableau|power bi|excel|looker|qlik|powerpoint|reporting|business intelligence)\b", re.I)),

    # ML / AI
    ("ML/AI", re.compile(r"\b(machine learning|deep learning|artificial intelligence|nlp|computer vision|pytorch|tensorflow|scikit|data mining)\b", re.I)),

    # Data Engineering
    ("Data Engineering", re.compile(r"\b(etl|data pipeline|pipelines|airflow|spark|kafka|hadoop|dbt|data warehousing|data integration|data transformation)\b", re.I)),

    # Statistics / Math
    ("Stats/Math", re.compile(r"\b(statistics|statistical analysis|mathematics|probability|regression|experimentation|a/b testing)\b", re.I)),

    # Soft Skills
    ("Soft Skill", re.compile(r"\b(communication|teamwork|problem solving|analytical skills|attention to detail|leadership|time management|interpersonal skills|collaboration|critical thinking|presentation skills|written communication|verbal communication|adaptability|multitasking|organizational skills)\b", re.I)),
]

def categorize_skill(skill):
    if not isinstance(skill, str) or not skill.strip():
        return "Other"
    s = skill.strip()
    for category, pattern in CATEGORY_RULES:
        if pattern.search(s):
            return category
    return "Other"