# filename: chicago_energy_forecast.py
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