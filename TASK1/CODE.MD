# Progressive Electricity Billing

## 1. Problem Statement

Develop a Python program to calculate household electricity bills using progressive consumption slabs, fixed charges, surcharges, and rebates. The program should process electricity consumption for several months, calculate each month's bill, compare bills across months, and identify unusual increases in electricity costs.

The program should:
- Accept monthly electricity consumption in kilowatt-hours (kWh).
- Calculate energy charges using progressive consumption slabs.
- Add fixed monthly charges.
- Apply a surcharge when consumption exceeds a specified limit.
- Apply a rebate when consumption is below a specified limit.
- Calculate the final bill for each month.
- Compare monthly bills and calculate percentage changes.
- Identify unusual increases in electricity bills.

**Assumptions for this program:**

| Electricity consumption slab | Rate per kWh |
|---|---:|
| First 100 units | ₹2.00 |
| Next 100 units (101–200) | ₹3.00 |
| Next 300 units (201–500) | ₹5.00 |
| Above 500 units | ₹7.00 |

Additional billing rules:
- Fixed monthly charge: ₹100.
- Surcharge: 10% of energy charges when consumption exceeds 500 units.
- Rebate: 5% of energy charges when consumption is below 100 units.
- An increase of more than 20% compared with the previous month's bill is considered unusual.
- The rebate and surcharge are applied to energy charges only.

*These rates and rules are illustrative and do not represent any specific electricity provider's tariff.*

## 2. Algorithm

1. Start the program.
2. Input the number of months to analyze.
3. For each month:
   - Enter the month name and electricity consumption.
   - Validate that consumption is nonnegative.
   - Calculate energy charges using progressive slabs.
   - Add the fixed monthly charge.
   - Apply the surcharge if consumption exceeds 500 units.
   - Apply the rebate if consumption is below 100 units.
   - Calculate the final bill.
   - Store the monthly consumption and bill amount.
4. Compare each month's bill with the previous month's bill.
5. Calculate the percentage increase or decrease.
6. If the bill increases by more than 20%, flag it as an unusual increase.
7. Display the monthly bill breakdown and comparison summary.
8. Stop the program.

## 3. Flowchart 
```mermaid 
    A([Start]) --> B[/Enter number of months/]
    B --> C[Initialize monthly records]
    C --> D[/Enter month and consumption/]
    D --> E{Consumption valid?}
    E -- No --> F[Display error]
    F --> Z([Stop])
    E -- Yes --> G[Calculate progressive energy charges]
    G --> H[Add fixed charge]
    H --> I{Consumption above 500?}
    I -- Yes --> J[Apply 10% surcharge]
    I -- No --> K{Consumption below 100?}
    J --> L[Calculate final bill]
    K -- Yes --> M[Apply 5% rebate]
    K -- No --> L
    M --> L
    L --> N[Store monthly bill]
    N --> O{More months?}
    O -- Yes --> D
    O -- No --> P[Compare consecutive monthly bills]
    P --> Q{Increase greater than 20%?}
    Q -- Yes --> R[Flag unusual increase]
    Q -- No --> S[Record normal change]
    R --> T[Display monthly and comparison reports]
    S --> T
    T --> Z
```



## 5. Sample Input

Enter number of months: 3

--- Month 1 ---
Enter month name: January
Enter electricity consumption (kWh): 150

--- Month 2 ---
Enter month name: February
Enter electricity consumption (kWh): 180

--- Month 3 ---
Enter month name: March
Enter electricity consumption (kWh): 300


## 6. Sample Output


PROGRESSIVE ELECTRICITY BILLING

========== MONTHLY BILL DETAILS ==========

Month: January
Consumption: 150.00 kWh
Energy Charges: Rs. 350.00
Fixed Charges: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 0.00
Final Bill: Rs. 450.00

Month: February
Consumption: 180.00 kWh
Energy Charges: Rs. 440.00
Fixed Charges: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 0.00
Final Bill: Rs. 540.00

Month: March
Consumption: 300.00 kWh
Energy Charges: Rs. 900.00
Fixed Charges: Rs. 100.00
Surcharge: Rs. 0.00
Rebate: Rs. 0.00
Final Bill: Rs. 1000.00

========== MONTHLY BILL COMPARISON ==========

January -> February
Previous Bill: Rs. 450.00
Current Bill: Rs. 540.00
Bill Increase: Rs. 90.00
Percentage Change: 20.00%
Status: No unusual increase.

February -> March
Previous Bill: Rs. 540.00
Current Bill: Rs. 1000.00
Bill Increase: Rs. 460.00
Percentage Change: 85.19%
Alert: Unusual increase in electricity bill!

========== OVERALL SUMMARY ==========
Months Analyzed: 3
Total Electricity Cost: Rs. 1990.00
Average Monthly Bill: Rs. 663.33
