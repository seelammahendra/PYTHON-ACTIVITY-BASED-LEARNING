def calculate_aggregate(marks):
    """Calculate aggregate percentage across all subjects."""
    return sum(marks.values()) / len(marks)
def check_eligibility(applicant):
    """Check all scholarship eligibility criteria."""
    reasons = []

    # Minimum subject-wise marks
    minimum_marks = {
        "Mathematics": 60,
        "Science": 60,
        "English": 50
    }

    for subject, minimum in minimum_marks.items():
        if applicant["marks"][subject] < minimum:
            reasons.append(
                f"{subject} marks below {minimum}"
            )


    if applicant["aggregate"] < 75:
        reasons.append("Aggregate below 75%")

    
    if applicant["attendance"] < 85:
        reasons.append("Attendance below 85%")

    if applicant["income"] > 300000:
        reasons.append("Annual family income exceeds Rs. 300000")

    return reasons


def rank_applicants(applicants):
    """Filter eligible applicants and rank them."""
    eligible = []
    rejected = []

    for applicant in applicants:
        reasons = check_eligibility(applicant)

        if not reasons:
            eligible.append(applicant)
        else:
            rejected.append({
                "id": applicant["id"],
                "name": applicant["name"],
                "reasons": reasons
            })


   
    eligible.sort(
        key=lambda a: (
            -a["aggregate"],
            -(a["marks"]["Mathematics"] +
              a["marks"]["Science"]),
            -a["attendance"],
            a["id"]
        )
    )

    return eligible, rejected


def main():
    print("UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM")

    try:
        number = int(input("Enter number of applicants: "))

        if number <= 0:
            print("Number of applicants must be positive.")
            return

        applicants = []
        used_ids = set()

        for i in range(number):
            print(f"\nApplicant {i + 1}")

            applicant_id = int(input("Enter applicant ID: "))

            if applicant_id <= 0 or applicant_id in used_ids:
                print("Applicant ID must be positive and unique.")
                return

            used_ids.add(applicant_id)

            name = input("Enter applicant name: ").strip()

            if not name:
                print("Applicant name cannot be empty.")
                return

            marks = {}

            for subject in ["Mathematics", "Science", "English"]:
                score = float(
                    input(f"Enter {subject} marks (0-100): ")
                )

                if not 0 <= score <= 100:
                    print("Marks must be between 0 and 100.")
                    return

                marks[subject] = score

            attendance = float(
                input("Enter attendance percentage (0-100): ")
            )

            income = float(
                input("Enter annual family income (Rs.): ")
            )

            if not 0 <= attendance <= 100 or income < 0:
                print("Invalid attendance or family income.")
                return

            aggregate = calculate_aggregate(marks)

            applicants.append({
                "id": applicant_id,
                "name": name,
                "marks": marks,
                "aggregate": aggregate,
                "attendance": attendance,
                "income": income
            })

        eligible, rejected = rank_applicants(applicants)

        
        print("\n========== SCHOLARSHIP RANKING ==========")

        if eligible:
            print(
                f"{'Rank':<6}{'ID':<8}{'Name':<15}"
                f"{'Aggregate':<13}{'Attendance':<13}"
            )
            print("-" * 55)

            for rank, applicant in enumerate(eligible, start=1):
                print(
                    f"{rank:<6}{applicant['id']:<8}"
                    f"{applicant['name']:<15}"
                    f"{applicant['aggregate']:.2f}%"
                    f"{'':<6}{applicant['attendance']:.2f}%"
                )

            print(
                f"\nTotal eligible applicants: {len(eligible)}"
            )
        else:
            print("No applicants meet all scholarship criteria.")

        
        print("\n========== INELIGIBLE APPLICANTS ==========")

        if rejected:
            for applicant in rejected:
                print(
                    f"\n{applicant['name']} "
                    f"(ID: {applicant['id']})"
                )

                for reason in applicant["reasons"]:
                    print(f"- {reason}")
        else:
            print("No ineligible applicants.")

    except ValueError:
        print("Invalid input. Enter numeric values where required.")


if __name__ == "__main__":
    main()
