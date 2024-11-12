# filename: check_columns.py
import pandas as pd

# Load the data
data = pd.read_csv('chicago_energy_data.csv')

# Print the column names
print(data.columns.tolist())