from datetime import datetime
import math
RATES = {
    "bike": 20,
    "car": 50,
    "truck": 100
}

DAILY_LIMIT = 500
OVERNIGHT_FEE = 100
PENALTY = 200
MAX_HOURS = 72

try:
   
    vehicle = input("Enter vehicle type (Bike/Car/Truck): ").strip().lower()

    if vehicle not in RATES:
        raise ValueError("Invalid vehicle category!"
    time_format = "%Y-%m-%d %H:%M"

    entry_input = input("Enter entry date and time (YYYY-MM-DD HH:MM): ")
    exit_input = input("Enter exit date and time (YYYY-MM-DD HH:MM): ")

    entry = datetime.strptime(entry_input, time_format)
    exit_time = datetime.strptime(exit_input, time_format)

   
    if exit_time <= entry:
        raise ValueError("Exit time must be later than entry time!")
    duration_seconds = (exit_time - entry).total_seconds()
    duration_hours = duration_seconds / 3600
    billable_hours = max(1, math.ceil(duration_hours))

   
    hourly_charge = billable_hours * RATES[vehicle]

    
    parking_days = (exit_time.date() - entry.date()).days + 1

    parking_charge = min(hourly_charge, parking_days * DAILY_LIMIT)

    
    overnight_count = (exit_time.date() - entry.date()).days
    overnight_charge = overnight_count * OVERNIGHT_FEE
  
    penalty = PENALTY if duration_hours > MAX_HOURS else 0

    total_fee = parking_charge + overnight_charge + penalty
    print("\n======= SMART PARKING BILL =======")
    print(f"Vehicle Type       : {vehicle.title()}")
    print(f"Parking Duration   : {duration_hours:.2f} hours")
    print(f"Billable Hours     : {billable_hours}")
    print(f"Hourly Rate        : Rs. {RATES[vehicle]}")
    print(f"Parking Charge     : Rs. {parking_charge:.2f}")
    print(f"Overnight Fee      : Rs. {overnight_charge:.2f}")
    print(f"Penalty             : Rs. {penalty:.2f}")
    print("----------------------------------")
    print(f"Total Amount       : Rs. {total_fee:.2f}")
    print("==================================")

except ValueError as error:
    print("Error:", error)
