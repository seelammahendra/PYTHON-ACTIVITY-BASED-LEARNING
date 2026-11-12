# Sports Tournament Ranking System – Python

## 1. Problem Statement

The Sports Tournament Ranking System is used to store match results, calculate team scores, and generate final tournament rankings. The system awards points based on match results: 3 points for a win, 1 point for a draw, and 0 points for a loss. It calculates goal difference and total goals scored to resolve ties between teams. Finally, it displays the teams in ranking order according to the tournament rules.

## 2. Algorithm

1. Start the program.
2. Enter the number of teams participating in the tournament.
3. Enter the names of all teams.
4. Initialize points, goals scored, and goals conceded to zero.
5. Enter the number of matches.
6. Read the two team names and their scores for each match.
7. Award 3 points to the winning team.
8. Award 1 point to each team if the match is a draw.
9. Award 0 points to the losing team.
10. Calculate the goal difference for each team.
11. Sort teams based on:
    - Highest total points.
    - Highest goal difference.
    - Highest goals scored.
12. Display the final team rankings.
13. Stop the program.
## 3. Flow chart 
``` mermaid 
flowchart TD
    A([Start]) --> B[Enter Number of Teams]
    B --> C[Enter Team Names]
    C --> D[Initialize Team Scores]
    D --> E[Enter Number of Matches]
    E --> F[Enter Match Details and Scores]
    F --> G{Compare Team Scores}
    G -->|Team 1 Wins| H[Award 3 Points to Team 1]
    G -->|Team 2 Wins| I[Award 3 Points to Team 2]
    G -->|Draw| J[Award 1 Point to Both Teams]
    H --> K[Update Goals]
    I --> K
    J --> K
    K --> L{All Matches Completed?}
    L -->|No| F
    L -->|Yes| M[Calculate Goal Difference]
    M --> N[Sort Teams by Points and Tie-break Values]
    N --> O[Display Final Rankings]
    O --> P([Stop])

## 5. SAMPLE INPUT

Enter number of teams: 4
Enter team name: India
Enter team name: Australia
Enter team name: England
Enter team name: Pakistan

Enter number of matches: 4

Match 1
Enter first team: India
Enter second team: Australia
Enter first team score: 3
Enter second team score: 1

Match 2
Enter first team: England
Enter second team: Pakistan
Enter first team score: 2
Enter second team score: 2

Match 3
Enter first team: India
Enter second team: England
Enter first team score: 1
Enter second team score: 0

Match 4
Enter first team: Australia
Enter second team: Pakistan
Enter first team score: 2
Enter second team score: 1


## 6. Sample Output


===== FINAL TOURNAMENT RANKINGS =====

Rank   Team        Points   Goal Difference

1      India          6          3
2      Australia      3          0
3      England        1         -1
4      Pakistan       1         -2
