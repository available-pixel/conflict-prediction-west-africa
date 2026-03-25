# visualize_predictions_stacked.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load predictions
# -----------------------------
predictions = pd.read_csv("../data/processed/predicted_conflict_events.csv")

# -----------------------------
# 2. Pivot data for plotting
# -----------------------------
plot_data = predictions.pivot(index='Country', columns='Year', values='Predicted_ConflictEvents').fillna(0)

# -----------------------------
# 3. Sort countries by 2027 predictions
# -----------------------------
plot_data = plot_data.sort_values(by=2027, ascending=False)

# -----------------------------
# 4. Set style
# -----------------------------
sns.set_style("whitegrid")
plt.figure(figsize=(14,7))

# -----------------------------
# 5. Plot stacked bar chart
# -----------------------------
colors = ['#1f77b4', '#ff7f0e']  # 2024: blue, 2027: orange
plot_data.plot(kind='bar', stacked=True, color=colors, figsize=(14,7))
plt.title("Predicted Conflict Events in West African Countries: 2024 vs 2027 (Stacked)", fontsize=16)
plt.ylabel("Number of Conflict Events", fontsize=12)
plt.xlabel("Country", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Year')
plt.tight_layout()

# -----------------------------
# 6. Save figure
# -----------------------------
plt.savefig("../data/processed/conflict_predictions_stacked_2024_2027.png")
plt.show()