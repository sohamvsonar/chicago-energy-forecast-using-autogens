# filename: collect_clean_prepare_chicago_energy.py
import pandas as pd

# Please replace this URL with the actual URL of the Chicago energy data
url = 'https://example.com/chicago_energy_data_2020_2024.csv'  # Modify to the actual data source

try:
    # Step 1: Collecting data
    data = pd.read_csv(url)

    # Step 2: Cleaning data
    # Drop columns that are not needed
    data.drop(columns=['unnecessary_column_1', 'unnecessary_column_2'], inplace=True)  # Modify as needed
    # Fill missing values with a suitable method (e.g., forward fill, backward fill, median)
    data.fillna(method='ffill', inplace=True)  # You can change the method based on your requirements
    # Convert date columns to datetime format if needed
    data['date'] = pd.to_datetime(data['date_column'])  # Modify 'date_column' to your date column

    # Step 3: Preparing data
    # Filtering data for the specific years
    data = data[(data['date'].dt.year >= 2020) & (data['date'].dt.year <= 2024)]
    # Reset index for cleanliness
    data.reset_index(drop=True, inplace=True)

    # Show the cleaned and prepared data
    print(data.head())

    # Optionally, save the cleaned data to a new CSV
    data.to_csv('cleaned_chicago_energy_2020_2024.csv', index=False)

except Exception as e:
    print(f"An error occurred: {e}")