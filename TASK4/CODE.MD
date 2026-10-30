# Student Performance Trend Analysis Using Python

## 1. Problem Statement

Student Performance Trend Analysis is a Python program designed to analyze students' examination scores across multiple examinations. It compares assessment scores, calculates improvements and declines, identifies consistently weak subjects, and classifies students according to predefined performance criteria.

The program performs the following operations:

1. Accept the number of students, subjects, and examinations.
2. Input each student's scores for every subject across multiple examinations.
3. Calculate the average score for each student in each examination.
4. Compare consecutive examination scores to determine improvements or declines.
5. Identify subjects in which a student consistently scores below the specified pass mark.
6. Classify students according to their overall average scores.
7. Display a performance report containing averages, trends, weak subjects, and student classifications.

### Assumptions

- Each examination is scored out of 100 marks per subject.
- The pass mark for a subject is 40.
- A student is classified according to their average score across all subjects in the latest examination.
- Student classifications are:
  - **Excellent:** 85–100
  - **Good:** 70–84.99
  - **Average:** 50–69.99
  - **Needs Improvement:** Below 50
- A subject is considered consistently weak if the student scores below 40 in every examination.
- Improvement or decline is calculated by comparing the average score of consecutive examinations.

## 2. Algorithm

1. Start the program.
2. Input the number of students, subjects, and examinations.
3. Set the pass mark and student classification criteria.
4. For each student:
   - Enter the student's name.
   - Input scores for every subject across all examinations.
   - Validate that each score is between 0 and 100.
5. Calculate the average score for each examination.
6. Compare consecutive examination averages to identify improvements or declines.
7. Identify consistently weak subjects by checking whether the score is below 40 in every examination.
8. Calculate the student's overall average for the latest examination.
9. Classify the student as Excellent, Good, Average, or Needs Improvement.
10. Display the performance analysis for each student.
11. Repeat the process for all students.
12. Stop the program.

## 3. Flowchart 

```mermaid
    A([Start]) --> B[Enter student and examination details]
    B --> C[Input subject scores]
    C --> D[Calculate examination averages]
    D --> E[Compare examination results]
    E --> F[Identify consistently weak subjects]
    F --> G[Classify student by latest average]
    G --> H[Display performance report]
    H --> I{More students?}
    I -->|Yes| C
    I -->|No| J([Stop])
```



## 5. Sample Input


Enter number of students: 2
Enter number of subjects: 2
Enter number of examinations: 3
Enter subject 1 name: Mathematics
Enter subject 2 name: Science

===== Student 1 =====
Enter student name: Asha
Mathematics - Exam 1 score: 80
Mathematics - Exam 2 score: 85
Mathematics - Exam 3 score: 90
Science - Exam 1 score: 75
Science - Exam 2 score: 80
Science - Exam 3 score: 85

===== Student 2 =====
Enter student name: Rohan
Mathematics - Exam 1 score: 35
Mathematics - Exam 2 score: 38
Mathematics - Exam 3 score: 30
Science - Exam 1 score: 55
Science - Exam 2 score: 50
Science - Exam 3 score: 45


## 6. Sample Output
===== Student 1 =====

Examination Performance:
Exam 1 Average: 77.50
Exam 2 Average: 82.50
Exam 3 Average: 87.50

Performance Trends:
Exam 1 to Exam 2: Improved by 5.00 marks
Exam 2 to Exam 3: Improved by 5.00 marks

===== PERFORMANCE REPORT =====
Student Name: Asha
Latest Exam Average: 87.50
Classification: Excellent
Consistently Weak Subjects: None
==============================

===== Student 2 =====

Examination Performance:
Exam 1 Average: 45.00
Exam 2 Average: 44.00
Exam 3 Average: 37.50

Performance Trends:
Exam 1 to Exam 2: Declined by 1.00 marks
Exam 2 to Exam 3: Declined by 6.50 marks

===== PERFORMANCE REPORT =====
Student Name: Rohan
Latest Exam Average: 37.50
Classification: Needs Improvement
Consistently Weak Subjects: Mathematics
==============================

Student performance analysis completed.


