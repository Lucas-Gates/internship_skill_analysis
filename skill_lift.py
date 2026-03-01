import pandas as pd
from itertools import combinations
from collections import Counter

df = pd.read_csv("data/cleaned/internships_exploded.csv")

total_jobs = df["job_link"].nunique()

# Skills per job
skills_by_job = (
    df.groupby("job_link")["job_skills"]
      .apply(lambda s: sorted(set([x for x in s if isinstance(x, str) and x.strip()])))
)

# Count individual skill frequencies (by job presence, not exploded count)
skill_job_counts = (
    df[["job_link", "job_skills"]]
    .drop_duplicates()
    .groupby("job_skills")["job_link"]
    .nunique()
)

pair_counts = Counter()

for skills in skills_by_job:
    if len(skills) < 2:
        continue
    for a, b in combinations(skills, 2):
        pair_counts[(a, b)] += 1

rows = []

for (a, b), pair_count in pair_counts.items():
    prob_ab = pair_count / total_jobs
    prob_a = skill_job_counts[a] / total_jobs
    prob_b = skill_job_counts[b] / total_jobs

    lift = prob_ab / (prob_a * prob_b)

    rows.append((a, b, pair_count, round(lift, 2)))

lift_df = pd.DataFrame(rows, columns=["skill_a", "skill_b", "count", "lift"])
# Filter out rare pairs (support threshold)
lift_df = lift_df[lift_df["count"] >= 20]

lift_df = lift_df.sort_values("lift", ascending=False)

lift_df.to_csv("data/cleaned/skill_lift.csv", index=False)

print("Saved: data/cleaned/skill_lift.csv")
print(lift_df.head(25))