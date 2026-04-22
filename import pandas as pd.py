import pandas as pd
import os
from datetime import datetime

leaderboard_path = "leaderboard.csv"

results = [
    ["Random Forest", 0.89, 0.88, 0.87, 0.88]
]

# Load or create
if os.path.exists(leaderboard_path):
    lb = pd.read_csv(leaderboard_path)
else:
    lb = pd.DataFrame(columns=[
        "Model", "Accuracy", "Precision", "Recall", "F1 Score", "Date"
    ])

# Add date column
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

new_results = pd.DataFrame(results, columns=[
    "Model", "Accuracy", "Precision", "Recall", "F1 Score"
])

new_results["Date"] = current_time

lb = pd.concat([lb, new_results], ignore_index=True)

# Sort
lb = lb.sort_values(by="Accuracy", ascending=False)

# Rank
lb.reset_index(drop=True, inplace=True)
lb["Rank"] = lb.index + 1

lb.to_csv(leaderboard_path, index=False)

print(lb)
