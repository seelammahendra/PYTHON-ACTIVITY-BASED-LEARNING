# Progressive Water Tariff Analysis Using Python

## 1. Problem Statement

Develop a Python program to calculate water bills for multiple households using progressive consumption slabs, fixed service fees, and penalties. The program should compare household water consumption, calculate the total bill for each household, and identify households with excessive water usage.

### Requirements

- Accept the number of households and each household's water consumption in kilolitres (kL).
- Calculate water charges using progressive tariff slabs.
- Add a fixed service fee to each household's bill.
- Apply a penalty when consumption exceeds the specified limit.
- Display each household's consumption, slab charges, penalty, and total bill.
- Compare consumption across households.
- Identify households with excessive water usage and determine which household consumes the most water.

### Example tariff rules

For this program, assume the following rates:

| Water consumption slab | Rate per kL |
|---|---:|
| First 10 kL | ₹5 |
| Next 10 kL (10–20 kL) | ₹8 |
| Above 20 kL | ₹12 |

Additional rules:
- **Fixed service fee:** ₹50 per household.
- **Excessive usage limit:** 25 kL.
- **Excess usage penalty:** ₹100 if consumption exceeds 25 kL.
- The penalty is applied once per household per billing period.

These are example rates for an academic program, not an actual utility tariff.

## 2. Algorithm

1. Start.
2. Define the water tariff slabs, fixed fee, excessive usage limit, and penalty.
3. Input the number of households.
4. For each household:
   - Enter the household name or ID.
   - Enter water consumption in kL.
   - Calculate the charge for the first 10 kL.
   - Calculate the charge for the next 10 kL, if applicable.
   - Calculate the charge for consumption above 20 kL, if applicable.
   - Add the fixed service fee.
   - Apply the penalty if consumption exceeds 25 kL.
   - Calculate the final bill.
5. Store the results for all households.
6. Compare household consumption and identify excessive users.
7. Find the household with the highest consumption.
8. Display the complete billing report and consumption comparison.
9. Stop.

## 3. Flowchart

```mermaid 

    A([Start]) --> B[Define tariff slabs and fees]
    B --> C[/Enter number of households/]
    C --> D[/Enter household name and consumption/]
    D --> E[Calculate progressive water charges]
    E --> F[Add fixed service fee]
    F --> G{Consumption above 25 kL?}
    G -- Yes --> H[Add penalty of Rs. 100]
    G -- No --> I[No penalty]
    H --> J[Calculate total bill]
    I --> J
    J --> K[Store household details]
    K --> L{More households?}
    L -- Yes --> D
    L -- No --> M[Compare consumption]
    M --> N[Identify excessive users and highest consumer]
    N --> O[/Display billing report/]
    O --> P([Stop])
```
## 5. Sample Input


Enter number of households: 3

Household 1
Enter household name or ID: H101
Enter water consumption (kL): 8

Household 2
Enter household name or ID: H102
Enter water consumption (kL): 18

Household 3
Enter household name or ID: H103
Enter water consumption (kL): 30


## 6. Sample Output


========== WATER BILL REPORT ==========

Household: H101
Consumption: 8.00 kL
Water Charges: Rs. 40.00
Fixed Fee: Rs. 50.00
Penalty: Rs. 0.00
Total Bill: Rs. 90.00

Household: H102
Consumption: 18.00 kL
Water Charges: Rs. 114.00
Fixed Fee: Rs. 50.00
Penalty: Rs. 0.00
Total Bill: Rs. 164.00

Household: H103
Consumption: 30.00 kL
Water Charges: Rs. 260.00
Fixed Fee: Rs. 50.00
Penalty: Rs. 100.00
Total Bill: Rs. 410.00

========== CONSUMPTION ANALYSIS ==========
Average Consumption: 18.67 kL
Highest Consumer: H103 (30.00 kL)

Excessive Water Users:
- H103: 30.00 kL

Households Ranked by Consumption:
1. H103 - 30.00 kL
2. H102 - 18.00 kL
3. H101 - 8.00 kL


