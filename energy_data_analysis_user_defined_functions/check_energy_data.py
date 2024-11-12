# filename: check_energy_data.py
import pandas as pd

# Load the data
data = pd.read_csv('chicago_energy_data.csv')

# Print the first few rows and the column names of the data
print(data.head())
print(data.columns)