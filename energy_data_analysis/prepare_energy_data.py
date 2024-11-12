# filename: prepare_energy_data.py
import os
import pandas as pd
import numpy as np

# Step 1: Check for the file
file_path = 'chicago_energy_data.csv'

if os.path.exists(file_path):
    # Step 2: Read the data if it exists
    df = pd.read_csv(file_path)
else:
    # Step 3: Generate sample data if it doesn't exist
    years = pd.date_range(start='2020-01-01', end='2024-12-31', freq='ME')
    data = {
        'Year': years.year,
        'Month': years.month,
        'Energy_Use': np.random.randint(100, 1000, size=len(years)),  # Sample energy use data
        'Type': np.random.choice(['Residential', 'Commercial', 'Industrial'], size=len(years))
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

# Step 4: Clean and prepare the data
# Check for missing values and fill them
df.ffill(inplace=True)

# Check the data types and convert if necessary
df['Year'] = df['Year'].astype(int)
df['Month'] = df['Month'].astype(int)

# Print the cleaned data
print(df)