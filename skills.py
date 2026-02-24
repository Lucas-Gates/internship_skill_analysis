import re

CATEGORY_RULES = [
    #languages
    ("Language", re.compile(r"^(Python|R|Java|C\+\+|C#|Javascript|TypeScript|Scala|Go|Rust|Php)$", re.I)),
    #databases / query
    ("Database", re.compile(r"^(SQL|PostgreSQL|MySQL|SQLite|Oracle|Snowflake|Redshift|BigQuery|MongoDB|NoSQL)$", re.I)),
    #cloud / platforms
    ("Cloud", re.compile(r"^(AWS|Azure|GCP|Databricks)$", re.I)),
    #visualization / bi
    ("Visualization", re.compile(r"^(Tableau|Power BI|Excel|Looker|Qlik|Matplotlib|Seaborn)$", re.I)),
    #ml/ai
    ("ML/AI", re.compile(r"^(Machine Learning|Deep Learning|Artificial Intelligence|NLP|Computer Vision|PyTorch|TensorFlow|scikit-learn)$", re.I)),
    #data engineering / pipelines
    ("Data Engineering", re.compile(r"^(ETL|Data Engineering|Data Pipeline|Airflow|Spark|Kafka|Hadoop|dbt)$", re.I)),
    #stats / math
    ("Stats/Math", re.compile(r"^(Statistics|Mathematics|Probability|Regression|A/B Testing|Experimentation)$", re.I)),
    #soft skills
    ("Soft Skill", re.compile(r"^(Communication|Teamwork|Problem Solving|Project Management|Attention To Detail|Analytical Skills|Leadership|Time Management)$", re.I)),
]

def categorize_skill(skill):
    if not isinstance(skill, str) or not skill.strip():
        return "Other"
    s = skill.strip()
    for category, pattern in CATEGORY_RULES:
        if pattern.search(s):
            return category
    return "Other"