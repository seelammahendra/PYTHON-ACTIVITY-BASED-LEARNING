# Smart Parking Fee Management Using Python

## 1. Problem Statement

Smart Parking Fee Management is a Python program designed to calculate parking charges based on vehicle category, entry time, exit time, overnight parking, daily fee limits, and penalty conditions.

The program accepts parking details from the user, validates the time inputs, calculates the parking duration, and determines the total parking fee according to predefined rules.

The program performs the following operations:

1. Accept the vehicle category, entry date and time, and exit date and time.
2. Validate the date and time inputs.
3. Calculate the total parking duration.
4. Apply different hourly rates for cars, bikes, and trucks.
5. Identify overnight parking and apply the relevant charges.
6. Enforce a maximum daily parking fee.
7. Apply penalties for invalid parking conditions, such as parking beyond a specified maximum duration.
8. Display the parking duration, base fee, penalties, and final amount payable.

### Assumptions

The following rates and rules are used for this simulation. They can be changed according to actual parking policies.

| Vehicle category | Hourly rate |
|---|---:|
| Bike | ₹20 |
| Car | ₹50 |
| Truck | ₹100 |

Additional rules:

- **Minimum charge:** One hour's fee, even for shorter stays.
- **Partial hours:** Any additional fraction of an hour is charged as a full hour.
- **Overnight parking:** An additional ₹100 is charged for each midnight crossed.
- **Daily fee limit:** The hourly parking charge cannot exceed ₹500 per calendar day.
- **Penalty:** A ₹200 penalty applies if the total parking duration exceeds 72 hours.
- **Time validation:** The exit date and time must be later than the entry date and time.
- **Vehicle validation:** Only bikes, cars, and trucks are accepted.

---

## 2. Algorithm

1. **Start** the program.
2. Define hourly rates for bikes, cars, and trucks.
3. Define the daily fee limit, overnight fee, and penalty amount.
4. Accept the vehicle category, entry date and time, and exit date and time.
5. Validate the vehicle category and date/time formats.
6. Check whether the exit time is later than the entry time. If not, display an error and stop.
7. Calculate the total parking duration in hours.
8. Round up partial hours to the next whole hour.
9. Calculate the hourly parking charge using the vehicle category.
10. Apply the daily fee limit.
11. Count the midnight boundaries crossed and calculate the overnight fee.
12. If the parking duration exceeds 72 hours, add the penalty.
13. Calculate the final fee by adding the capped parking charge, overnight fees, and applicable penalty.
14. Display the parking duration, parking charge, overnight fee, penalty, and total amount payable.
15. **Stop** the program.

## 3. Flowchart

```mermaid 

    A([Start]) --> B[/Enter vehicle and entry/exit times/]
    B --> C{Inputs valid?}
    C -->|No| D[/Display error/]
    D --> Z([Stop])
    C -->|Yes| E[Calculate parking duration]
    E --> F[Calculate hourly charge]
    F --> G[Apply daily fee limit]
    G --> H[Calculate overnight fee]
    H --> I{Duration exceeds 72 hours?}
    I -->|Yes| J[Add penalty]
    I -->|No| K[Calculate final fee]
    J --> K
    K --> L[/Display parking bill/]
    L --> Z
```



## 5. Sample Input


Enter vehicle type (Bike/Car/Truck): Car
Enter entry date and time (YYYY-MM-DD HH:MM): 2026-10-29 22:30
Enter exit date and time (YYYY-MM-DD HH:MM): 2026-10-30 02:15


## 6. Sample Output


======= SMART PARKING BILL =======
Vehicle Type       : Car
Parking Duration   : 3.75 hours
Billable Hours     : 4
Hourly Rate        : Rs. 50
Parking Charge     : Rs. 200.00
Overnight Fee      : Rs. 100.00
Penalty             : Rs. 0.00
----------------------------------
Total Amount       : Rs. 300.00
==================================


### Calculation

- **Parking duration:** 3 hours 45 minutes = 3.75 hours.
- **Billable hours:** 4 hours.
- **Hourly parking charge:** 4 × ₹50 = ₹200.
- **Overnight fee:** One midnight crossed × ₹100 = ₹100.
- **Penalty:** ₹0 because the duration does not exceed 72 hours.
- **Total fee:** ₹200 + ₹100 + ₹0 = **₹300**.




