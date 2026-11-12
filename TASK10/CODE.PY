teams = {}
n = int(input("Enter number of teams: "))

for i in range(n):
    name = input("Enter team name: ")
    teams[name] = {
        "points": 0,
        "goals_scored": 0,
        "goals_conceded": 0
    }

m = int(input("Enter number of matches: "))

for i in range(m):
    print("\nMatch", i + 1)

    team1 = input("Enter first team: ")
    team2 = input("Enter second team: ")

    score1 = int(input("Enter first team score: "))
    score2 = int(input("Enter second team score: "))

    teams[team1]["goals_scored"] += score1
    teams[team1]["goals_conceded"] += score2

    teams[team2]["goals_scored"] += score2
    teams[team2]["goals_conceded"] += score1

    if score1 > score2:
        teams[team1]["points"] += 3

    elif score1 < score2:
        teams[team2]["points"] += 3

    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1


for team in teams:
    teams[team]["goal_difference"] = (
        teams[team]["goals_scored"]
        - teams[team]["goals_conceded"]
    )


ranking = sorted(
    teams.items(),
    key=lambda x: (
        -x[1]["points"],
        -x[1]["goal_difference"],
        -x[1]["goals_scored"],
        x[0]
    )
)

print("\n===== FINAL TOURNAMENT RANKINGS =====")
print("Rank\tTeam\t\tPoints\tGoal Difference")

for i, (team, data) in enumerate(ranking, 1):
    print(
        i, "\t",
        team, "\t\t",
        data["points"], "\t",
        data["goal_difference"]
    )

