# filename: visualize_chicago_energy_usage.py
import os
os.environ['MPLBACKEND'] = 'Agg'  # Force the backend to Agg before importing matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('chicago_energy_usage.csv')

# Filter data for the years 2020-2024
filtered_data = data[(data['Year'] >= 2020) & (data['Year'] <= 2024)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Year'], filtered_data['Usage'], marker='o', linestyle='-')
plt.title('Energy Usage in Chicago (2020-2024)', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Usage', fontsize=12)
plt.grid()
plt.xticks(filtered_data['Year'])

# Save the plot to a file
plt.savefig('chicago_energy_usage_plot.png')