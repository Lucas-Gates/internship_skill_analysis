import os
import pandas as pd
import re
from skill_sorting import categorize_skill

ALIASES = {
    # SQL
    "Sql": "SQL",
    "Sql ": "SQL",
    "Sql Server": "SQL",
    # Power BI
    "Powerbi": "Power BI",
    "Powerbi ": "Power BI",
    "Power Bi": "Power BI",
    # Data Analysis
    "Data Analytics": "Data Analysis",
    "Data analysis": "Data Analysis",
    # Communication
    "Communication Skills": "Communication",
    # ML variants
    "Ml": "Machine Learning",
    # Capitalization fixes
    "Aws": "AWS",
    "Gcp": "GCP",
    "Azure": "Azure",
    # skills
    "Problem Solving": "Problem Solving",
    "Analytical Skills": "Analytical Skills",
    "Attention To Detail": "Attention To Detail",
    "Communication Skill": "Communication",
    "Communication Skills": "Communication",
}

def clean_skill(skill):
    if not isinstance(skill, str):
        return ""

    skill = skill.strip()

    if skill == "":
        return ""
    skill = re.sub(r"\s+", " ", skill)
    skill = skill.title()
    skill = ALIASES.get(skill, skill)
    return skill

def is_early_career(title, level):
    if not isinstance(title, str):
        title = ""
    if not isinstance(level, str):
        level = ""
    t = title.lower()
    l = level.lower()
    title_hits = [
        "intern", "internship", "co-op", "coop", "student",
        "new grad", "new graduate", "early career",
        "entry level", "entry-level",
        "junior", "jr"
    ]
    level_hits = ["internship", "entry level", "associate", "junior"]
    return any(k in t for k in title_hits) or any(k in l for k in level_hits)

postings = pd.read_csv("data/raw/job_postings.csv")
skills = pd.read_csv("data/raw/job_skills.csv")
summary = pd.read_csv("data/raw/job_summary.csv")

early_postings = postings[
    postings.apply(
        lambda r: is_early_career(r["job_title"], r["job_level"]),
        axis=1
    )
].copy()
print("Early-career postings:", len(early_postings), "out of", len(postings))
merged = early_postings.merge(skills, on="job_link", how="left")
merged = merged.merge(summary, on="job_link", how="left")
os.makedirs("data/cleaned", exist_ok=True)
merged.to_csv("data/cleaned/internships_full.csv", index=False)
print("Saved: data/cleaned/internships_full.csv  shape =", merged.shape)

merged["job_skills"] = merged["job_skills"].fillna("")
merged["job_skills"] = merged["job_skills"].str.split(",")

exploded = merged.explode("job_skills").copy()
exploded["job_skills"] = exploded["job_skills"].map(clean_skill)
exploded = exploded[exploded["job_skills"] != ""]

exploded["skill_category"] = exploded["job_skills"].map(categorize_skill)

exploded.to_csv("data/cleaned/internships_exploded.csv", index=False)
print("Saved: data/cleaned/internships_exploded.csv  shape =", exploded.shape)

top_skills = exploded["job_skills"].value_counts().head(20)
print("\nTop 20 skills in internships:\n")
print(top_skills)

category_counts = exploded["skill_category"].value_counts()
print("\nSkill category counts:\n")
print(category_counts)

category_counts.to_csv("data/cleaned/skill_category_counts.csv")

job_category = exploded[["job_link", "skill_category"]].drop_duplicates()

jobs_per_category = (
    job_category.groupby("skill_category")["job_link"]
    .nunique()
    .sort_values(ascending=False)
)

total_jobs = exploded["job_link"].nunique()

category_share_df = (jobs_per_category / total_jobs * 100).round(1).reset_index()
category_share_df.columns = ["skill_category", "percent_of_postings"]

print("\nPercent of postings mentioning each category:\n")
print(category_share_df)

category_share_df.to_csv("data/cleaned/skill_category_share.csv", index=False)

top_by_category = (
    exploded.groupby(["skill_category", "job_skills"])
    .size()
    .reset_index(name="count")
    .sort_values(["skill_category", "count"], ascending=[True, False])
)

top_by_category.to_csv("data/cleaned/top_skills_by_category.csv", index=False)
print("\nSaved top skills by category -> data/cleaned/top_skills_by_category.csv")