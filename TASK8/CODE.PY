def calculate_basic_fare(distance):
    if distance <= 100:
        return distance * 1.50
    elif distance <= 300:
        return (100 * 1.50) + ((distance - 100) * 1.25)
    else:
        return (100 * 1.50) + (200 * 1.25) + (
            (distance - 300) * 1.00
        )


def calculate_passenger_fare(name, age, distance, class_name):
    class_multipliers = {
        "sleeper": 1.0,
        "ac 3-tier": 1.5,
        "ac 2-tier": 2.0
    }

    reservation_fee = 40

    basic_fare = calculate_basic_fare(distance)
    class_fare = basic_fare * class_multipliers[class_name]

    if age < 5:
        concession = 100
    elif age < 12:
        concession = 50
    elif age >= 60:
        concession = 30
    else:
        concession = 0

    discount = class_fare * concession / 100
    fare_after_discount = class_fare - discount

    if age < 5:
        reservation_fee = 0

    final_fare = fare_after_discount + reservation_fee

    print(f"\nPassenger: {name}")
    print(f"Age: {age}")
    print(f"Basic fare: Rs. {basic_fare:.2f}")
    print(f"Fare after class multiplier: Rs. {class_fare:.2f}")
    print(f"Age concession: {concession}%")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"Reservation fee: Rs. {reservation_fee:.2f}")
    print(f"Final fare: Rs. {final_fare:.2f}")

    cancelled = input("Is the ticket cancelled? (yes/no): ").lower()

    if cancelled == "yes":
        cancellation_penalty = final_fare * 0.25
        refund = final_fare - cancellation_penalty

        print(f"Cancellation penalty: Rs. {cancellation_penalty:.2f}")
        print(f"Refund amount: Rs. {refund:.2f}")

        return 0, refund

    else:
        print(f"Amount payable: Rs. {final_fare:.2f}")
        return final_fare, 0


def main():
    print("RAILWAY FARE AND RESERVATION CALCULATOR")

    distance = float(input("Enter journey distance (km): "))

    if distance <= 0:
        print("Distance must be greater than zero.")
        return

    print("\nAvailable Classes:")
    print("1. Sleeper")
    print("2. AC 3-Tier")
    print("3. AC 2-Tier")

    class_choice = input("Select travel class (1/2/3): ")

    class_options = {
        "1": "sleeper",
        "2": "ac 3-tier",
        "3": "ac 2-tier"
    }

    if class_choice not in class_options:
        print("Invalid travel class.")
        return

    class_name = class_options[class_choice]

    number_of_passengers = int(input("Enter number of passengers: "))

    if number_of_passengers <= 0:
        print("Number of passengers must be positive.")
        return

    total_payable = 0
    total_refund = 0

    for i in range(number_of_passengers):
        print(f"\n--- Passenger {i + 1} ---")

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))

        if age < 0:
            print("Age cannot be negative.")
            return

        payable, refund = calculate_passenger_fare(
            name, age, distance, class_name
        )

        total_payable += payable
        total_refund += refund

    print("\n--- JOURNEY SUMMARY ---")
    print(f"Distance: {distance:.2f} km")
    print(f"Travel class: {class_name.title()}")
    print(f"Total amount payable: Rs. {total_payable:.2f}")
    print(f"Total refunds: Rs. {total_refund:.2f}")


if __name__ == "__main__":
    main()
