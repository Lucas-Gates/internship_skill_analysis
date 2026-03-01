import os
import pandas as pd
from itertools import combinations
from collections import Counter

df = pd.read_csv("data/cleaned/internships_exploded.csv")

skills_by_job = (
    df.groupby("job_link")["job_skills"]
      .apply(lambda s: sorted(set([x for x in s if isinstance(x, str) and x.strip()])))
)

pair_counts = Counter()

for skills in skills_by_job:
    if len(skills) < 2:
        continue
    for a, b in combinations(skills, 2):
        pair_counts[(a, b)] += 1

pairs = pd.DataFrame(
    [(a, b, c) for (a, b), c in pair_counts.items()],
    columns=["skill_a", "skill_b", "count"]
).sort_values("count", ascending=False)

os.makedirs("data/cleaned", exist_ok=True)
pairs.to_csv("data/cleaned/skill_pairs.csv", index=False)

print("Saved: data/cleaned/skill_pairs.csv")
print(pairs.head(25))