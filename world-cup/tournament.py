import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    filename = sys.argv[1]
    # Opening file given in command line argument.
    with open(filename) as file:
        # Using DictReader to get the data in csv file as a list of dictionaries.
        reader = csv.DictReader(file)
        for row in reader:
            # Converting rating of each team from string to integer form so it can be processed easily.
            row["rating"] = int(row["rating"])
            # Storing the whole data from csv in teams(as a list of dictionaries)
            teams.append(row)

    counts = {}
    # Simulate n tournaments and record each team wins in counts dictionary.
    for _ in range(N):
        # Simulate tourament function to get winner
        winner = simulate_tournament(teams)
        # Check if winning team is already in the dictionary.If not adding it.
        if not (winner in counts):
            counts[winner] = 1
        # If team already in the dictionary. Increment its wins.
        else:
            counts[winner] += 1
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team],reverse=True):
        print(team)
        #print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    # Simulate a game.
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    # Using probability and randomness to name winner beacause its a soccer match.
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    # Return True if team1 wins, False otherwise.
    return random.random() < probability


def simulate_round(teams):
    # Simulate a round. Return a list of winning teams.
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    # Starting a forever loop.
    while True:
        teams = simulate_round(teams)
        # Checking if only one team left.
        if len(teams) == 1:
            """As teams is a list of dictionaries.
            Two square brackets.One for getting the individual dictionary and the other for getting team's name.
            """
            return teams[0]["team"]


if __name__ == "__main__":
    main()
