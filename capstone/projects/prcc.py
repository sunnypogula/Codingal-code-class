import pandas as pd

# Load the datasets
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# 1. Display basic information to identify unwanted columns and missing/null values
print("--- Matches Info ---")
matches.info()

print("\n--- Deliveries Info ---")
deliveries.info()

# 2. Drop unwanted columns
# Columns with high proportions of null values (e.g., 'umpire3' in standard IPL matches dataset)
# or irrelevant metadata can be dropped.
matches_cleaned = matches.drop(columns=["umpire3"], errors="ignore")

# 3. Handle null / missing values
# For categorical columns, fill null values with a placeholder like 'Unknown' or mode
matches_cleaned["city"] = matches_cleaned["city"].fillna("Unknown")
matches_cleaned["winner"] = matches_cleaned["winner"].fillna("No Result")
matches_cleaned["player_of_match"] = matches_cleaned["player_of_match"].fillna(
    "None"
)

# For deliveries, handle missing player dismissals or extras if present
deliveries_cleaned = deliveries.copy()
if "dismissal_kind" in deliveries_cleaned.columns:
    deliveries_cleaned["dismissal_kind"] = deliveries_cleaned[
        "dismissal_kind"
    ].fillna("Not Out")
if "player_dismissed" in deliveries_cleaned.columns:
    deliveries_cleaned["player_dismissed"] = deliveries_cleaned[
        "player_dismissed"
    ].fillna("None")

# Verify that null values have been handled
print("\n--- Remaining Null Values in Matches ---")
print(matches_cleaned.isnull().sum())

print("\n--- Remaining Null Values in Deliveries ---")
print(deliveries_cleaned.isnull().sum())