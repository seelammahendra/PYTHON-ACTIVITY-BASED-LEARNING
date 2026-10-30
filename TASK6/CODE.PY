def calculate_bill(age, consultation, diagnostics, treatment):
    """Calculate subtotal, concessions, and final bill."""

    subtotal = consultation + diagnostics + treatment

  
    senior_discount = 0

    if age >= 60:
        senior_discount = subtotal * 0.10

    
    high_bill_discount = 0

    if subtotal >= 10000:
        high_bill_discount = subtotal * 0.05
 
    total_discount = min(
        senior_discount + high_bill_discount,
        subtotal * 0.15
    )

    final_bill = subtotal - total_discount

    return (
        subtotal,
        senior_discount,
        high_bill_discount,
        total_discount,
        final_bill
    )


def classify_patient(final_bill):
    """Classify the patient according to the billing policy."""

    if final_bill == 0:
        return "No Payment Due"
    elif final_bill <= 5000:
        return "Standard"
    elif final_bill <= 15000:
        return "Moderate"
    else:
        return "High-Cost"


def main():
    print("HOSPITAL BILLING AND PATIENT CLASSIFICATION")

    try:
        patient_id = input("Enter patient ID: ").strip()
        patient_name = input("Enter patient name: ").strip()
        age = int(input("Enter patient age: "))

        if not patient_id or not patient_name:
            print("Patient ID and name cannot be empty.")
            return

        if age < 0:
            print("Age cannot be negative.")
            return

        consultation = float(
            input("Enter consultation charges (Rs.): ")
        )
        diagnostics = float(
            input("Enter diagnostic charges (Rs.): ")
        )
        treatment = float(
            input("Enter treatment charges (Rs.): ")
        )

        if min(consultation, diagnostics, treatment) < 0:
            print("Charges cannot be negative.")
            return

        payment_status = input(
            "Enter payment status (Paid/Pending): "
        ).strip().lower()

        if payment_status not in ("paid", "pending"):
            print("Invalid payment status. Enter Paid or Pending.")
            return

        (
            subtotal,
            senior_discount,
            high_bill_discount,
            total_discount,
            final_bill
        ) = calculate_bill(
            age, consultation, diagnostics, treatment
        )

        classification = classify_patient(final_bill)

        print("\n========== HOSPITAL BILL ==========")
        print(f"Patient ID: {patient_id}")
        print(f"Patient Name: {patient_name}")
        print(f"Age: {age}")

        print("\n--- Charge Details ---")
        print(f"Consultation: Rs. {consultation:.2f}")
        print(f"Diagnostics: Rs. {diagnostics:.2f}")
        print(f"Treatment: Rs. {treatment:.2f}")
        print(f"Subtotal: Rs. {subtotal:.2f}")

        print("\n--- Concessions ---")
        print(f"Senior Citizen Discount: Rs. {senior_discount:.2f}")
        print(f"High-Bill Discount: Rs. {high_bill_discount:.2f}")
        print(f"Total Discount: Rs. {total_discount:.2f}")

        print("\n--- Final Summary ---")
        print(f"Final Bill: Rs. {final_bill:.2f}")
        print(f"Patient Classification: {classification}")
        print(f"Payment Status: {payment_status.title()}")

        if payment_status == "pending" and final_bill > 0:
            print(f"Amount Due: Rs. {final_bill:.2f}")
        else:
            print("Amount Due: Rs. 0.00")

    except ValueError:
        print("Invalid input. Enter numbers for age and charges.")


if __name__ == "__main__":
    main()
