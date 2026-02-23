import os
import pandas as pd

postings = pd.read_csv("data/job_postings.csv")
skills = pd.read_csv("data/job_skills.csv")
summary = pd.read_csv("data/job_summary.csv")
intern_postings = postings[postings["job_title"].str.contains("intern", case=False, na=False)].copy()
print("Intern postings:", len(intern_postings), "out of", len(postings))

merged = intern_postings.merge(skills, on="job_link", how="left")
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