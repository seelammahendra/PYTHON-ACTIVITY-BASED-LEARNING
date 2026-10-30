def compare_vehicles(distance, vehicles):
    results = []

    for vehicle in vehicles:
        name = vehicle["name"]
        mileage = vehicle["mileage"]
        fuel_price = vehicle["fuel_price"]
        available_fuel = vehicle["available_fuel"]
        reserve_fuel = vehicle["reserve_fuel"]
       
        journey_fuel = distance / mileage

        total_fuel_required = journey_fuel + reserve_fuel
        journey_cost = journey_fuel * fuel_price

       
        feasible = available_fuel >= total_fuel_required

        results.append({
            "name": name,
            "journey_fuel": journey_fuel,
            "total_fuel_required": total_fuel_required,
            "journey_cost": journey_cost,
            "feasible": feasible
        })

    return results


def main():
    print("FUEL CONSUMPTION AND ROUTE COMPARISON")

    try:
        distance = float(input("Enter journey distance (km): "))
        number_of_vehicles = int(input("Enter number of vehicles: "))

        if distance <= 0 or number_of_vehicles <= 0:
            print("Distance and number of vehicles must be positive.")
            return

        vehicles = []

        for i in range(number_of_vehicles):
            print(f"\nEnter details for Vehicle {i + 1}")

            name = input("Vehicle name: ").strip()
            mileage = float(input("Mileage (km/litre): "))
            fuel_price = float(input("Fuel price per litre (Rs.): "))
            available_fuel = float(input("Available fuel (litres): "))
            reserve_fuel = float(input("Required reserve (litres): "))

            if (
                not name
                or mileage <= 0
                or fuel_price < 0
                or available_fuel < 0
                or reserve_fuel < 0
            ):
                print("Invalid vehicle details. Please enter valid values.")
                return

            vehicles.append({
                "name": name,
                "mileage": mileage,
                "fuel_price": fuel_price,
                "available_fuel": available_fuel,
                "reserve_fuel": reserve_fuel
            })

        results = compare_vehicles(distance, vehicles)

        print("\n--- VEHICLE COMPARISON REPORT ---")
        print(f"Journey Distance: {distance:.2f} km")

        for result in results:
            status = (
                "Feasible"
                if result["feasible"]
                else "Not Feasible"
            )

            print(f"\nVehicle: {result['name']}")
            print(
                f"Journey Fuel: "
                f"{result['journey_fuel']:.2f} litres"
            )
            print(
                f"Total Fuel Required (including reserve): "
                f"{result['total_fuel_required']:.2f} litres"
            )
            print(f"Journey Cost: Rs. {result['journey_cost']:.2f}")
            print(f"Status: {status}")

        feasible_vehicles = [
            result for result in results if result["feasible"]
        ]

        if feasible_vehicles:
            lowest_cost = min(
                feasible_vehicles,
                key=lambda vehicle: vehicle["journey_cost"]
            )

            print("\n--- BEST OPTION ---")
            print(f"Lowest-Cost Vehicle: {lowest_cost['name']}")
            print(
                f"Estimated Journey Cost: "
                f"Rs. {lowest_cost['journey_cost']:.2f}"
            )
            print("This vehicle has enough fuel, including its reserve.")
        else:
            print("\nNo vehicle has enough fuel to complete the journey")
            print("while maintaining its required reserve.")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main()
