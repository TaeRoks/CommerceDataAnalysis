import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Step 1: Load the data
order_items = pd.read_csv('order_items.csv')
orders = pd.read_csv('orders.csv')

# Merge the dataframes
merged_data = pd.merge(order_items, orders, on='order_id')

# Step 2: Preprocess the data
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])
merged_data['purchase_date'] = merged_data['order_purchase_timestamp'].dt.date

# Step 3: Group and Aggregate
product_purchase_counts = merged_data.groupby(['product_id', 'purchase_date']).size().reset_index(name='purchase_count')

# Step 4: Create Time Series
time_series = product_purchase_counts.pivot(index='purchase_date', columns='product_id', values='purchase_count').fillna(0)

# Choose a product_id for forecasting
product_id_to_forecast = '167b4b8c4bd0c401bea62f5e050d70a4'
product_data = time_series[product_id_to_forecast].reset_index()

# Convert 'purchase_date' to datetime
product_data['purchase_date'] = pd.to_datetime(product_data['purchase_date'])

# Feature Engineering
product_data['year'] = product_data['purchase_date'].dt.year
product_data['month'] = product_data['purchase_date'].dt.month
product_data['day'] = product_data['purchase_date'].dt.day

# Split the data into training and testing sets
train_size = int(len(product_data) * 0.8)
train, test = product_data[:train_size], product_data[train_size:]

# Train the ARIMA model
order = (5, 1, 0)  # You may need to adjust these parameters based on your data
model = ARIMA(train[product_id_to_forecast], order=order)
fit_model = model.fit()

# Make predictions
predictions = fit_model.forecast(steps=len(test))

# Plot the results
plt.plot(product_data['purchase_date'], product_data[product_id_to_forecast], label='Actual', linestyle='solid', color='blue')
plt.plot(test['purchase_date'], predictions, label='Forecasted (ARIMA)', linestyle='dashed', color='red')
plt.legend()
plt.show()
