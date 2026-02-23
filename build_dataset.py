import os
import pandas as pd
import re

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

postings = pd.read_csv("data/job_postings.csv")
skills = pd.read_csv("data/job_skills.csv")
summary = pd.read_csv("data/job_summary.csv")

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
exploded["job_skills"] = exploded["job_skills"].astype(str).str.strip()
exploded["job_skills"] = exploded["job_skills"].str.title()
skill_map = {
    "Data Analysis": "Data Analysis",
    "Data analysis": "Data Analysis",
    "Data Analytics": "Data Analysis",
    "Powerbi": "Power BI",
    "Powerbi ": "Power BI",
}
exploded["job_skills"] = exploded["job_skills"].replace(skill_map)
exploded = exploded[exploded["job_skills"] != ""]

exploded.to_csv("data/cleaned/internships_exploded.csv", index=False)
print("Saved: data/cleaned/internships_exploded.csv  shape =", exploded.shape)

top_skills = exploded["job_skills"].value_counts().head(20)
print("\nTop 20 skills in internships:\n")
print(top_skills)