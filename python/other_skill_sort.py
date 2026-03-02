import pandas as pd

df = pd.read_csv("data/cleaned/internships_exploded.csv")

other = df[df["skill_category"] == "Other"]

top_other = other["job_skills"].value_counts().head(50)

print("\nTop 50 skills currently categorized as Other:\n")
print(top_other)