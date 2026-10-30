def process_examination():
    print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")

    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Student name cannot be empty.")
        return

    number_of_subjects = int(input("Enter number of subjects: "))

    if number_of_subjects <= 0:
        print("Number of subjects must be positive.")
        return

    max_marks = 100
    pass_marks = 35
    grace_limit = 5
    grace_used = 0

    subject_results = []

    for i in range(number_of_subjects):
        print(f"\n--- Subject {i + 1} ---")

        subject_name = input("Enter subject name: ").strip()
        marks = float(input("Enter marks obtained (0-100): "))

        if not subject_name:
            print("Subject name cannot be empty.")
            return

        if marks < 0 or marks > max_marks:
            print("Invalid marks. Marks must be between 0 and 100.")
            return

        grace_awarded = 0
        final_marks = marks

        if marks < pass_marks:
            marks_needed = pass_marks - marks
            grace_remaining = grace_limit - grace_used

            if (
                marks_needed <= 5
                and marks_needed <= grace_remaining
                and marks + marks_needed <= max_marks
            ):
                grace_awarded = marks_needed
                final_marks = marks + grace_awarded
                grace_used += grace_awarded

        passed = final_marks >= pass_marks

        subject_results.append({
            "name": subject_name,
            "original_marks": marks,
            "grace": grace_awarded,
            "final_marks": final_marks,
            "passed": passed
        })

    total_marks = sum(
        subject["final_marks"] for subject in subject_results
    )
    maximum_total = number_of_subjects * max_marks
    percentage = (total_marks / maximum_total) * 100

    passed_all_subjects = all(
        subject["passed"] for subject in subject_results
    )

    if not passed_all_subjects:
        classification = "Fail"
    elif percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass Class"

    print("\n--- SUBJECT-WISE RESULT ---")

    for subject in subject_results:
        status = "Pass" if subject["passed"] else "Fail"

        print(f"\nSubject: {subject['name']}")
        print(f"Original Marks: {subject['original_marks']:.2f}")
        print(f"Grace Marks: {subject['grace']:.2f}")
        print(f"Final Marks: {subject['final_marks']:.2f}")
        print(f"Status: {status}")

    print("\n--- FINAL RESULT ---")
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total_marks:.2f}/{maximum_total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grace Marks Used: {grace_used}/{grace_limit}")
    print(f"Classification: {classification}")


if __name__ == "__main__":
    process_examination()
