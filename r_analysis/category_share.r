library(tidyverse)
source("r_analysis/theme.r")

cat_share = read_csv("data/cleaned/skill_category_share.csv")

# remove "Other" from the plot (it is always 100% by construction)
plot_df = cat_share %>%
  filter(skill_category != "Other") %>%
  arrange(percent_of_postings)

p = ggplot(plot_df, aes(x = percent_of_postings, y = reorder(skill_category, percent_of_postings))) +
  geom_col(aes(fill = percent_of_postings)) +
  scale_fill_gradient(low = "#90CAF9", high = "#0D47A1") +
  guides(fill = "none") +
  labs(
    title = "Technical Skill Categories Mentioned in Early-Career Postings",
    x = "% of postings mentioning category",
    y = "Category"
  ) +
  theme_portfolio()

print(p)

ggsave("report/figures/category_share.png", p, width = 9, height = 5)

