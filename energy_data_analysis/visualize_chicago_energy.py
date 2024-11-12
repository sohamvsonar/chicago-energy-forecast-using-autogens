# filename: visualize_chicago_energy.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('chicago_energy_data.csv')

# Convert the 'Year' column to datetime if necessary (assuming there's a 'Year' column)
data['Year'] = pd.to_datetime(data['Year'], format='%Y').dt.year

# Filter for the years 2020-2024
filtered_data = data[(data['Year'] >= 2020) & (data['Year'] <= 2024)]

# Visualize the energy usage
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Year'], filtered_data['Usage'], marker='o')  # Replace 'Usage' with the actual column name for energy usage
plt.title('Chicago Energy Usage (2020-2024)')
plt.xlabel('Year')
plt.ylabel('Energy Usage')
plt.grid()
plt.xticks(filtered_data['Year'])
plt.savefig('chicago_energy_usage_2020_2024.png')
plt.close()  # Use close instead of show to prevent showing in an interactive window