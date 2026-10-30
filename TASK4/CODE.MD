# Multi-Day Water Tank Simulation Using Python

## 1. Problem Statement

The Multi-Day Water Tank Simulation is a Python program that simulates changes in the water level of a tank over multiple days based on varying inflow and outflow quantities.

The program accepts the tank's initial water level, maximum capacity, minimum required water level, and daily inflow and outflow quantities. It updates the water level after each interval, detects overflow and water shortages, and determines the first interval in which the water level reaches or exceeds a specified threshold.

The program performs the following operations:

1. Accept the initial water level, tank capacity, and target water level.
2. Accept the inflow and outflow quantities for each day.
3. Calculate the updated water level after every interval.
4. Detect overflow when the incoming water exceeds the tank's available capacity.
5. Detect water shortages when the outflow exceeds the available water.
6. Maintain the water level within the tank's physical limits.
7. Identify the first interval in which the water level reaches or exceeds the specified threshold.
8. Display a daily simulation report and the final water level.

### Assumptions

- All water quantities are measured in litres.
- Inflow and outflow quantities must be non-negative.
- The initial water level must be between zero and the tank's maximum capacity.
- Excess water is discarded when the tank overflows.
- If the requested outflow exceeds the available water, the shortage is recorded and the tank becomes empty.
- The target threshold must be between zero and the tank's maximum capacity.

## 2. Algorithm

1. Start the program.
2. Input the tank's initial water level, maximum capacity, target threshold, and number of days.
3. Validate the input values.
4. Initialize overflow and shortage counters.
5. For each day:
   - Read the inflow and outflow quantities.
   - Calculate the water level before applying the tank capacity limit.
   - If the water level exceeds the maximum capacity, record the overflow and set the level to the maximum capacity.
   - If the water level becomes negative, record the shortage and set the level to zero.
   - Check whether the target threshold has been reached for the first time.
   - Display the updated water level.
6. After processing all days, display the final water level, total overflow, total shortage, and first threshold-reaching interval.
7. Stop the program.

## 3. Flowchart 
```mermaid
    A([Start]) --> B[Enter tank details]
    B --> C[Enter daily inflow and outflow]
    C --> D[Calculate new water level]
    D --> E{Level exceeds capacity?}
    E -->|Yes| F[Record overflow and set level to capacity]
    E -->|No| G{Level below zero?}
    F --> H[Check target threshold]
    G -->|Yes| I[Record shortage and set level to zero]
    G -->|No| H
    I --> H
    H --> J{More days?}
    J -->|Yes| C
    J -->|No| K[Display simulation summary]
    K --> L([Stop])
```
## 5. Sample Input


Enter tank capacity (litres): 1000
Enter initial water level (litres): 500
Enter target water level (litres): 800
Enter number of days: 4

Day 1
Enter inflow (litres): 300
Enter outflow (litres): 100

Day 2
Enter inflow (litres): 400
Enter outflow (litres): 100

Day 3
Enter inflow (litres): 100
Enter outflow (litres): 150

Day 4
Enter inflow (litres): 50
Enter outflow (litres): 100


## 6. Sample Output


===== WATER TANK SIMULATION =====

Day 1
Water level after Day 1: 700.00 litres

Day 2
Overflow detected: 0.00 litres
Water level after Day 2: 1000.00 litres

Day 3
Water level after Day 3: 950.00 litres

Day 4
Water level after Day 4: 900.00 litres

===== SIMULATION SUMMARY =====
Final water level: 900.00 litres
Total overflow: 0.00 litres
Total shortage: 0.00 litres
First threshold reached on Day: 2
Simulation completed.




