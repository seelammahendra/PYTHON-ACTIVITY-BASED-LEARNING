# ATM Transaction Sequence Simulation Using Python

## 1. Problem Statement

The ATM Transaction Sequence Simulation is a Python program that simulates basic ATM operations by processing a sequence of deposits and withdrawals.

The program starts with an initial account balance and processes each transaction entered by the user. It validates the transaction amount, checks the available balance, and enforces a maximum withdrawal limit.

The program must perform the following operations:

1. Accept the initial account balance.
2. Allow the user to enter a sequence of deposit and withdrawal transactions.
3. **Deposit:** Add the deposit amount to the current balance if the amount is valid.
4. **Withdrawal:** Deduct the withdrawal amount only if it is valid, does not exceed the withdrawal limit, and does not exceed the available balance.
5. **Reject invalid transactions:** Reject zero or negative amounts, withdrawals exceeding the limit, and withdrawals exceeding the available balance.
6. Maintain the account balance after every successful transaction.
7. Display a transaction summary containing the total number of transactions, successful transactions, rejected transactions, total deposits, total withdrawals, and final account balance.

The program continues processing transactions until the user chooses to exit.

### Assumptions

- The initial balance must be non-negative.
- The maximum withdrawal limit per transaction is ₹10,000.
- Deposits must be positive amounts.
- Withdrawals must be positive amounts.
- A withdrawal is permitted only when the amount is within the withdrawal limit and sufficient funds are available.
- Rejected transactions do not change the account balance.

---

## 2. Algorithm

**Step 1:** Start the program.

**Step 2:** Read the initial account balance and validate that it is non-negative.

**Step 3:** Initialize the following variables:
- `balance` = initial balance
- `total_deposits` = 0
- `total_withdrawals` = 0
- `successful_transactions` = 0
- `rejected_transactions` = 0
- `total_transactions` = 0

**Step 4:** Display the ATM menu:
- Option 1: Deposit
- Option 2: Withdraw
- Option 3: Display balance
- Option 4: Exit and display summary

**Step 5:** Read the user's choice.

**Step 6:** If the user selects Deposit:
- Read the deposit amount.
- If the amount is positive, add it to the balance and update the total deposits and successful transaction count.
- Otherwise, reject the transaction and update the rejected transaction count.

**Step 7:** If the user selects Withdraw:
- Read the withdrawal amount.
- If the amount is not positive, reject the transaction.
- Otherwise, check whether the amount exceeds ₹10,000.
- If it exceeds the limit, reject the transaction.
- Otherwise, check whether sufficient balance is available.
- If sufficient funds are available, deduct the amount and update the total withdrawals and successful transaction count.
- Otherwise, reject the transaction.

**Step 8:** If the user selects Display Balance, display the current balance.

**Step 9:** If the user selects Exit, display the transaction summary and terminate the program.

**Step 10:** If the user enters an invalid menu option, display an error message and return to the menu.

**Step 11:** Repeat Steps 5–10 until the user exits.

**Step 12:** Stop the program.

## 3. Flowchart 
```mermaid
    A([Start]) --> B[Enter Initial Balance]
    B --> C[Display ATM Menu]
    C --> D{Select Operation}

    D -->|Deposit| E[Validate Amount]
    E --> F{Valid Amount?}
    F -->|Yes| G[Add to Balance]
    F -->|No| H[Reject Transaction]

    D -->|Withdraw| I[Check Amount, Limit and Balance]
    I --> J{Valid Withdrawal?}
    J -->|Yes| K[Deduct from Balance]
    J -->|No| H

    G --> C
    K --> C
    H --> C

    D -->|Check Balance| L[Display Balance]
    L --> C

    D -->|Exit| M[Display Transaction Summary]
    M --> N([Stop])
```
## 5. Sample Input

The following example demonstrates successful deposits, successful withdrawals, an invalid deposit, a withdrawal exceeding the limit, and a withdrawal with insufficient funds
Enter initial balance (Rs.): 5000

===== ATM MENU =====
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Enter your choice (1-4): 1
Enter deposit amount (Rs.): 2000

Enter your choice (1-4): 2
Enter withdrawal amount (Rs.): 1500

Enter your choice (1-4): 1
Enter deposit amount (Rs.): -500

Enter your choice (1-4): 2
Enter withdrawal amount (Rs.): 12000

Enter your choice (1-4): 2
Enter withdrawal amount (Rs.): 7000

Enter your choice (1-4): 3

Enter your choice (1-4): 4


## 6. Sample Output


Enter initial balance (Rs.): 5000

===== ATM MENU =====
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Enter your choice (1-4): 1
Enter deposit amount (Rs.): 2000
Deposit successful!
Current balance: Rs. 7000.00

Enter your choice (1-4): 2
Enter withdrawal amount (Rs.): 1500
Withdrawal successful!
Current balance: Rs. 5500.00

Enter your choice (1-4): 1
Enter deposit amount (Rs.): -500
Invalid deposit amount! Transaction rejected.

Enter your choice (1-4): 2
Enter withdrawal amount (Rs.): 12000
Withdrawal limit exceeded! Transaction rejected.
Maximum limit: Rs. 10000.00

Enter your choice (1-4): 2
Enter withdrawal amount (Rs.): 7000
Insufficient balance! Transaction rejected.

Enter your choice (1-4): 3
Current balance: Rs. 5500.00

Enter your choice (1-4): 4

===== TRANSACTION SUMMARY =====
Total transactions     : 5
Successful transactions: 2
Rejected transactions  : 3
Total deposits         : Rs. 2000.00
Total withdrawals      : Rs. 1500.00
Final balance          : Rs. 5500.00

Thank you for using the ATM!


