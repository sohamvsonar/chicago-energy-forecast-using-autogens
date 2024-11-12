

def Get_ChicagoEnergyData():
    """Data Engineer":"Responsibilities: Generate code to collect data from any source, if not found make sample data, clean.
    
    Return: prepare Chicago Energy data for 2020-2024 in a csv file name chicago_energy_data.csv.
    """
    import pandas as pd
    import numpy as np

    # Step 1: Generate sample data
    years = [2020, 2021, 2022, 2023, 2024]
    months = [f'{i:02d}' for i in range(1, 13)]

    data = []

    # Here write the code to create random consumption values and random cost calculation.....


    # Step 2: Create DataFrame
    df = pd.DataFrame(data, columns=['Year', 'Month', 'Energy_Consumption', 'Energy_Cost'])

    # Step 3: Data Cleaning (if needed, e.g., checking for NaN)
    df.dropna(inplace=True)  # removing any NaN values

    # Step 4: Export to CSV
    df.to_csv('chicago_energy_data.csv', index=False)
    print("Chicago Energy data for 2020-2024 has been generated and saved to 'chicago_energy_data.csv'.")


def Show_ChicagoEnergyData_CurrentUsage(data):
    """Generate code to visualize Chicago Energy usage for 2020-2024
    
    Args: chicago_energy_data.csv file which is in the same folder
    
    Return: plot the graph and save it as chicago_energy_consumption.png file.
    
    """
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data
    data = pd.read_csv('chicago_energy_data.csv')

    # Filter the data for the years 2020-2024
    filtered_data = data[(data['Year'] >= 2020) & (data['Year'] <= 2024)]

    # Create a datetime index for plotting (assuming Month is in numeric format)
    filtered_data['Date'] = pd.to_datetime(filtered_data[['Year', 'Month']].assign(Day=1))

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['Date'], filtered_data['Energy_Consumption'], marker='o')  # Plot Energy Consumption
    plt.title('Chicago Energy Consumption (2020-2024)')
    plt.xlabel('Date')
    plt.ylabel('Energy Consumption')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as a PNG file
    plt.savefig('chicago_energy_consumption.png')
    plt.show()


def Show_ChicagoEnergyData_UsageForecast(data):
    """Generate code to forecast Chicago Energy usage for 2025-2027
    
    Args: take reference from the chicago_energy_data.csv file which has data from 2020-2024 
    
    Return: plot it and save it as chicago_energy_forecast.png file.
    
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from statsmodels.tsa.arima.model import ARIMA

    # Step 1: Read the data from the CSV file
    data = pd.read_csv('chicago_energy_data.csv')

    # Create a DateTime index from 'Year' and 'Month'
    data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(Day=1))

    # Set the new Date column as the index
    data.set_index('Date', inplace=True)

    # Step 2: Resampling monthly data if necessary
    monthly_data = data['Energy_Consumption'].resample('ME').mean()

    # Step 3: Forecasting using ARIMA
    model = ARIMA(monthly_data, order=(5, 1, 0))  # Parameters may need tuning
    model_fit = model.fit()

    # Forecast for 2025-2027
    forecast = model_fit.forecast(steps=36)  # 3 years for monthly data
    forecast_index = pd.date_range(start='2025-01-01', periods=36, freq='ME')

    # Step 4: Create a plot
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data.index, monthly_data, label='Historical Data', color='blue')
    plt.plot(forecast_index, forecast, label='Forecasted Data', color='orange')
    plt.title('Chicago Energy Usage Forecast (2025-2027)')
    plt.xlabel('Date')
    plt.ylabel('Energy Usage')
    plt.legend()
    plt.grid()
    plt.savefig('chicago_energy_forecast.png')
    plt.show()


