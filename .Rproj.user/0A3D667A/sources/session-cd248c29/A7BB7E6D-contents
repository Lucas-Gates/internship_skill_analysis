library(tidyverse)
source("r_analysis/theme.R")

exploded = read_csv("data/cleaned/internships_exploded.csv")

top_skills = exploded %>%
  count(job_skills, skill_category, sort = TRUE) %>%
  slice_head(n = 20) %>%
  arrange(n)

p = ggplot(top_skills, aes(x = n, y = reorder(job_skills, n))) +
  geom_col(aes(fill = skill_category)) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Top 20 Skills in Early-Career Data Roles",
    x = "Mentions Across Postings",
    y = "Skill",
    fill = "Category"
  ) +
  theme_portfolio()

print(p)
ggsave("report/figures/top_20_skills.png", p, width = 9, height = 7)
