library(tidyverse)

exploded = read_csv("data/cleaned/internships_exploded.csv")

n_jobs = n_distinct(exploded$job_link)

top10 = exploded %>%
  select(job_link, job_skills) %>%
  distinct() %>%
  count(job_skills, sort = TRUE) %>%
  slice_head(n = 10) %>%
  mutate(percent_of_postings = round(n / n_jobs * 100, 1))

write_csv(top10, "report/top10_skills_percent.csv")
print(top10)
