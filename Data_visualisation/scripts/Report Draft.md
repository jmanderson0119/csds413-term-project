
# Suggested Title:
- **The Academic Treasure Hunt**: **Finding the Hidden Ivies Through Data**
- Beyond the Numbers - What Really Matters When Choosing a University
- **Unmasking Hidden Ivies: A Data-Driven Reveal of True University Quality**

# Idea Behind the visualization:

Many visualizations present absolute values without showing relative context. 
What I mean to say is that absolute numbers can be misleading (they hide the story), and the context around them matters, so we can use relative metrics to reveal them.

So my idea is to reframe the institutional metric into a relative, insight-revealing visualization.

College rankings and comparison sites show you absolute numbers—2,000 faculty, $50M in research, 66% 4-year graduation—but these numbers mean nothing without context. Is 2,000 faculty a lot? For 20,000 students, no. For 5,000 students, yes. We reframe 9 key institutional metrics from absolute to relative measurements, revealing that CWRU's true value is hidden in plain sight.


==I would also like you to add some details about the base visualization we are using (https://datausa.io/profile/university/case-western-reserve-university)==

# Data Sources:

These are our important data sources:
- CWRU [Interactive Factbook](https://case.edu/ir/InteractiveFactBook)![Attachment.tiff](file:///Attachment.tiff) - this was our initial reference, where we noticed that only facts were presented, no reference or relevance provided
- 
- IPEDS Compare Colleges Tool (IPEDS → peer benchmarking): https://nces.ed.gov/ipeds/institution-profile/201645#enrollment
- Integrated Postsecondary Education Data System - this is where we collected most of our data from
- 
- https://datausa.io/profile/university/case-western-reserve-university - this is our actual visualisation reference
- 
- Hidden Ivys link: https://www.rebellionresearch.com/hidden-ivies-2025-ranking-the-definitive-list-of-all-63-hidden-ivy-schools?utm_source=chatgpt.com - we used this link to find schools similar to Case Western, this is a list of 63 hidden Ivy schools by rebellion research.


There are some other references we used:
- NCES or College Scorecard datasets (acceptance rate, cost, ROI)
    
- Institutional Research Tableau Dashboards: https://public.tableau.com/app/profile/cwru.office.of.institutional.research/viz/RetentionandGraduationRates_16248979084830/RetentionandGraduationbyFallEnteringCohort
- https://case.edu/admission/apply/admission-statistics
- Most Important
- https://datausa.io/profile/university/case-western-reserve-university

# Data Collection and Dataset Preparation

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
| Georgia Institute of Technology   |
| Northeastern University           |


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
