from datetime import datetime


def time_to_minutes(time_text):
    """Convert HH:MM time into minutes after midnight."""
    parsed_time = datetime.strptime(time_text, "%H:%M")
    return parsed_time.hour * 60 + parsed_time.minute


def intervals_overlap(start1, end1, start2, end2):
    """Return True if two time intervals overlap."""
    return start1 < end2 and start2 < end1


def parse_schedule(schedule_string):
    """
    Expected format:
    Course,Day,StartTime,EndTime,Room
    Example:
    Mathematics,Monday,09:00,10:00,R101
    """
    parts = [part.strip() for part in schedule_string.split(",")]

    if len(parts) != 5:
        raise ValueError("Schedule must contain five comma-separated fields.")

    course, day, start, end, room = parts

    start_minutes = time_to_minutes(start)
    end_minutes = time_to_minutes(end)

    if start_minutes >= end_minutes:
        raise ValueError("Start time must be earlier than end time.")

    return (
        course,
        day.title(),
        start,
        end,
        room.upper()
    )


def validate_timetable(existing, proposed, unavailable_rooms):
    conflicts = []

    for index, current in enumerate(proposed):
        course, day, start, end, room = current

        try:
            start_minutes = time_to_minutes(start)
            end_minutes = time_to_minutes(end)

            if start_minutes >= end_minutes:
                conflicts.append(
                    f"{course}: Start time must be earlier than end time."
                )
                continue

        except ValueError:
            conflicts.append(
                f"{course}: Invalid time format. Use HH:MM."
            )
            continue

        # Check room unavailability.
        for unavailable in unavailable_rooms:
            unavailable_room, unavailable_day, unavailable_start, unavailable_end = unavailable

            if room == unavailable_room and day == unavailable_day:
                u_start = time_to_minutes(unavailable_start)
                u_end = time_to_minutes(unavailable_end)

                if intervals_overlap(
                    start_minutes,
                    end_minutes,
                    u_start,
                    u_end
                ):
                    conflicts.append(
                        f"{course}: Room {room} is unavailable "
                        f"on {day} from {unavailable_start} "
                        f"to {unavailable_end}."
                    )

        # Check against existing courses and earlier proposed courses.
        all_other_classes = existing + proposed[:index]

        for other in all_other_classes:
            other_course, other_day, other_start, other_end, other_room = other

            if course == other_course and day == other_day:
                # Avoid treating a course as a conflict with itself.
                continue

            if day != other_day:
                continue

            other_start_minutes = time_to_minutes(other_start)
            other_end_minutes = time_to_minutes(other_end)

            if intervals_overlap(
                start_minutes,
                end_minutes,
                other_start_minutes,
                other_end_minutes
            ):
                if room == other_room:
                    conflicts.append(
                        f"{course}: Room conflict with {other_course} "
                        f"in room {room} on {day}."
                    )
                else:
                    conflicts.append(
                        f"{course}: Time conflict with {other_course} "
                        f"on {day}."
                    )

    return conflicts


def main():
    print("STUDENT TIMETABLE CONFLICT DETECTION")

    existing = []
    proposed = []
    unavailable_rooms = []

    existing_count = int(
        input("Enter number of existing classes: ")
    )

    for i in range(existing_count):
        schedule = input(
            f"Enter existing schedule {i + 1} "
            "(Course,Day,Start,End,Room): "
        )

        try:
            existing.append(parse_schedule(schedule))
        except ValueError as error:
            print("Invalid existing schedule:", error)
            return

    unavailable_count = int(
        input("Enter number of room unavailability periods: ")
    )

    for i in range(unavailable_count):
        print(f"Unavailability period {i + 1}")
        room = input("Room: ").strip().upper()
        day = input("Day: ").strip().title()
        start = input("Unavailable start time (HH:MM): ").strip()
        end = input("Unavailable end time (HH:MM): ").strip()

        try:
            start_minutes = time_to_minutes(start)
            end_minutes = time_to_minutes(end)

            if start_minutes >= end_minutes:
                print("Invalid unavailability interval.")
                return

        except ValueError:
            print("Invalid time format.")
            return

        unavailable_rooms.append((room, day, start, end))

    proposed_count = int(
        input("Enter number of proposed classes: ")
    )

    for i in range(proposed_count):
        schedule = input(
            f"Enter proposed schedule {i + 1} "
            "(Course,Day,Start,End,Room): "
        )

        try:
            proposed.append(parse_schedule(schedule))
        except ValueError as error:
            print("Invalid proposed schedule:", error)
            return

    print("\n--- PROPOSED TIMETABLE ---")

    for course in proposed:
        print(course)

    conflicts = validate_timetable(
        existing,
        proposed,
        unavailable_rooms
    )

    print("\n--- VALIDATION RESULTS ---")

    if conflicts:
        print("Timetable validation failed.")

        for conflict in conflicts:
            print("- " + conflict)
    else:
        print("Timetable is valid.")
        print("No time conflicts or room availability issues detected.")


if __name__ == "__main__":
    main()
        
