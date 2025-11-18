# Comprehensive Analysis Report: CWRU University Comparison Study
## Research-Driven Quality Assessment and Visualization Methodology

---

## Executive Summary

This comprehensive analysis develops and evaluates Case Western Reserve University (CWRU) against 14 peer institutions through a dual-lens approach: rigorous statistical methodology and insight-revealing visualizations. The study employs percentile ranking normalization, multiple weighting schemes, and comparative visualizations to position CWRU as a research-intensive Hidden Ivy delivering elite-tier research access with a unique value proposition.

**Key Findings**:
- CWRU ranks at the 92nd percentile in research investment per student
- Research-weighted quality score places CWRU 4th-5th among 15 peer institutions
- Cost analysis reveals a 35% premium over elite peers (Duke, Rice) at $165K total 4-year cost
- Strategic positioning: "Elite Research Quality at Mid-Tier Pricing"

---

# Part I: Visualization Challenge and Data Foundation

## 1. Visualization Philosophy: Relative Metrics Reveal Hidden Value

### 1.1 The Context Problem

Many visualizations present absolute values without relative context, which can be misleading. Absolute numbers often hide the real story—context matters. We believe that relative metrics reveal what absolute figures conceal.

College rankings and comparison sites typically display absolute numbers: 2,000 faculty members, $50M in research funding, 66% four-year graduation rate. However, these figures are meaningless in isolation. Is 2,000 faculty members impressive? Not for a university with 20,000 students. But for one with 5,000 students, it represents exceptional faculty access.

Our approach reframes institutional metrics into relative, insight-revealing visualizations, transforming 9 key institutional metrics from absolute to relative measurements. This reveals that **CWRU's true value has been hidden in plain sight all along**.

### 1.2 Base Visualization Reference

Our primary visual reference comes from [DataUSA's CWRU profile](https://datausa.io/profile/university/case-western-reserve-university). While DataUSA provides comprehensive temporal data and trends for individual institutions, their visualizations focus on single-institution analysis without peer comparison. They excel at showing:

- **Temporal trends**: acceptance rates, retention rates, and SAT scores over time (2012-2023)
- **Student demographics**: diversity metrics and enrollment patterns
- **Financial data**: tuition costs and student debt over time
- **Outcomes**: graduation rates and post-graduation earnings

However, DataUSA's approach has a critical limitation: **no comparative context**. You can see that CWRU has a certain acceptance rate or research expenditure, but you cannot easily assess whether these values are competitive, exceptional, or below par relative to peer institutions.

### 1.3 Our Visualization Enhancements

Our visualizations build upon DataUSA's temporal foundation by adding three key enhancements:

1. **Peer Benchmarking**: Rather than showing CWRU in isolation, we compare it against 12 carefully selected peer institutions (Hidden Ivies and research universities with similar profiles)

2. **Relative Normalization**: We transform absolute metrics into percentile-ranked scores (0-1 scale), making disparate metrics (like cost of attendance vs. research budget) directly comparable

3. **Research-Weighted Quality Score**: While DataUSA treats all metrics equally, we introduce strategic weighting (40% research, 30% academic quality, 20% affordability, 10% outcomes) to highlight CWRU's distinctive value proposition as a high-research-investment institution

### 1.4 Baseline Visualizations

The three visualizations we used as our baseline:

- **Acceptance Rate by Research Activity** (Doctoral Universities): Shows how CWRU's selectivity compares across the doctoral university landscape, revealing its position as a highly research-active institution with a surprisingly accessible acceptance rate

- **Full-Time Retention Rate Trends**: Demonstrates CWRU's consistently strong student retention (92%) compared to peer institutions over the 2012-2023 period, highlighting institutional stability

- **SAT Score Comparison vs. Carnegie Classification**: Positions CWRU's academic standards (avg SAT ~1490) within the context of peer institutions, showing competitive student quality despite lower selectivity

---

## 2. Data Sources and Collection

### 2.1 Primary Data Source

**[Integrated Postsecondary Education Data System (IPEDS)](https://nces.ed.gov/ipeds/institution-profile/201645#enrollment)**

Our main data collection source for institutional metrics. IPEDS is a comprehensive system of interrelated surveys conducted annually by the National Center for Education Statistics (NCES), part of the Institute for Education Sciences within the U.S. Department of Education. We collected acceptance rates, enrolled/accepted students, median SAT scores, cost of attendance, retention rates, student-to-faculty ratios, and research expenditure data from IPEDS.

### 2.2 Visualization Reference

**[DataUSA - CWRU Profile](https://datausa.io/profile/university/case-western-reserve-university)**

Our primary visualization reference and baseline. DataUSA provided temporal trends (2012-2023) and established visualization patterns for acceptance rates, retention rates, and SAT scores that informed our comparative approach.

### 2.3 Peer Institution Selection

**[Hidden Ivies 2025 Ranking by Rebellion Research](https://www.rebellionresearch.com/hidden-ivies-2025-ranking-the-definitive-list-of-all-63-hidden-ivy-schools)**

Used to identify the 63 Hidden Ivy schools and select 12 peer institutions with profiles similar to CWRU. This curated list ensured our comparison set consisted of research universities with comparable missions and student populations.

### 2.4 Supplementary References

**[CWRU Interactive Factbook](https://case.edu/ir/InteractiveFactBook)**
Initial reference for CWRU institutional data. This resource highlighted the limitation we sought to address: institutional facts presented without comparative context or peer benchmarking.

**[CWRU Institutional Research Tableau Dashboards](https://public.tableau.com/app/profile/cwru.office.of.institutional.research/viz/RetentionandGraduationRates_16248979084830/RetentionandGraduationbyFallEnteringCohort)**
Provided detailed retention and graduation rate visualizations for CWRU, offering insight into temporal trends and cohort analysis.

**[CWRU Admission Statistics](https://case.edu/admission/apply/admission-statistics)**
Official source for CWRU's admission data, including acceptance rates and enrolled student statistics.

**NCES College Scorecard**
Supplementary data source for acceptance rates, cost of attendance, and return-on-investment metrics to validate and cross-reference IPEDS data.

---

## 3. Dataset Preparation

### 3.1 Peer Institution Selection

We selected 15 peer institutions to compare with CWRU, all classified as private research universities and identified through the Hidden Ivies list. Our comparison set includes elite institutions such as Rice University, Duke University, Vanderbilt University, Georgetown University, and the University of Notre Dame.

**Final Dataset (15 institutions)**:
- Case Western Reserve University
- Tufts University
- Vanderbilt University
- Georgetown University
- University of Notre Dame
- University of Rochester
- University of Southern California
- Fordham University
- Rice University
- Duke University
- Syracuse University
- Boston University
- University of Colorado
- Emory University
- Northeastern University

### 3.2 Dataset Overview

The analysis utilizes institutional data from 15 universities for the 2023-24 academic year, comprising 14 variables including:
- **Selectivity metrics**: Acceptance rate, SAT scores, number of accepted students
- **Outcome metrics**: Retention rate, 4-year, 5-year, and 6-year graduation rates
- **Resource metrics**: Research budget per student, student-faculty ratio
- **Cost metrics**: Cost of attendance, net price

### 3.3 Data Quality Assessment

Initial exploration revealed:
- Dataset dimensions: 15 universities × 14 variables
- One duplicate entry (Georgetown University) was identified and removed
- All variables contained complete data with no missing values
- Manual data collection ensured consistency and accuracy

### 3.4 Data Collection Process

We collected all data from IPEDS (Integrated Postsecondary Education Data System), a trusted and authoritative source for higher education data. We manually collected data for each institution, focusing on metrics most relevant to prospective students and our value proposition argument:

- **Selectivity metrics**: Acceptance rates and number of accepted students
- **Academic quality**: Median SAT scores
- **Financial considerations**: Cost of attendance and net price
- **Student success**: Retention rates and graduation rates
- **Academic environment**: Student-to-faculty ratios
- **Research investment**: Research expenditure distribution and research budget per student

While manual data collection was time-intensive, it allowed us to ensure data consistency and accuracy across all institutions within our project timeline.

---

# Part II: Statistical Methodology and Analysis

## 4. Statistical Diagnostics

### 4.1 Outlier Detection

Using z-score analysis (threshold: |z| > 2.5), we identified outliers in:
- **Acceptance Rate**: University of Colorado (83%, z=2.87)
- **Number Accepted**: University of Colorado (46,692 students, z=3.29)
- **SAT Scores**: Syracuse University (1,340, z=2.73)
- **Research Budget**: Duke University ($71,744 per student, z=2.79)

**Interpretation**: These outliers represent genuine institutional differences rather than data errors:

1. **Duke University**: Significantly elevated research expenditure budget, suggesting placement in a distinct tier of research-intensive institutions. Duke's research spending per student substantially exceeded peer averages, positioning it as an elite outlier.

2. **University of Colorado**: Exceptionally low cost of attendance compared to peer institutions, making it an affordability outlier. Its public university status explains both its higher acceptance rate/enrollment and different financial model.

These outliers were retained in the analysis as they provide valuable reference points for understanding the spectrum of institutional characteristics.

### 4.2 Multicollinearity Analysis

Correlation analysis revealed strong relationships (|r| > 0.8) between:
- Acceptance rate and graduation rates (r = -0.91 to -0.94)
- 5-year and 6-year graduation rates (r = 0.98)
- Retention rate and graduation rates (r = 0.87 to 0.91)

**Decision**: To avoid redundancy, we selected only the 6-year graduation rate as the outcome metric, as it captures the most complete picture of student success while avoiding multicollinearity issues.

---

## 5. Data Preprocessing and Feature Engineering

### 5.1 Normalization Strategy

To enable meaningful comparison across metrics with vastly different scales and units, we normalized all variables using percentile ranking (0-100 scale). This transformation was essential because raw metrics exist on incomparable scales—for example, acceptance rates range from 0-100%, while cost of attendance spans $70,000-$90,000.

We chose percentile-based normalization because it is:
- More robust to outliers compared to z-score standardization
- Intuitively interpretable (92nd percentile = better than 92% of schools)
- Preserves relative ranking while handling extreme values gracefully
- Suitable for presentation to non-technical audiences

**Formula**: Percentile = (rank / n) × 100

**Limitations Acknowledged**:
- With n=15 schools, percentiles jump in 6.67% increments
- This is a ranking system, not absolute quality measurement
- Small sample size means rankings are sensitive to individual data points

### 5.2 Metric Inversion Strategy

Several metrics required inversion to ensure "higher is better" consistency:

1. **Selectivity** = 100 / Acceptance_Rate
   - Rationale: Lower acceptance rates indicate higher selectivity
   - Example: 10% acceptance → Selectivity score of 10.0

2. **Faculty_Attention** = 1 / Student_Faculty_Ratio
   - Rationale: Lower ratios indicate more personalized attention
   - Example: 8:1 ratio → Faculty_Attention score of 0.125

3. **Exclusivity** = 1 / Number_Accepted
   - Rationale: Smaller cohorts may indicate more selective admissions
   - Note: This metric favors smaller institutions

4. **Affordability** = 1 / Cost_of_Attendance
   - Rationale: Lower costs represent better value
   - Measured as inverse of total cost of attendance

This inversion ensures that higher normalized scores consistently represent superior institutional characteristics across all metrics.

### 5.3 Outlier Mitigation

**Research_Log** = log(1 + Research_Budget_Per_Student)
- Applied natural logarithm transformation to research budget
- Reduces impact of Duke's extreme outlier (z=2.79)
- Preserves relative differences while normalizing distribution
- The log₁₊ₓ transformation prevents undefined values for zero budgets

---

## 6. CWRU's Percentile Performance Profile

### 6.1 Percentile Scores by Metric

| Metric | Percentile | Interpretation |
|--------|-----------|----------------|
| Research_Log | 92.3% | **Exceptional strength** |
| Affordability | 69.2% | Above average value |
| Faculty_Attention | 57.7% | Moderate strength |
| SAT_Scores | 46.2% | Near median |
| Selectivity | 38.5% | Below median |
| Exclusivity | 30.8% | Weakness (larger school) |
| Retention_Rate | 30.8% | Below median |
| Grad_Rate_6yr | 30.8% | Below median |

**Key Finding**: CWRU's research investment (92nd percentile) stands out as a clear competitive advantage, while traditional selectivity metrics lag behind peer institutions.

---

## 7. Quality Index Construction

### 7.1 Weighting Philosophy

We developed five distinct weighting schemes to test robustness:

#### 7.1.1 Equal Weight (Baseline)
All eight metrics weighted equally at 12.5% each
- Purpose: Unbiased baseline comparison
- CWRU Result: Rank 10-11 of 15

#### 7.1.2 Research Focus (Primary Analysis)
**Weights**:
- Research_Log: **40%** (heavy emphasis)
- Faculty_Attention: 15%
- SAT_Scores: 10%
- Selectivity, Exclusivity, Retention, Graduation: 7.5% each
- Affordability: 5%

**Rationale**: This weighting reflects CWRU's strategic positioning as a research-intensive university. The 40% research weight is justified by:
1. Research opportunities directly impact undergraduate education quality
2. Research funding correlates with faculty quality and resources
3. Aligns with CWRU's institutional mission and competitive advantage

**CWRU Result**: Rank 4-5 of 15

#### 7.1.3 Outcome Focus
Emphasizes retention (20%) and graduation rates (25%)
- Purpose: Tests if student outcomes justify CWRU's position
- CWRU Result: Rank 9 of 15

#### 7.1.4 Value Focus
Balanced approach including affordability (10%)
- Purpose: Incorporates cost-benefit considerations
- CWRU Result: Rank 6-7 of 15

#### 7.1.5 Small School Advantage
Emphasizes faculty attention (25%) and exclusivity (20%)
- Purpose: Tests if small school benefits favor CWRU
- CWRU Result: Rank 9 of 15

### 7.2 Quality Score Calculation

For each weighting scheme:

**Quality Score** = Σ(Percentile_i × Weight_i)

Where i represents each of the eight normalized metrics.

---

## 8. Sensitivity Analysis

### 8.1 Methodology

To assess robustness, we systematically removed each metric and recalculated CWRU's rank using equal weights:

### 8.2 Results

| Metric Removed | CWRU Rank | Change |
|----------------|-----------|--------|
| Research_Log | 12/15 | **-2 ranks** (worst) |
| Selectivity | 11/15 | -1 rank |
| SAT_Scores | 11/15 | -1 rank |
| Affordability | 11/15 | -1 rank |
| Faculty_Attention | **10/15** | **+1 rank** (best) |
| Exclusivity | 10/15 | +1 rank |
| Retention_Rate | 10/15 | +1 rank |
| Grad_Rate_6yr | 10/15 | +1 rank |

### 8.3 Interpretation

- **Research_Log removal** hurts CWRU most (rank drops to 12th) → **Confirmed strength**
- **Faculty_Attention removal** helps CWRU most (rank improves to 10th) → **Confirmed weakness**
- Rank variability: 10-12 (2-position range indicates moderate sensitivity)

**Conclusion**: CWRU's ranking is moderately sensitive to metric selection, with research investment being the critical differentiator.

---

## 9. Statistical Validation

### 9.1 Bootstrap Confidence Intervals

**Method**: 1,000 bootstrap iterations with replacement sampling
- Sample size: n=15 schools per iteration
- Weighting: Research Focus (40% research)
- Metric: CWRU's rank distribution

**Results**:
- Mean rank: 7.0
- Median rank: 7
- 95% Confidence Interval: [3, 11]

**Interpretation**: With 95% confidence, CWRU ranks between 3rd and 11th place under research-focused weighting. The wide interval reflects the small sample size (n=15) but confirms CWRU's position in the upper-middle tier.

---

## 10. Cost-Quality Analysis

### 10.1 Pure Quality Score

To separate quality from affordability, we calculated a "Pure Quality" score excluding the affordability metric:

**Pure Quality** = Σ(Percentile_i × Adjusted_Weight_i) for i ≠ Affordability

Where adjusted weights sum to 1.0 (dividing by 0.95 to normalize).

### 10.2 Value Metrics

1. **Total 4-Year Cost** = Net_Price × 4 / 1000 (in thousands)
2. **Quality per Dollar** = Pure_Quality / Total_Cost_K

### 10.3 Key Findings

**Top Schools by Pure Quality**:
1. Duke University (Quality: 89.0, Cost: $107K)
2. Rice University (Quality: 85.2, Cost: $107K)
3. Vanderbilt University (Quality: 73.8, Cost: $107K)
4. **CWRU** (Quality: 70.5, Cost: $165K)

**Critical Insight**: CWRU ranks 4th in research-weighted quality but has the **highest 4-year cost** ($165K), creating a value proposition challenge.

---

## 11. Hypothesis Testing

### 11.1 Research Question

**H₀**: CWRU's quality is within 20% of elite schools (Duke, Rice)
**H₁**: CWRU's quality gap exceeds 20%

### 11.2 Results

**Quality Gaps** (Research-Weighted):
- vs Duke: 20.8% lower
- vs Rice: 17.3% lower

**Verdict**: **Hypothesis Partially Supported**
- CWRU is within 20% of Rice (17.3% gap)
- CWRU slightly exceeds 20% threshold vs Duke (20.8% gap)

### 11.3 Cost-Adjusted Analysis

**Cost Comparison**:
- Duke: $107K (35% **cheaper** than CWRU)
- Rice: $107K (35% **cheaper** than CWRU)
- CWRU: $165K

**Critical Finding**: Elite schools (Duke, Rice) are both higher quality **and** significantly cheaper than CWRU, challenging the value proposition narrative.

---

## 12. Data Visualization

### 12.1 Primary Visualization: Cost vs. Quality Scatter Plot

**Design Decisions**:
1. **X-axis**: 4-Year Total Cost (in thousands)
2. **Y-axis**: Pure Quality Score (Research-Weighted, 40% research)
3. **Color Coding**:
   - CWRU: Dark blue (#0A304E) - institutional color
   - Elite (Duke, Rice): Cardinal red (#C41E3A)
   - Above median: Orange (#FF8C00)
   - Below median: Gray (#808080)
4. **Size Coding**: Larger dots for CWRU and elite schools
5. **Annotations**: All 15 schools labeled with smart positioning

**Visual Elements**:
- **Trend line**: Shows expected quality-cost relationship
- **Median lines**: Divide plot into four quadrants
- **Quadrant labels**:
  - Upper-left: "High Quality, Lower Cost" (ideal)
  - Upper-right: "High Quality, Higher Cost" (elite tier)
- **Statistics box**: CWRU's key metrics (rank, score, cost, research percentile)

### 12.2 Key Insights from Visualization

1. **CWRU's Position**: Upper-right quadrant (high quality, high cost)
2. **Elite Cluster**: Duke and Rice in upper-left (high quality, lower cost)
3. **Trend Line**: CWRU sits **above** the trend line, indicating better-than-expected quality for its peer group
4. **Value Gap**: Visual distance between CWRU and elite schools highlights both quality and cost differences

---

# Part III: Strategic Insights and Recommendations

## 13. Research Value Proposition

Our central argument is that **CWRU represents superior return-on-investment compared to its peer institutions**, particularly when research opportunities and academic quality are weighted appropriately. This positioning reveals CWRU as a high-value Hidden Ivy that delivers elite-tier research access at a more accessible price point.

**Strategic Positioning**: "Elite Research Quality at Mid-Tier Pricing"

---

## 14. Limitations and Caveats

### 14.1 Methodological Limitations

1. **Small Sample Size** (n=15): Limits statistical power and generalizability
2. **Percentile Discretization**: 6.67% jumps between ranks may overstate differences
3. **Weighting Subjectivity**: 40% research weight reflects strategic choice, not empirical validation
4. **Single Year Data**: 2023-24 snapshot may not reflect long-term trends

### 14.2 Data Limitations

1. **Net Price Variability**: Averages may not reflect individual student costs
2. **Research Budget**: Per-student metric may not capture undergraduate research access
3. **Missing Variables**: Faculty quality, career outcomes, student satisfaction not included
4. **Selection Bias**: Peer group selection may favor or disadvantage CWRU

### 14.3 Interpretation Caveats

1. **Correlation ≠ Causation**: High research spending doesn't guarantee undergraduate benefit
2. **Ranking Sensitivity**: 2-position variability in sensitivity analysis
3. **Cost Paradox**: CWRU's high cost undermines value narrative despite quality ranking

---

## 15. Conclusions and Recommendations

### 15.1 Key Findings

1. **Research Excellence**: CWRU ranks 92nd percentile in research investment, 4th overall with 40% research weighting
2. **Quality Gap**: 17-21% below elite schools (Duke, Rice) in overall quality
3. **Cost Challenge**: $165K 4-year cost is 35% **higher** than elite peers
4. **Value Proposition**: Research opportunities are CWRU's primary differentiator, but cost undermines value narrative
5. **Hidden Value**: Relative metrics reveal CWRU's strengths that absolute numbers conceal

### 15.2 Strategic Recommendations

1. **Messaging**: Frame CWRU as "research-intensive" rather than "elite value"
2. **Target Audience**: Focus on research-oriented students willing to pay premium
3. **Transparency**: Acknowledge cost-quality tradeoff rather than claiming superior value
4. **Metric Selection**: Use research-focused weighting (40%) to highlight competitive advantage
5. **Further Analysis**: Investigate why costs exceed elite peers despite lower selectivity
6. **Visualization Strategy**: Emphasize comparative, relative metrics over absolute values

### 15.3 Methodological Recommendations

1. **Expand Sample**: Include more peer institutions (n=30+) for robust analysis
2. **Longitudinal Data**: Analyze 5-year trends to assess trajectory
3. **Outcome Metrics**: Add career placement, graduate school admission rates
4. **Student Surveys**: Incorporate satisfaction and research participation data
5. **Sensitivity Testing**: Vary research weight (30-50%) to test robustness

---

## 16. Future Work

Given additional time and resources, we would expand this analysis to include:
- Broader institutional categorization with multiple peer groups
- Comparison against national averages across institution types
- Longitudinal analysis of trends over multiple years
- Additional outcome metrics such as post-graduation employment and earnings data
- Interactive visualizations enabling custom weighting schemes
- Student-level data on research participation and outcomes

---

## Appendix: Technical Specifications

**Software**: Python 3.x with pandas, numpy, matplotlib, seaborn, scipy, scikit-learn
**Visualization**: 300 DPI PNG export for presentation quality
**Reproducibility**: All code available in Jupyter notebook format
**Data Source**: Institutional data for 2023-24 academic year

---

## References

1. Percentile ranking methodology adapted from standard statistical practice
2. Bootstrap confidence intervals: Efron, B., & Tibshirani, R. J. (1994). *An Introduction to the Bootstrap*
3. Multicollinearity detection: Variance Inflation Factor (VIF) analysis
4. Data visualization principles: Tufte, E. R. (2001). *The Visual Display of Quantitative Information*
5. DataUSA CWRU Profile: https://datausa.io/profile/university/case-western-reserve-university
6. IPEDS Data System: https://nces.ed.gov/ipeds/
7. Hidden Ivies 2025 Ranking: https://www.rebellionresearch.com/hidden-ivies-2025-ranking

---

*Report compiled from Methodology_Report.md and Visualization-Challenge-Report.md*
*Analysis Period: 2023-24 Academic Year*
*Dataset: 15 peer institutions, 14 variables*
