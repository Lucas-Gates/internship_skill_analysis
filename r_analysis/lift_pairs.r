library(tidyverse)
source("r_analysis/theme.R")

lift = read_csv("data/cleaned/skill_lift.csv")

top_lift = lift %>%
  arrange(desc(lift)) %>%
  slice_head(n = 15) %>%
  mutate(pair = paste(skill_a, "+", skill_b)) %>%
  arrange(lift)

top_lift = top_lift %>%
  mutate(pair = gsub(" \\(Programming Language\\)", "", pair))

p = ggplot(top_lift, aes(x = lift, y = reorder(pair, lift))) +
  geom_col(aes(fill = lift)) +
  scale_fill_gradient(low = "#B3E5FC", high = "#01579B") +
  guides(fill = "none") +
  labs(
    title = "Top Technical Skill Pairs (Lift: More-Than-Expected Co-Occurrence)",
    x = "Lift",
    y = "Skill Pair"
  ) +
  theme_portfolio() +
  theme(plot.margin = margin(10, 40, 10, 10))

print(p)
ggsave("report/figures/top_lift_pairs.png", p, width = 13, height = 7)
