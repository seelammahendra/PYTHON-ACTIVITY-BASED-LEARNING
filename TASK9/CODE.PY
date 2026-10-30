def analyze_travel_budget():
    print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

    base_currency = input(
        "Enter base currency code (e.g., INR): "
    ).strip().upper()

    budget = float(input("Enter planned travel budget: "))
    number_of_expenses = int(
        input("Enter number of expenses: ")
    )

    if not base_currency or budget < 0 or number_of_expenses <= 0:
        print("Invalid budget, currency, or number of expenses.")
        return

    total_expenses = 0.0
    category_totals = {}
    expense_details = []

    for i in range(number_of_expenses):
        print(f"\n--- Expense {i + 1} ---")

        description = input("Enter expense description: ").strip()
        category = input("Enter expense category: ").strip().title()
        amount = float(input("Enter expense amount: "))
        currency = input("Enter currency code: ").strip().upper()
        exchange_rate = float(
            input(
                f"Enter exchange rate (1 {currency} in "
                f"{base_currency}): "
            )
        )
        fee_percentage = float(
            input("Enter conversion fee percentage: ")
        )

        if (
            not description
            or not category
            or not currency
            or amount < 0
            or exchange_rate <= 0
            or fee_percentage < 0
            or fee_percentage > 100
        ):
            print("Invalid expense details. Please try again.")
            return

        converted_amount = amount * exchange_rate
        conversion_fee = converted_amount * fee_percentage / 100
        total_cost = converted_amount + conversion_fee

        total_expenses += total_cost

        category_totals[category] = (
            category_totals.get(category, 0) + total_cost
        )

        expense_details.append({
            "description": description,
            "category": category,
            "original_amount": amount,
            "currency": currency,
            "converted_amount": converted_amount,
            "conversion_fee": conversion_fee,
            "total_cost": total_cost
        })

    print("\n--- EXPENSE DETAILS ---")

    for expense in expense_details:
        print(f"\nDescription: {expense['description']}")
        print(f"Category: {expense['category']}")
        print(
            f"Original Amount: {expense['original_amount']:.2f} "
            f"{expense['currency']}"
        )
        print(
            f"Converted Amount: {expense['converted_amount']:.2f} "
            f"{base_currency}"
        )
        print(
            f"Conversion Fee: {expense['conversion_fee']:.2f} "
            f"{base_currency}"
        )
        print(
            f"Total Cost: {expense['total_cost']:.2f} "
            f"{base_currency}"
        )

    print("\n--- CATEGORY TOTALS ---")

    for category, total in category_totals.items():
        print(f"{category}: {total:.2f} {base_currency}")

    largest_category = max(category_totals, key=category_totals.get)

    print("\n--- TRAVEL BUDGET SUMMARY ---")
    print(f"Planned Budget: {budget:.2f} {base_currency}")
    print(f"Total Expenses: {total_expenses:.2f} {base_currency}")
    print(
        f"Largest Expense Category: {largest_category} "
        f"({category_totals[largest_category]:.2f} {base_currency})"
    )

    balance = budget - total_expenses

    if balance > 0:
        print(f"Remaining Budget: {balance:.2f} {base_currency}")
        print("Status: Within Budget")
    elif balance < 0:
        print(f"Excess Spending: {-balance:.2f} {base_currency}")
        print("Status: Over Budget")
    else:
        print("Status: Budget Fully Utilized")


if __name__ == "__main__":
    analyze_travel_budget()
