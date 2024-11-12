# filename: clean_forecast_data.py
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('chicago_energy_data.csv')

# Data Cleaning
# Assuming the relevant column we are analyzing is named 'Energy_Usage' and is in monthly format
data['Date'] = pd.to_datetime(data['Date'])  # Ensure the date column is datetime
data.set_index('Date', inplace=True)

# Ensure energy usage data is numeric
data['Energy_Usage'] = pd.to_numeric(data['Energy_Usage'], errors='coerce')
data.dropna(subset=['Energy_Usage'], inplace=True)

# Resample to monthly
monthly_data = data['Energy_Usage'].resample('M').sum()  # Adjust the resampling as necessary

# Fit the ARIMA model
model = ARIMA(monthly_data, order=(5, 1, 0))  # Example parameters
model_fit = model.fit()

# Create forecast
forecast = model_fit.forecast(steps=36)  # Forecast for 3 years (36 months)

# Plotting the forecast
plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data, label='Observed', color='blue')
plt.plot(forecast.index, forecast, label='Forecast', color='red')
plt.title('Chicago Energy Usage Forecast 2025-2027')
plt.xlabel('Date')
plt.ylabel('Energy Usage')
plt.legend()
plt.savefig('chicago_energy_forecast.png')
plt.close()