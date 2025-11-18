
# CWRU - A Hidde Ivy 


# Idea Behind the Visualization:

Many visualizations present absolute values without relative context, which can be misleading. Absolute numbers often hide the real story—context matters. We believe that relative metrics reveal what absolute figures conceal.

Our approach reframes institutional metrics into relative, insight-revealing visualizations. College rankings and comparison sites typically display absolute numbers: 2,000 faculty members, $50M in research funding, 66% four-year graduation rate. However, these figures are meaningless in isolation. Is 2,000 faculty members impressive? Not for a university with 20,000 students. But for one with 5,000 students, it represents exceptional faculty access.

We transform 9 key institutional metrics from absolute to relative measurements, revealing that CWRU's true value has been hidden in plain sight all along.

## Base Visualization Reference

Our primary visual reference comes from [DataUSA's CWRU profile](https://datausa.io/profile/university/case-western-reserve-university). While DataUSA provides comprehensive temporal data and trends for individual institutions, their visualizations focus on single-institution analysis without peer comparison. They excel at showing:

- **Temporal trends**: acceptance rates, retention rates, and SAT scores over time (2012-2023)
- **Student demographics**: diversity metrics and enrollment patterns
- **Financial data**: tuition costs and student debt over time
- **Outcomes**: graduation rates and post-graduation earnings

However, DataUSA's approach has a critical limitation: **no comparative context**. You can see that CWRU has a certain acceptance rate or research expenditure, but you cannot easily assess whether these values are competitive, exceptional, or below par relative to peer institutions.

Our visualizations build upon DataUSA's temporal foundation by adding three key enhancements:

1. **Peer Benchmarking**: Rather than showing CWRU in isolation, we compare it against 12 carefully selected peer institutions (Hidden Ivies and research universities with similar profiles)

2. **Relative Normalization**: We transform absolute metrics into percentile-ranked scores (0-1 scale), making disparate metrics (like cost of attendance vs. research budget) directly comparable

3. **Research-Weighted Quality Score**: While DataUSA treats all metrics equally, we introduce strategic weighting (40% research, 30% academic quality, 20% affordability, 10% outcomes) to highlight CWRU's distinctive value proposition as a high-research-investment institution

The three visualizations we used as our baseline:

- **Acceptance Rate by Research Activity** (Doctoral Universities): Shows how CWRU's selectivity compares across the doctoral university landscape, revealing its position as a highly research-active institution with a surprisingly accessible acceptance rate

- **Full-Time Retention Rate Trends**: Demonstrates CWRU's consistently strong student retention (92%) compared to peer institutions over the 2012-2023 period, highlighting institutional stability

- **SAT Score Comparison vs. Carnegie Classification**: Positions CWRU's academic standards (avg SAT ~1490) within the context of peer institutions, showing competitive student quality despite lower selectivity

# Data Sources

We utilized multiple data sources to ensure comprehensive and accurate institutional comparisons:

## Primary Data Source

**[Integrated Postsecondary Education Data System (IPEDS)](https://nces.ed.gov/ipeds/institution-profile/201645#enrollment)**
Our main data collection source for institutional metrics. IPEDS is a comprehensive system of interrelated surveys conducted annually by the National Center for Education Statistics (NCES), part of the Institute for Education Sciences within the U.S. Department of Education. We collected acceptance rates, enrolled/accepted students, median SAT scores, cost of attendance, retention rates, student-to-faculty ratios, and research expenditure data from IPEDS.

## Visualization Reference

**[DataUSA - CWRU Profile](https://datausa.io/profile/university/case-western-reserve-university)**
Our primary visualization reference and baseline. DataUSA provided temporal trends (2012-2023) and established visualization patterns for acceptance rates, retention rates, and SAT scores that informed our comparative approach.

## Peer Institution Selection

**[Hidden Ivies 2025 Ranking by Rebellion Research](https://www.rebellionresearch.com/hidden-ivies-2025-ranking-the-definitive-list-of-all-63-hidden-ivy-schools)**
Used to identify the 63 Hidden Ivy schools and select 12 peer institutions with profiles similar to CWRU. This curated list ensured our comparison set consisted of research universities with comparable missions and student populations.

## Supplementary References

**[CWRU Interactive Factbook](https://case.edu/ir/InteractiveFactBook)**
Initial reference for CWRU institutional data. This resource highlighted the limitation we sought to address: institutional facts presented without comparative context or peer benchmarking.

**[CWRU Institutional Research Tableau Dashboards](https://public.tableau.com/app/profile/cwru.office.of.institutional.research/viz/RetentionandGraduationRates_16248979084830/RetentionandGraduationbyFallEnteringCohort)**
Provided detailed retention and graduation rate visualizations for CWRU, offering insight into temporal trends and cohort analysis.

**[CWRU Admission Statistics](https://case.edu/admission/apply/admission-statistics)**
Official source for CWRU's admission data, including acceptance rates and enrolled student statistics.

**NCES College Scorecard**
Supplementary data source for acceptance rates, cost of attendance, and return-on-investment metrics to validate and cross-reference IPEDS data.

# Data Collection and Dataset Preparation

## Peer Institution Selection

We selected 13 peer institutions to compare with CWRU, all classified as private research universities and identified through the Hidden Ivies list. Our comparison set includes elite institutions such as Rice University, Duke University, Vanderbilt University, Georgetown University, and the University of Notre Dame.

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

## Data Collection Process

We collected all the data from IPEDS i.e. the **Integrated Postsecondary Education Data System**. Which is a system of interrelated surveys conducted annually by the [National Center for Education Statistics](https://en.wikipedia.org/wiki/National_Center_for_Education_Statistics "National Center for Education Statistics") (NCES), a part of the [Institute for Education Sciences](https://en.wikipedia.org/wiki/Institute_for_Education_Sciences "Institute for Education Sciences") within the [United States Department of Education](https://en.wikipedia.org/wiki/United_States_Department_of_Education "United States Department of Education").

IPEDS is a trusted and authoritative source for higher education data. We manually collected data for each institution, focusing on metrics most relevant to prospective students and our value proposition argument:

- **Selectivity metrics**: Acceptance rates and number of accepted students
- **Academic quality**: Median SAT scores
- **Financial considerations**: Cost of attendance and net price
- **Student success**: Retention rates and graduation rates
- **Academic environment**: Student-to-faculty ratios
- **Research investment**: Research expenditure distribution and research budget per student

While manual data collection was time-intensive, it allowed us to ensure data consistency and accuracy across all institutions within our project timeline.

## Research Value Proposition

Our central argument is that **CWRU represents superior return-on-investment compared to its peer institutions**, particularly when research opportunities and academic quality are weighted appropriately. This positioning reveals CWRU as a high-value Hidden Ivy that delivers elite-tier research access at a more accessible price point.

## Future Work

Given additional time and resources, we would expand this analysis to include:
- Broader institutional categorization with multiple peer groups
- Comparison against national averages across institution types
- Longitudinal analysis of trends over multiple years
- Additional outcome metrics such as post-graduation employment and earnings data

# Data Preprocessing

## Normalization Strategy

To enable meaningful comparison across metrics with vastly different scales and units, we normalized all variables using min-max scaling to a 0-1 range. This transformation was essential because raw metrics exist on incomparable scales—for example, acceptance rates range from 0-100%, while cost of attendance spans $70,000-$90,000.

We chose percentile-based normalization because it is more robust to outliers compared to z-score standardization, preserving the relative ranking of institutions while handling extreme values gracefully.

## Metric Inversion

For metrics where lower values indicate better performance, we applied inverse transformations before normalization:

- **Acceptance rate**: Lower selectivity percentage = higher exclusivity
- **Student-to-faculty ratio**: Lower ratio = better faculty access
- **Number of accepted students**: Lower count = higher selectivity
- **Cost of attendance**: Lower cost = better affordability

This inversion ensures that higher normalized scores consistently represent superior institutional characteristics across all metrics.

## Outlier Detection

Our analysis identified two notable outliers:

1. **Duke University**: Significantly elevated research expenditure budget, suggesting placement in a distinct tier of research-intensive institutions. Duke's research spending per student substantially exceeded peer averages, positioning it as an elite outlier.

2. **University of Colorado**: Exceptionally low cost of attendance compared to peer institutions, making it an affordability outlier. This suggests Colorado operates under a different financial model than other institutions in our comparison set.

These outliers were retained in the analysis rather than removed, as they provide valuable reference points for understanding the spectrum of institutional characteristics within the Hidden Ivies and peer research universities.



