import pandas as pd

postings = pd.read_csv("data/job_postings.csv")
skills = pd.read_csv("data/job_skills.csv")
summary = pd.read_csv("data/job_summary.csv")

print("\nPostings:")
print(postings.columns)
print(postings.head())
print(postings.info())
print("\nSkills:")
print(skills.columns)
print(skills.head())
print(skills.info())
print("\nSummary:")
print(summary.columns)
print(summary.head())
print(summary.info())
