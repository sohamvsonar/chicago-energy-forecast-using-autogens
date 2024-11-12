# filename: chicago_energy_data.py
import pandas as pd
import numpy as np

# Step 1: Create a sample dataset
dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='ME')  # Changed 'M' to 'ME'
data = {
    'Date': dates,
    'Energy_Consumption_kWh': np.random.randint(1000, 5000, size=len(dates)),
    'Energy_Production_kWh': np.random.randint(1000, 5000, size=len(dates)),
    'Cost_per_kWh': np.round(np.random.uniform(0.1, 0.5, size=len(dates)), 2),
}

energy_data = pd.DataFrame(data)

# Step 2: Cleaning the dataset
# Removing any potential duplicates
energy_data.drop_duplicates(inplace=True)

# Filling missing values (if any) with the mean of the column
energy_data.fillna(energy_data.mean(), inplace=True)

# Step 3: Prepare the dataset
# Convert date column to datetime format
energy_data['Date'] = pd.to_datetime(energy_data['Date'])

# It's a good practice to set the index to the Date for time series data
energy_data.set_index('Date', inplace=True)

# Showing the first few rows of the cleaned dataset
print(energy_data.head())

# Saving the cleaned data to a CSV file
energy_data.to_csv('chicago_energy_data_2020_2024.csv')