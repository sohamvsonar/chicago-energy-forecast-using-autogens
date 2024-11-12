# filename: visualize_energy_consumption.py
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
data = pd.read_csv('chicago_energy_data.csv')

# Step 2: Filter data for 2020-2024
data['Year'] = pd.to_datetime(data['Date']).dt.year
filtered_data = data[(data['Year'] >= 2020) & (data['Year'] <= 2024)]

# Check if the filtered data is empty
if filtered_data.empty:
    print("No data found for the years 2020-2024.")
    exit()

# Step 3: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Year'], filtered_data['Consumption'], marker='o')
plt.title('Chicago Energy Consumption (2020-2024)')
plt.xlabel('Year')
plt.ylabel('Energy Consumption')
plt.grid()
plt.xticks(range(2020, 2025))
plt.savefig('chicago_energy_consumption.png')  # Step 4: Save the plot
plt.close()  # Close the plot to free up memory