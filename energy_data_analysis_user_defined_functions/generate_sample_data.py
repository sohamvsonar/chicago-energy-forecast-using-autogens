# filename: generate_sample_data.py
import pandas as pd
import numpy as np

# Generate sample data
years = np.arange(2020, 2025)
months = np.arange(1, 13)
data = []

for year in years:
    for month in months:
        consumption = np.random.randint(100000, 150000)  # Sample energy consumption
        cost = consumption * 0.12  # Sample energy cost at a rate of $0.12 per unit
        data.append([year, month, consumption, cost])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Year', 'Month', 'Energy_Consumption', 'Energy_Cost'])

# Save to CSV
df.to_csv('chicago_energy_data.csv', index=False)