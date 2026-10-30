# University Admission Decision Engine Using Python

## 1. Problem Statement

Develop a Python program to evaluate university applicants based on subject eligibility, aggregate marks, course-specific admission thresholds, and tie-breaking criteria. The program should identify eligible applicants and generate a ranked list for each course.

### Requirements
- Accept applicant details, including name, aggregate marks, and subject marks.
- Check whether applicants meet the required subject eligibility criteria.
- Evaluate applicants against course-specific aggregate thresholds.
- Rank eligible applicants based on aggregate marks.
- Use subject marks and applicant ID as tie-breakers when aggregate marks are equal.
- Display eligible applicants in ranked order and list rejected applicants with their reasons for ineligibility.

**Admission rules used in this example:**
1. Each course specifies the required subjects and minimum marks in each subject.
2. Each course has a minimum aggregate percentage.
3. Applicants must satisfy both the subject requirements and the aggregate threshold.
4. Eligible applicants are ranked by:
   - Highest aggregate percentage.
   - Highest total marks in the course's required subjects.
   - Lowest applicant ID if the previous criteria are tied.

*These rules are illustrative and can be changed to match a university's actual admission policy.*

## 2. Algorithm

1. Start.
2. Define the available courses and their admission requirements.
3. Input the number of applicants.
4. For each applicant:
   - Enter the applicant ID and name.
   - Enter the marks obtained in each subject.
   - Calculate the aggregate percentage.
5. Select a course for admission evaluation.
6. Check whether the applicant satisfies the minimum marks required in each compulsory subject.
7. Check whether the applicant meets the course's minimum aggregate percentage.
8. If both conditions are satisfied, mark the applicant as eligible; otherwise, record the reason for rejection.
9. Sort eligible applicants by aggregate percentage, required-subject marks, and applicant ID.
10. Display the ranked list of eligible applicants.
11. Display applicants who do not meet the requirements and their rejection reasons.
12. Stop.

## 3. Flowchart

```mermaid

    A([Start]) --> B[Define course requirements]
    B --> C[/Enter applicant details and marks/]
    C --> D[Calculate aggregate percentage]
    D --> E[Select course]
    E --> F{Meet subject eligibility?}
    F -- No --> G[Record subject eligibility failure]
    F -- Yes --> H{Meet aggregate threshold?}
    H -- No --> I[Record aggregate threshold failure]
    H -- Yes --> J[Add applicant to eligible list]
    G --> K{More applicants?}
    I --> K
    J --> K
    K -- Yes --> C
    K -- No --> L[Rank eligible applicants]
    L --> M[/Display ranked list and rejection reasons/]
    M --> N([Stop])
```
## 5.Sample input
Enter number of applicants: 3

Applicant 1
Applicant ID: 103
Applicant name: Ananya
Mathematics marks (0-100): 90
Physics marks (0-100): 85
Chemistry marks (0-100): 80
English marks (0-100): 75

Applicant 2
Applicant ID: 101
Applicant name: Bharat
Mathematics marks (0-100): 85
Physics marks (0-100): 80
Chemistry marks (0-100): 75
English marks (0-100): 80

Applicant 3
Applicant ID: 102
Applicant name: Charan
Mathematics marks (0-100): 60
Physics marks (0-100): 55
Chemistry marks (0-100): 65
English marks (0-100): 70
           


## 6. Sample Output


=============================================
ADMISSION RANKING: ENGINEERING
Minimum aggregate: 75%
=============================================

Rank | ID | Name | Aggregate | Required-Subject Marks
------------------------------------------------------------
   1 | 103 | Ananya | 82.50% | 255.00
   2 | 101 | Bharat | 80.00% | 240.00

Rejected Applicants:
- Charan (ID: 102)
  Reason: Mathematics marks below required minimum (70)
  Reason: Physics marks below required minimum (60)
  Reason: Aggregate below required minimum (75%)

=============================================
ADMISSION RANKING: SCIENCE
Minimum aggregate: 65%
=============================================

Rank | ID | Name | Aggregate | Required-Subject Marks
------------------------------------------------------------
   1 | 103 | Ananya | 82.50% | 255.00
   2 | 101 | Bharat | 80.00% | 240.00
   3 | 102 | Charan | 62.50% | 180.00

Rejected Applicants:
None

=============================================
ADMISSION RANKING: ARTS
Minimum aggregate: 60%
=============================================

Rank | ID | Name | Aggregate | Required-Subject Marks
------------------------------------------------------------
   1 | 103 | Ananya | 82.50% | 75.00
   2 | 101 | Bharat | 80.00% | 80.00
   3 | 102 | Charan | 62.50% | 70.00

Rejected Applicants:
None
