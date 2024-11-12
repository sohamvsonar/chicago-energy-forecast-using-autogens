# filename: prepare_chicago_energy_data.py
import pandas as pd
import requests
from io import StringIO

# Step 1: Download the data
url = "https://example.com/chicago_energy_data.csv"  # Replace with actual URL
response = requests.get(url)

# Step 2: Load data into a DataFrame
data = StringIO(response.text)
df = pd.read_csv(data)

# Step 3: Filter data for the years 2020-2024
df['Year'] = pd.to_datetime(df['Date']).dt.year  # Assuming there's a 'Date' column
df_filtered = df[(df['Year'] >= 2020) & (df['Year'] <= 2024)]

# Step 4: Clean data by handling missing values
df_cleaned = df_filtered.dropna()

# Step 5: Prepare data (this can include various transformations)
# Here, I'm assuming we want to reset the index after cleaning
df_prepared = df_cleaned.reset_index(drop=True)

# Display the first few rows for verification
print(df_prepared.head())

# Save cleaned and prepared data to a new file
df_prepared.to_csv('chicago_energy_data_prepared_2020_2024.csv', index=False)