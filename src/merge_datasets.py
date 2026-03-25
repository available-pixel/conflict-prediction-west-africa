import pandas as pd

# Load datasets
conflict = pd.read_csv("../data/raw/acled_conflict_events.csv")
econ = pd.read_csv("../data/raw/world_bank_econ.csv")
climate = pd.read_csv("../data/raw/world_bank_climate.csv")

# Merge datasets on Country and Year
merged = conflict.merge(econ, on=["Country", "Year"])
merged = merged.merge(climate, on=["Country", "Year"])

# Optional: check for missing values
print("Missing values per column:")
print(merged.isna().sum())

# Save merged dataset
merged.to_csv("../data/processed/conflict_dataset.csv", index=False)
print("Merged dataset saved to data/processed/conflict_dataset.csv")