import numpy as np

players = np.array([
    "Babar",
    "Kohli",
    "Root",
    "Smith",
    "Williamson"
])

runs = np.array([
    [45, 67, 23, 89, 54],
    [72, 45, 91, 34, 78],
    [33, 56, 42, 65, 29],
    [61, 44, 73, 52, 80],
    [55, 77, 48, 69, 91]
])
#matches = np.array([10, 12, 8, 11, 9])

#total_sum = np.sum(runs)
#average_runs = np.mean(runs)
#highest_runs = np.max(runs)
#lowest_runs = np.min(runs)

#largest_valus = np.argmax(runs)
#best_player = largest_valus
#above_average = players[runs > average_runs]
#runs_above_average= runs[runs > average_runs]
#runs_per_match = runs/matches
#highest_average_index = np.argmax(runs_per_match)
#highest_runs_per_match = np.argmax(runs_per_match)
average_runs = np.mean(runs, axis=1)
highest_player_index = np.argmax(average_runs)
highest_average_runs = players[highest_player_index]
highest_score = np.max(runs)
equal_to = runs == highest_score
positions = np.where(runs == highest_score)
match_averages = np.mean(runs, axis=0)


#print("Total: ", total_sum)
#print("Average: ", average_runs)
#print("Highest: ", highest_runs)
#print("Lowest: ", lowest_runs)
#print("Best player: ", players[largest_valus])
#print("Largest Run: ", runs[largest_valus])
#print("Players above average:", above_average)
#print("Runs above average: ", runs_above_average)
#print("Runs per match: ", runs_per_match)
#print("Highest runs per match: ", runs_per_match[highest_average_index])
#print("Best runs-per-match player: ", players[highest_runs_per_match])
#print(np.mean(runs, axis=1))
#print(np.sum(runs, axis=0))
print("Best player average: ", highest_average_runs)
print("Average: ", average_runs[highest_player_index])
print("Highest score: ", highest_score)
print(equal_to)
print(runs[runs == highest_score])
print(np.where(runs == highest_score))
print(players[positions[0]])
print("Average score per match:", match_averages)