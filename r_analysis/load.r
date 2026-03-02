library(tidyverse)

exploded = read_csv("data/cleaned/internships_exploded.csv")
cat_share = read_csv("data/cleaned/skill_category_share.csv")
top_by_cat = read_csv("data/cleaned/top_skills_by_category.csv")
lift = read_csv("data/cleaned/skill_lift.csv")

glimpse(exploded)
glimpse(cat_share)
glimpse(top_by_cat)
glimpse(lift)

cat("Unique postings:", n_distinct(exploded$job_link), "\n")
cat("Unique skills:", n_distinct(exploded$job_skills), "\n")