import math


def calculate_volumetric_weight(length, width, height):
    return (length * width * height) / 5000


def calculate_billable_weight(actual_weight, volumetric_weight):
    return max(actual_weight, volumetric_weight)


def calculate_charge(weight, zone, surcharge, handling_fee):
    zone_rates = {
        "local": 40,
        "regional": 70,
        "national": 100
    }

    base_charge = weight * zone_rates[zone]
    urgency_charge = base_charge * surcharge

    total_charge = base_charge + urgency_charge + handling_fee

    return base_charge, urgency_charge, total_charge


def main():
    print("COURIER CHARGE OPTIMIZATION")

    actual_weight = float(input("Enter parcel weight (kg): "))
    length = float(input("Enter length (cm): "))
    width = float(input("Enter width (cm): "))
    height = float(input("Enter height (cm): "))

    zone = input(
        "Enter distance zone (Local/Regional/National): "
    ).strip().lower()

    urgency = input(
        "Enter required urgency (Standard/Express/Priority): "
    ).strip().lower()

    fragile = input(
        "Does the parcel contain fragile items? (yes/no): "
    ).strip().lower()

    prohibited = input(
        "Does the parcel contain prohibited items? (yes/no): "
    ).strip().lower()

    if (
        actual_weight <= 0
        or length <= 0
        or width <= 0
        or height <= 0
    ):
        print("Invalid parcel weight or dimensions.")
        return

    if zone not in ["local", "regional", "national"]:
        print("Invalid distance zone.")
        return

    if urgency not in ["standard", "express", "priority"]:
        print("Invalid urgency selection.")
        return

    if fragile not in ["yes", "no"] or prohibited not in ["yes", "no"]:
        print("Please enter yes or no for parcel restrictions.")
        return

    volumetric_weight = calculate_volumetric_weight(
        length, width, height
    )

    billable_weight = calculate_billable_weight(
        actual_weight, volumetric_weight
    )

    print(f"\nVolumetric Weight: {volumetric_weight:.2f} kg")
    print(f"Billable Weight: {billable_weight:.2f} kg")

    services = {
        "Standard": {
            "max_weight": 20,
            "surcharge": 0.00,
            "supports_fragile": False
        },
        "Express": {
            "max_weight": 15,
            "surcharge": 0.25,
            "supports_fragile": True
        },
        "Priority": {
            "max_weight": 10,
            "surcharge": 0.50,
            "supports_fragile": True
        }
    }

    handling_fee = 30
    max_dimension = 100

    eligible_services = []

    print("\n--- COURIER SERVICE COMPARISON ---")

    for service_name, details in services.items():
        reasons = []

        if billable_weight > details["max_weight"]:
            reasons.append("Exceeds maximum weight")

        if max(length, width, height) > max_dimension:
            reasons.append("Exceeds maximum dimension")

        if prohibited == "yes":
            reasons.append("Prohibited contents")

        if fragile == "yes" and not details["supports_fragile"]:
            reasons.append("Fragile-item handling unavailable")

        if urgency == "priority" and service_name != "Priority":
            reasons.append("Does not meet priority urgency")

        elif urgency == "express" and service_name == "Standard":
            reasons.append("Does not meet express urgency")

        if reasons:
            print(f"\n{service_name}: Ineligible")
            for reason in reasons:
                print(f"  - {reason}")
            continue

        base, urgency_fee, total = calculate_charge(
            billable_weight,
            zone,
            details["surcharge"],
            handling_fee
        )

        print(f"\nService: {service_name}")
        print(f"Base Charge: Rs. {base:.2f}")
        print(f"Urgency Surcharge: Rs. {urgency_fee:.2f}")
        print(f"Handling Fee: Rs. {handling_fee:.2f}")
        print(f"Total Charge: Rs. {total:.2f}")
        print("Eligibility: Eligible")

        eligible_services.append({
            "name": service_name,
            "total": total
        })

    print("\n--- RECOMMENDATION ---")

    if not eligible_services:
        print("No courier service satisfies all requirements.")
    else:
        best_service = min(
            eligible_services,
            key=lambda service: service["total"]
        )

        print(f"Selected Service: {best_service['name']}")
        print(f"Minimum Charge: Rs. {best_service['total']:.2f}")


if __name__ == "__main__":
    main()
