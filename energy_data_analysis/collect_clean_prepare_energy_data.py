# filename: collect_clean_prepare_energy_data.py
import pandas as pd

# Step 1: Collect Data
url = "https://data.cityofchicago.org/resource/energy_data.csv"  # Example URL for energy data
data = pd.read_csv(url)

# Step 2: Clean Data
data['date'] = pd.to_datetime(data['date'])  # Convert date column to datetime
data = data[(data['date'].dt.year >= 2020) & (data['date'].dt.year <= 2024)]  # Filter for years 2020-2024
data = data.dropna()  # Drop rows with missing values

# Step 3: Prepare Data
data = data.rename(columns={'old_column_name': 'new_column_name'})  # Example of renaming columns
# Add additional preparations as necessary, e.g. aggregating data

# Save the cleaned and prepared data to a new CSV file
data.to_csv('cleaned_chicago_energy_data_2020_2024.csv', index=False)

print("Data collection, cleaning, and preparation completed successfully.")