import pandas as pd
import os

# 📁 File path
leaderboard_path = "leaderboard.csv"

# 📊 Example model results (EDIT THIS AFTER RUNNING YOUR MODEL)
# Format: Model, Accuracy, Precision, Recall, F1 Score
results = [
    ["Random Forest", 0.89, 0.88, 0.87, 0.88]
]

# 📥 Load existing leaderboard or create new
if os.path.exists(leaderboard_path):
    lb = pd.read_csv(leaderboard_path)
else:
    lb = pd.DataFrame(columns=["Model", "Accuracy", "Precision", "Recall", "F1 Score"])

# 📌 Convert results into DataFrame
new_results = pd.DataFrame(results, columns=[
    "Model", "Accuracy", "Precision", "Recall", "F1 Score"
])

# ➕ Append new results
lb = pd.concat([lb, new_results], ignore_index=True)

# 🔄 Remove duplicate models (keep latest)
lb = lb.drop_duplicates(subset=["Model"], keep="last")

# 🔽 Sort by Accuracy (highest first)
lb = lb.sort_values(by="Accuracy", ascending=False)

# 🏆 Add Rank
lb.reset_index(drop=True, inplace=True)
lb["Rank"] = lb.index + 1

# 💾 Save leaderboard
lb.to_csv(leaderboard_path, index=False)

# 🖥️ Show output
print("\n🏆 Updated Leaderboard:\n")
print(lb)