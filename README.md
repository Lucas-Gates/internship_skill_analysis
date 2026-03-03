# Early-Career Data Skills Intelligence

## Overview

For this project, I analyzed 1,426 job postings and over
35,000 extracted skill mentions to identify high-demand skills and
statistically significant technical skill stacks in data science and
computer science roles.

Using a Python data pipeline and R-based visualization, my
analysis transforms raw job posting data into structured labor market
data.

------------------------------------------------------------------------

## Objectives

-   Clean and normalize skill labels across postings
-   Categorize skills
-   Measure skill co-occurrence using lift (association strength)
-   Identify statistically significant early-career technical stacks
-   Produce good visualizations for clear communication

------------------------------------------------------------------------

## Methodology

### 1. Data Pipeline (Python)

-   Merged job postings, skills, and summaries using relational keys
-   Implemented alias normalization and whitespace cleaning
-   Built a system to classify skills into:
    -   Language
    -   Database
    -   Visualization / BI
    -   ML / AI
    -   Data Engineering
    -   Cloud
    -   Stats / Math
    -   Soft Skills
-   Computed co-occurrence
-   Calculated lift to identify skill associations beyond random chance

### 2. Visualization & Reporting (R)

-   Category prevalence across postings
-   Top 20 in-demand skills
-   Top technical skill stacks by lift
-   Top skills within each technical category

------------------------------------------------------------------------

## Key Findings

-   Soft skills appear in ~64% of early-career postings, but technical
    categories such as databases and visualization tools are almost as
    common.
-   SQL and Python are the most frequently mentioned technical skills.
-   Distinct technical stacks emerge:
    -   **BI Stack:** Business Intelligence + SQL Server + Power BI
    -   **ML Stack:** PyTorch + TensorFlow
    -   **Data Engineering Stack:** Hadoop + Spark
-   Python and R frequently co-occur in specialized analytics roles.

------------------------------------------------------------------------

## Tech Stack

-   Python (pandas)
-   R (tidyverse / ggplot2)
-   Regex-based classification
-   Association analysis (lift)
-   Data visualization best practices

------------------------------------------------------------------------

## How to Run

### Python Pipeline

``` bash
python python/build_dataset.py
python python/skill_cooccurrence.py
python python/skill_lift.py
```

### R Visualizations

``` r
source("r_analysis/category_share.r")
source("r_analysis/top_skills.r")
source("r_analysis/top_by_category.r")
source("r_analysis/lift_pairs.r")
```