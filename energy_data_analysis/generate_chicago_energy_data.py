# filename: generate_chicago_energy_data.py
import pandas as pd
import numpy as np

# Step 1: Generate sample data
years = [2020, 2021, 2022, 2023, 2024]
months = [f'{i:02d}' for i in range(1, 13)]  # ['01', '02', ..., '12']

data = []

for year in years:
    for month in months:
        energy_consumption = np.random.randint(1000, 5000)  # random consumption values
        energy_cost = np.round(energy_consumption * np.random.uniform(0.1, 0.5), 2)  # random cost calculation
        data.append([year, month, energy_consumption, energy_cost])

# Step 2: Create DataFrame
df = pd.DataFrame(data, columns=['Year', 'Month', 'Energy_Consumption', 'Energy_Cost'])

# Step 3: Data Cleaning (if needed, e.g., checking for NaN)
df.dropna(inplace=True)  # removing any NaN values

# Step 4: Export to CSV
df.to_csv('chicago_energy_data.csv', index=False)
print("Chicago Energy data for 2020-2024 has been generated and saved to 'chicago_energy_data.csv'.")