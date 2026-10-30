MAX_WITHDRAWAL_LIMIT = 10000
while True:
    try:
        balance = float(input("Enter initial balance (Rs.): "))

        if balance >= 0:
            break

        print("Invalid balance! Balance cannot be negative.")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")


total_deposits = 0.0
total_withdrawals = 0.0
total_transactions = 0
successful_transactions = 0
rejected_transactions = 0

print("\n===== ATM MENU =====")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

while True:
    try:
        choice = int(input("\nEnter your choice (1-4): "))

    except ValueError:
        print("Invalid choice! Enter a number from 1 to 4.")
        continue

   
    if choice == 1:
        try:
            amount = float(input("Enter deposit amount (Rs.): "))
        except ValueError:
            print("Invalid amount! Transaction rejected.")
            total_transactions += 1
            rejected_transactions += 1
            continue

        total_transactions += 1

        if amount <= 0:
            print("Invalid deposit amount! Transaction rejected.")
            rejected_transactions += 1

        else:
            balance += amount
            total_deposits += amount
            successful_transactions += 1

            print("Deposit successful!")
            print(f"Current balance: Rs. {balance:.2f}")

    
    elif choice == 2:
        try:
            amount = float(input("Enter withdrawal amount (Rs.): "))
        except ValueError:
            print("Invalid amount! Transaction rejected.")
            total_transactions += 1
            rejected_transactions += 1
            continue

        total_transactions += 1

        if amount <= 0:
            print("Invalid withdrawal amount! Transaction rejected.")
            rejected_transactions += 1

        elif amount > MAX_WITHDRAWAL_LIMIT:
            print("Withdrawal limit exceeded! Transaction rejected.")
            print(f"Maximum limit: Rs. {MAX_WITHDRAWAL_LIMIT:.2f}")
            rejected_transactions += 1

        elif amount > balance:
            print("Insufficient balance! Transaction rejected.")
            rejected_transactions += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful_transactions += 1

            print("Withdrawal successful!")
            print(f"Current balance: Rs. {balance:.2f}")

   
    elif choice == 3:
        print(f"Current balance: Rs. {balance:.2f}")

   
    elif choice == 4:
        print("\n===== TRANSACTION SUMMARY =====")
        print(f"Total transactions     : {total_transactions}")
        print(f"Successful transactions: {successful_transactions}")
        print(f"Rejected transactions  : {rejected_transactions}")
        print(f"Total deposits         : Rs. {total_deposits:.2f}")
        print(f"Total withdrawals      : Rs. {total_withdrawals:.2f}")
        print(f"Final balance          : Rs. {balance:.2f}")

        print("\nThank you for using the ATM!")
        break

    
    else:
        print("Invalid choice! Please select an option from 1 to 4.")
