def analyze_travel_budget():
    print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

    base_currency = input("Enter base currency code (e.g., INR): ").upper()

    budget = float(input("Enter your travel budget: "))
    number_of_expenses = int(input("Enter number of expenses: "))

    if budget < 0 or number_of_expenses < 1:
        print("Invalid budget or number of expenses.")
        return

    total_expenses = 0.0

    for i in range(number_of_expenses):
        print(f"\nExpense {i + 1}")

        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        currency = input("Enter expense currency code: ").upper()
        exchange_rate = float(
            input(f"Enter exchange rate (1 {currency} in {base_currency}): ")
        )
        fee_percentage = float(input("Enter conversion fee percentage: "))

        if amount < 0 or exchange_rate <= 0:
            print("Invalid amount or exchange rate.")
            return

        if fee_percentage < 0 or fee_percentage > 100:
            print("Conversion fee must be between 0 and 100.")
            return

        converted_amount = amount * exchange_rate
        conversion_fee = converted_amount * fee_percentage / 100
        total_cost = converted_amount + conversion_fee

        total_expenses += total_cost

        print(f"Description: {description}")
        print(f"Original amount: {amount:.2f} {currency}")
        print(f"Converted amount: {converted_amount:.2f} {base_currency}")
        print(f"Conversion fee: {conversion_fee:.2f} {base_currency}")
        print(f"Total expense: {total_cost:.2f} {base_currency}")

    print("\n--- TRAVEL BUDGET SUMMARY ---")
    print(f"Planned budget: {budget:.2f} {base_currency}")
    print(f"Total expenses: {total_expenses:.2f} {base_currency}")

    balance = budget - total_expenses

    if balance > 0:
        print(f"Remaining budget: {balance:.2f} {base_currency}")
        print("Status: Within budget")
    elif balance < 0:
        print(f"Excess spending: {-balance:.2f} {base_currency}")
        print("Status: Over budget")
    else:
        print("Status: Budget fully utilized")


analyze_travel_budget()
