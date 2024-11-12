# filename: clean_chicago_energy_data.py
import pandas as pd

# Load the data
data = pd.read_csv('chicago_energy_data.csv')

# Display the initial data
print("Initial Data:")
print(data.head())

# Check for missing values
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Clean the data (if needed)
# Here we just ensure there are no missing values; you could fill or drop as required
data.fillna(0, inplace=True)  # Fill missing values with 0

# Rename columns if necessary (for cleaner naming, in this case, they are fine)
data.rename(columns={
    'Electricity_Consumption_kWh': 'Electricity Consumption (kWh)',
    'Natural_Gas_Consumption_therms': 'Natural Gas Consumption (therms)'
}, inplace=True)

# Ensure proper data types (all should already be correct)
data.dtypes

# Save the cleaned data back to a new CSV file
data.to_csv('cleaned_chicago_energy_data.csv', index=False)

print("\nData cleaned and saved to cleaned_chicago_energy_data.csv.")