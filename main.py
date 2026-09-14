import numpy as np

players = np.array([
    "Babar",
    "Kohli",
    "Root",
    "Smith",
    "Williamson"
])

runs = np.array([450, 520, 380, 410, 490])

matches = np.array([10, 10, 10, 10, 10])

total_sum = np.sum(runs)
average_runs = np.mean(runs)
highest_runs = np.max(runs)
lowest_runs = np.min(runs)

largest_valus = np.argmax(runs)
best_player = largest_valus
above_average = players[runs > average_runs]

print("Total: ", total_sum)
print("Average: ", average_runs)
print("Highest: ", highest_runs)
print("Lowest: ", lowest_runs)
print("Best player: ", players[largest_valus])
print("Largest Run: ", runs[largest_valus])
print(runs > average_runs)
print("Players above average:", above_average)