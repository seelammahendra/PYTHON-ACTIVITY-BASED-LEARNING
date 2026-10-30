products = []
n = int(input("Enter number of products: "))
for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")

    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    actual_closing = int(input("Enter actual closing stock: "))
    minimum_stock = int(input("Enter minimum stock level: "))

   
    if min(opening, incoming, dispatched,
           actual_closing, minimum_stock) < 0:
        print("Invalid stock quantity. Enter non-negative values.")
        continue

    if dispatched > opening + incoming:
        print("Invalid transaction: dispatched quantity exceeds available stock.")
        continue
   
    expected_closing = opening + incoming - dispatched

    
    discrepancy = actual_closing - expected_closing

      if discrepancy == 0:
   status = "Matched"
    elif discrepancy < 0:
        status = "Stock Shortage"
    else:
        status = "Stock Surplus"

  
    replenishment = max(0, minimum_stock - actual_closing)
  products.append({
        "name": name,
        "opening": opening,
        "incoming": incoming,
        "dispatched": dispatched,
        "expected": expected_closing,
        "actual": actual_closing,
        "discrepancy": discrepancy,
        "status": status,
        "replenishment": replenishment
    })
print("\n========== INVENTORY RECONCILIATION REPORT ==========")
for p in products:
    print(f"\nProduct Name       : {p['name']}")
    print(f"Opening Stock      : {p['opening']}")
    print(f"Incoming Quantity  : {p['incoming']}")
    print(f"Dispatched Quantity: {p['dispatched']}")
    print(f"Expected Closing   : {p['expected']}")
    print(f"Actual Closing     : {p['actual']}")
    print(f"Discrepancy        : {p['discrepancy']}")
    print(f"Stock Status       : {p['status']}")
    print(f"Replenishment      : {p['replenishment']}")
print("\n========== FINAL SUMMARY ==========")
print("Total products processed:", len(products))
print("Products with matching stock:",
      sum(p["status"] == "Matched" for p in products))
print("Products with shortages:",
      sum(p["status"] == "Stock Shortage" for p in products))
print("Products with surpluses:",
      sum(p["status"] == "Stock Surplus" for p in products))
print("Total replenishment required:",
      sum(p["replenishment"] for p in products))

print("\nInventory reconciliation completed.")
