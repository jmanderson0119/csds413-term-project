
# CWRU - A Hidde Ivy 


# Idea Behind the Visualization:

Many visualizations present absolute values without relative context, which can be misleading. Absolute numbers often hide the real story—context matters. We believe that relative metrics reveal what absolute figures conceal.

Our approach reframes institutional metrics into relative, insight-revealing visualizations. College rankings and comparison sites typically display absolute numbers: 2,000 faculty members, $50M in research funding, 66% four-year graduation rate. However, these figures are meaningless in isolation. Is 2,000 faculty members impressive? Not for a university with 20,000 students. But for one with 5,000 students, it represents exceptional faculty access.

We transform 9 key institutional metrics from absolute to relative measurements, revealing that CWRU's true value has been hidden in plain sight all along.

## Base Visualization Reference

Our primary visual reference comes from [DataUSA's CWRU profile](https://datausa.io/profile/university/case-western-reserve-university). DataUSA provides comprehensive temporal data and trends for individual institutions, with three key visualization types that informed our approach:

1. **Acceptance Rate by Research Activity (Doctoral Universities)**: A horizontal bar chart showing acceptance rates for doctoral universities, categorized by research activity level. CWRU appears as a highly research-active institution with approximately 28% acceptance rate.

2. **Full-Time Retention Rate Trends**: A multi-line temporal chart tracking retention rates from 2012-2023 across multiple institutions. CWRU's red line shows consistent performance around 92% retention, compared to peer institutions ranging from 90-98%.

3. **SAT Score Comparison vs. Carnegie Classification**: A scatter plot comparing critical reading and math scores across CWRU and Carnegie parent institutions, showing CWRU's average scores around 700-750 for both sections (approximately 1490 combined).

### What DataUSA Does Well

DataUSA excels at presenting:
- **Temporal trends**: Multi-year patterns in acceptance rates, retention rates, and SAT scores (2012-2023)
- **Single-institution focus**: Deep dive into one university's metrics over time
- **Visual clarity**: Clean, readable charts with proper labeling and legends
- **Categorical comparisons**: Grouping by Carnegie classification or research activity level

### Critical Limitation: No Contextual Benchmarking

However, DataUSA's approach has a significant limitation: **lack of strategic peer comparison and relative positioning**. While you can see that CWRU has a certain acceptance rate or research expenditure, you cannot easily assess:
- Where CWRU ranks among carefully selected peer institutions
- Whether these absolute values represent competitive advantages or disadvantages
- How different institutional characteristics should be weighted based on strategic priorities
- What CWRU's relative value proposition is compared to similar Hidden Ivies

### Our Enhancements

We build upon DataUSA's temporal foundation by adding three key analytical layers:

1. **Strategic Peer Benchmarking**: Rather than showing CWRU alongside all doctoral universities or Carnegie classifications, we compare it against 12 carefully selected peer institutions (Hidden Ivies and research universities with similar profiles: Rice, Duke, Vanderbilt, Georgetown, Notre Dame, etc.)

2. **Relative Normalization**: We transform absolute metrics into percentile-ranked scores (0-1 scale), making disparate metrics (like cost of attendance vs. research budget) directly comparable and revealing relative positioning

3. **Research-Weighted Quality Score**: While DataUSA treats all metrics equally, we introduce strategic weighting (40% research, 30% academic quality, 20% affordability, 10% outcomes) to highlight CWRU's distinctive value proposition as a high-research-investment institution

This approach shifts from "what are CWRU's numbers?" to "what is CWRU's competitive position and value story?"

# Data Sources

We utilized multiple data sources to ensure comprehensive and accurate institutional comparisons:

## Primary Data Source

- **[IPEDS (Integrated Postsecondary Education Data System)](https://nces.ed.gov/ipeds/)** - Our main data collection source. IPEDS is a system of interrelated surveys conducted annually by the National Center for Education Statistics (NCES), part of the Institute for Education Sciences within the U.S. Department of Education. We collected institutional metrics including:
  - Acceptance rates and enrolled/accepted students
  - Median SAT scores
  - Cost of attendance and net price
  - Retention and graduation rates
  - Student-to-faculty ratios
  - Research expenditure distribution and budget

## Visualization Reference

- **[DataUSA - CWRU Profile](https://datausa.io/profile/university/case-western-reserve-university)** - Our primary visualization reference, providing temporal trends and baseline visualizations for institutional metrics (2012-2023)

## Peer Institution Selection

- **[Hidden Ivies 2025 Ranking by Rebellion Research](https://www.rebellionresearch.com/hidden-ivies-2025-ranking-the-definitive-list-of-all-63-hidden-ivy-schools)** - Used to identify the 63 Hidden Ivy schools and select 12 peer institutions similar to CWRU in profile and mission

## Supplementary References

- **[CWRU Interactive Factbook](https://case.edu/ir/InteractiveFactBook)** - Initial reference showing institutional facts without comparative context
- **[IPEDS Compare Colleges Tool](https://nces.ed.gov/ipeds/institution-profile/201645#enrollment)** - Peer benchmarking interface
- **[CWRU Institutional Research Tableau Dashboards](https://public.tableau.com/app/profile/cwru.office.of.institutional.research/viz/RetentionandGraduationRates_16248979084830/RetentionandGraduationbyFallEnteringCohort)** - Retention and graduation rate visualizations
- **[CWRU Admission Statistics](https://case.edu/admission/apply/admission-statistics)** - Official admission data
- **NCES College Scorecard** - Additional data on acceptance rates, cost, and ROI

# Data Collection and Dataset Preparation

<<<<<<< HEAD
=======
List of universities we are comparing:

|                                   |
| --------------------------------- |
| Case Western Reserve University   |
| Tufts University                  |
| Vanderbilt University             |
| Georgetown University             |
| University of Notre Dame          |
| University of Rochester           |
| University of Southern California |
| Fordham University                |
| Rice University                   |
| Duke University                   |
| Syracuse University               |
| Boston University                 |
| University of Colorado            |
| Georgetown University             |
| Emory University                  |
| Northeastern University           |


>>>>>>> f1372c1d72bc12f9b6a02d0112a785d306e1d00d
We collected all the data from IPEDS i.e. the **Integrated Postsecondary Education Data System**. Which is a system of interrelated surveys conducted annually by the [National Center for Education Statistics](https://en.wikipedia.org/wiki/National_Center_for_Education_Statistics "National Center for Education Statistics") (NCES), a part of the [Institute for Education Sciences](https://en.wikipedia.org/wiki/Institute_for_Education_Sciences "Institute for Education Sciences") within the [United States Department of Education](https://en.wikipedia.org/wiki/United_States_Department_of_Education "United States Department of Education").

It is a trusted source for collecting university-related data. I filtered my search by universities and populated the table for various factors.
The data collection was done manually, which is not ideal but given the tight timeline, this was the way to go.

We collected factors that we thought were important when considering taking admission to a university, like acceptance rate, enrolled/accepted students, Median SAT Scores, Cost of attendance, retention rate, student-to-faculty ratio, and the most important one in our argument, the expense distribution and research budget.

Our argument is that CWRU is a better return-on-investment school as compared to its other peers.

For our analysis, we considered ==13 (This number will change)== peer schools, of which few can also be considered as elite. Including Rice University, Duke, Southern California, Tufts, Notre Dame etc.

All these universities are Private research universities.

Given more time, our dataset would have been more comprehensive, and we would have categorized all these universities into one group, naming them peer universities, and would have compared CWRU with peer groups and the national average.

# Data Preprocessing

Moving on to the data pre-processing part

I had to normalize all the columns to make them comparable. We used percentile ranking as it is more robust to outliers. For example, the acceptance rate was on a percentage scale, and the cost of attendance was somewhere in the range of 70000 to 90000 dollars.

We did some outlier detection too, and it turned out that Duke University was being an outlier, probably because of a very high research expense budget, which probably suggests that it was in a different tier or cluster. Also, the University of Colorado stands out to be another outlier for being extremely affordable.

We inverted the metrics acceptance rate, student-faculty ratio, accepted students, and cost of attendance for 'lower is better' variables





# **Presentation Strategy:**

1. **Acknowledge limitations upfront**: "This weighting emphasizes research opportunities"
2. **Show sensitivity analysis**: Display how rankings change with different weights
3. **Focus on value proposition**: CWRU as "best research value" not "best overall"
4. **Use relative positioning**: "Top tier for research, mid-tier price"
