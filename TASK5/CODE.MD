
# Advanced Numeric Pattern Generator Using Python

## 1. Problem Statement

Write a Python program to generate a **Hollow Diamond Pattern** or a **Symmetric Numerical Pattern** based on the user's choice and specified dimension. The program must validate the input dimensions, handle invalid choices, and display the pattern with proper alignment.

The dimension must be an integer between 1 and 9.

## 2. Algorithm

1. Start.
2. Display the pattern menu:
   - 1. Hollow Diamond
   - 2. Symmetric Numerical Pyramid
3. Input the user's choice and dimension.
4. Validate the choice and dimension.
5. If the input is invalid, display an error message and stop.
6. If the choice is 1, generate the hollow diamond using loops.
7. If the choice is 2, generate the symmetric numerical pyramid using loops.
8. Display the generated pattern.
9. Stop.

## 3. Flowchart 

```mermaid

    A([Start]) --> B[/Display pattern menu/]
    B --> C[/Input choice and dimension/]
    C --> D{Valid input?}
    D -- No --> E[/Display error message/]
    E --> J([Stop])
    D -- Yes --> F{Choice equals 1?}
    F -- Yes --> G[Generate hollow diamond]
    F -- No --> H[Generate numerical pyramid]
    G --> I[/Display pattern/]
    H --> I
    I --> J
```

## 5. Sample Input


ADVANCED NUMERIC PATTERN GENERATOR
1. Hollow Diamond
2. Symmetric Numerical Pyramid
Enter your choice (1 or 2): 1
Enter dimension (1-9): 5


## 6. Sample Output


Generated Pattern:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *


### Another Sample: Symmetric Numerical Pyramid

**Sample Input**

Enter your choice (1 or 2): 2
Enter dimension (1-9): 5


**Sample Output**

        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1


