import pandas as pd

RAW_FILE = "electric_vehicles_dataset.csv"

OUTPUT_FILE = "clean_ev_data.csv"

df = pd.read_csv(RAW_FILE)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

numeric_cols = [
    "battery_capacity_kwh",
    "range_km",
    "charge_time_hr",
    "price_usd",
    "autonomous_level",
    "co2_emissions_g_per_km",
    "safety_rating",
    "units_sold_2024",
    "warranty_years"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

if "range_km" in df.columns and "battery_capacity_kwh" in df.columns:
    df["range_per_kwh"] = df["range_km"] / df["battery_capacity_kwh"]

if "vehicle_id" in df.columns:
    df = df.drop_duplicates(subset=["vehicle_id"], keep="first")
else:
    df = df.drop_duplicates()

df.to_csv(OUTPUT_FILE, index=False)

print("Cleaning complete!")
print("Saved as:", OUTPUT_FILE)
