library(tidyverse)
source("r_analysis/theme.r")

top_by_cat = read_csv("data/cleaned/top_skills_by_category.csv")

# pick top 5 per category (excluding Other)
plot_df = top_by_cat %>%
  filter(skill_category != "Other") %>%
  group_by(skill_category) %>%
  slice_max(order_by = count, n = 5, with_ties = FALSE) %>%
  ungroup()

p = ggplot(plot_df, aes(x = count, y = reorder(job_skills, count))) +
  geom_col(aes(fill = skill_category)) +
  scale_fill_brewer(palette = "Set2") +
  guides(fill = "none") +
  facet_wrap(~ skill_category, scales = "free_y") +
  labs(
    title = "Top Skills Within Each Category",
    x = "Count",
    y = "Skill"
  ) +
  theme_portfolio() +
  theme(
    strip.text = element_text(face = "bold"),
    plot.margin = margin(10, 20, 10, 10)
  )

print(p)
ggsave("report/figures/top_skills_by_category.png", p, width = 12, height = 8)
