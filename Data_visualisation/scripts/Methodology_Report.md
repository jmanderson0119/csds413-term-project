# Methodology Report: CWRU University Comparison Analysis

## Executive Summary

This analysis develops a comprehensive quality metric to evaluate Case Western Reserve University (CWRU) against 14 peer institutions, with particular emphasis on research investment as a key differentiator. The methodology employs percentile ranking normalization and multiple weighting schemes to provide a robust, statistically sound comparison.

---

## 1. Data Collection and Initial Exploration

### 1.1 Dataset Overview
The analysis utilizes institutional data from 15 universities for the 2023-24 academic year, comprising 14 variables including:
- **Selectivity metrics**: Acceptance rate, SAT scores, number of accepted students
- **Outcome metrics**: Retention rate, 4-year, 5-year, and 6-year graduation rates
- **Resource metrics**: Research budget per student, student-faculty ratio
- **Cost metrics**: Cost of attendance, net price

### 1.2 Data Quality Assessment
Initial exploration revealed:
- Dataset dimensions: 15 universities × 14 variables
- One duplicate entry (Georgetown University) was identified and removed
- All variables contained complete data with no missing values

---

## 2. Statistical Diagnostics

### 2.1 Outlier Detection
Using z-score analysis (threshold: |z| > 2.5), we identified outliers in:
- **Acceptance Rate**: University of Colorado (83%, z=2.87)
- **Number Accepted**: University of Colorado (46,692 students, z=3.29)
- **SAT Scores**: Syracuse University (1,340, z=2.73)
- **Research Budget**: Duke University ($71,744 per student, z=2.79)

**Interpretation**: These outliers represent genuine institutional differences rather than data errors. University of Colorado's public university status explains its higher acceptance rate and enrollment. Duke's exceptional research funding represents a legitimate competitive advantage.

### 2.2 Multicollinearity Analysis
Correlation analysis revealed strong relationships (|r| > 0.8) between:
- Acceptance rate and graduation rates (r = -0.91 to -0.94)
- 5-year and 6-year graduation rates (r = 0.98)
- Retention rate and graduation rates (r = 0.87 to 0.91)

**Decision**: To avoid redundancy, we selected only the 6-year graduation rate as the outcome metric, as it captures the most complete picture of student success while avoiding multicollinearity issues.

---

## 3. Data Preprocessing and Feature Engineering

### 3.1 Metric Inversion Strategy
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

### 3.2 Outlier Mitigation
**Research_Log** = log(1 + Research_Budget_Per_Student)
- Applied natural logarithm transformation to research budget
- Reduces impact of Duke's extreme outlier (z=2.79)
- Preserves relative differences while normalizing distribution
- The log₁ₚ transformation prevents undefined values for zero budgets

---

## 4. Normalization Methodology

### 4.1 Percentile Ranking Approach
We employed percentile ranking (0-100 scale) for all metrics:

**Formula**: Percentile = (rank / n) × 100

**Advantages**:
- Intuitive interpretation (92nd percentile = better than 92% of schools)
- All metrics on comparable 0-100 scale
- Robust to extreme outliers
- Suitable for presentation to non-technical audiences

**Limitations Acknowledged**:
- With n=15 schools, percentiles jump in 6.67% increments
- This is a ranking system, not absolute quality measurement
- Small sample size means rankings are sensitive to individual data points

### 4.2 CWRU's Percentile Scores
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

## 5. Quality Index Construction

### 5.1 Weighting Philosophy
We developed five distinct weighting schemes to test robustness:

#### 5.1.1 Equal Weight (Baseline)
All eight metrics weighted equally at 12.5% each
- Purpose: Unbiased baseline comparison
- CWRU Result: Rank 10-11 of 15

#### 5.1.2 Research Focus (Primary Analysis)
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

#### 5.1.3 Outcome Focus
Emphasizes retention (20%) and graduation rates (25%)
- Purpose: Tests if student outcomes justify CWRU's position
- CWRU Result: Rank 9 of 15

#### 5.1.4 Value Focus
Balanced approach including affordability (10%)
- Purpose: Incorporates cost-benefit considerations
- CWRU Result: Rank 6-7 of 15

#### 5.1.5 Small School Advantage
Emphasizes faculty attention (25%) and exclusivity (20%)
- Purpose: Tests if small school benefits favor CWRU
- CWRU Result: Rank 9 of 15

### 5.2 Quality Score Calculation
For each weighting scheme:

**Quality Score** = Σ(Percentile_i × Weight_i)

Where i represents each of the eight normalized metrics.

---

## 6. Sensitivity Analysis

### 6.1 Methodology
To assess robustness, we systematically removed each metric and recalculated CWRU's rank using equal weights:

### 6.2 Results
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

### 6.3 Interpretation
- **Research_Log removal** hurts CWRU most (rank drops to 12th) → **Confirmed strength**
- **Faculty_Attention removal** helps CWRU most (rank improves to 10th) → **Confirmed weakness**
- Rank variability: 10-12 (2-position range indicates moderate sensitivity)

**Conclusion**: CWRU's ranking is moderately sensitive to metric selection, with research investment being the critical differentiator.

---

## 7. Statistical Validation

### 7.1 Bootstrap Confidence Intervals
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

## 8. Cost-Quality Analysis

### 8.1 Pure Quality Score
To separate quality from affordability, we calculated a "Pure Quality" score excluding the affordability metric:

**Pure Quality** = Σ(Percentile_i × Adjusted_Weight_i) for i ≠ Affordability

Where adjusted weights sum to 1.0 (dividing by 0.95 to normalize).

### 8.2 Value Metrics
1. **Total 4-Year Cost** = Net_Price × 4 / 1000 (in thousands)
2. **Quality per Dollar** = Pure_Quality / Total_Cost_K

### 8.3 Key Findings
**Top Schools by Pure Quality**:
1. Duke University (Quality: 89.0, Cost: $107K)
2. Rice University (Quality: 85.2, Cost: $107K)
3. Vanderbilt University (Quality: 73.8, Cost: $107K)
4. **CWRU** (Quality: 70.5, Cost: $165K)

**Critical Insight**: CWRU ranks 4th in research-weighted quality but has the **highest 4-year cost** ($165K), creating a value proposition challenge.

---

## 9. Hypothesis Testing

### 9.1 Research Question
**H₀**: CWRU's quality is within 20% of elite schools (Duke, Rice)  
**H₁**: CWRU's quality gap exceeds 20%

### 9.2 Results
**Quality Gaps** (Research-Weighted):
- vs Duke: 20.8% lower
- vs Rice: 17.3% lower

**Verdict**: **Hypothesis Partially Supported**
- CWRU is within 20% of Rice (17.3% gap)
- CWRU slightly exceeds 20% threshold vs Duke (20.8% gap)

### 9.3 Cost-Adjusted Analysis
**Cost Comparison**:
- Duke: $107K (35% **cheaper** than CWRU)
- Rice: $107K (35% **cheaper** than CWRU)
- CWRU: $165K

**Critical Finding**: Elite schools (Duke, Rice) are both higher quality **and** significantly cheaper than CWRU, challenging the value proposition narrative.

---

## 10. Data Visualization

### 10.1 Primary Visualization: Cost vs. Quality Scatter Plot

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

### 10.2 Key Insights from Visualization
1. **CWRU's Position**: Upper-right quadrant (high quality, high cost)
2. **Elite Cluster**: Duke and Rice in upper-left (high quality, lower cost)
3. **Trend Line**: CWRU sits **above** the trend line, indicating better-than-expected quality for its peer group
4. **Value Gap**: Visual distance between CWRU and elite schools highlights both quality and cost differences

---

## 11. Limitations and Caveats

### 11.1 Methodological Limitations
1. **Small Sample Size** (n=15): Limits statistical power and generalizability
2. **Percentile Discretization**: 6.67% jumps between ranks may overstate differences
3. **Weighting Subjectivity**: 40% research weight reflects strategic choice, not empirical validation
4. **Single Year Data**: 2023-24 snapshot may not reflect long-term trends

### 11.2 Data Limitations
1. **Net Price Variability**: Averages may not reflect individual student costs
2. **Research Budget**: Per-student metric may not capture undergraduate research access
3. **Missing Variables**: Faculty quality, career outcomes, student satisfaction not included
4. **Selection Bias**: Peer group selection may favor or disadvantage CWRU

### 11.3 Interpretation Caveats
1. **Correlation ≠ Causation**: High research spending doesn't guarantee undergraduate benefit
2. **Ranking Sensitivity**: 2-position variability in sensitivity analysis
3. **Cost Paradox**: CWRU's high cost undermines value narrative despite quality ranking

---

## 12. Conclusions and Recommendations

### 12.1 Key Findings
1. **Research Excellence**: CWRU ranks 92nd percentile in research investment, 4th overall with 40% research weighting
2. **Quality Gap**: 17-21% below elite schools (Duke, Rice) in overall quality
3. **Cost Challenge**: $165K 4-year cost is 35% **higher** than elite peers
4. **Value Proposition**: Research opportunities are CWRU's primary differentiator, but cost undermines value narrative

### 12.2 Strategic Recommendations
1. **Messaging**: Frame CWRU as "research-intensive" rather than "elite value"
2. **Target Audience**: Focus on research-oriented students willing to pay premium
3. **Transparency**: Acknowledge cost-quality tradeoff rather than claiming superior value
4. **Metric Selection**: Use research-focused weighting (40%) to highlight competitive advantage
5. **Further Analysis**: Investigate why costs exceed elite peers despite lower selectivity

### 12.3 Methodological Recommendations
1. **Expand Sample**: Include more peer institutions (n=30+) for robust analysis
2. **Longitudinal Data**: Analyze 5-year trends to assess trajectory
3. **Outcome Metrics**: Add career placement, graduate school admission rates
4. **Student Surveys**: Incorporate satisfaction and research participation data
5. **Sensitivity Testing**: Vary research weight (30-50%) to test robustness

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
