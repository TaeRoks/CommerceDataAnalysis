import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV files
order_items = pd.read_csv('order_items.csv')
products = pd.read_csv('products.csv')
order_payments = pd.read_csv('order_payments.csv')

# Merge dataframes to get comprehensive information
merged_data = pd.merge(order_items, products, on='product_id', how='left')
merged_data = pd.merge(merged_data, order_payments, on='order_id', how='left')

# Seller analysis for leaders/outsiders in sales
seller_sales = merged_data.groupby('seller_id')['payment_value'].sum().reset_index()
seller_sales = seller_sales.sort_values(by='payment_value', ascending=False)
print("Seller Analysis - Leaders in Sales:")
print(seller_sales.head())  

# Sellers in each category analysis
category_seller_sales = merged_data.groupby(['seller_id', 'product_category_name'])['payment_value'].sum().reset_index()
category_seller_sales = category_seller_sales.sort_values(by=['product_category_name', 'payment_value'], ascending=[True, False])

# Specify the category to analyze
selected_category = 'informatica_acessorios'  # Replace with the desired category

# Filter data for the selected category
selected_category_data = category_seller_sales[category_seller_sales['product_category_name'] == selected_category]

# Visualization for leaders in sales
plt.figure(figsize=(10, 6))
sns.barplot(x='seller_id', y='payment_value', data=seller_sales.head(10))
plt.title('Top 10 Sellers - Leaders in Sales')
plt.xlabel('Seller ID')
plt.ylabel('Total Sales')
plt.show()

# Visualization for outsiders in sales
plt.figure(figsize=(10, 6))
sns.barplot(x='seller_id', y='payment_value', data=seller_sales.tail(10))
plt.title('Bottom 10 Sellers - Outsiders in Sales')
plt.xlabel('Seller ID')
plt.ylabel('Total Sales')
plt.show()

# Visualization for leaders in the selected category
plt.figure(figsize=(10, 6))
sns.barplot(x='seller_id', y='payment_value', data=selected_category_data.head(10))
plt.title(f'Top 10 Sellers - Leaders in {selected_category} Sales')
plt.xlabel('Seller ID')
plt.ylabel('Total Sales')
plt.show()

# Visualization for outsiders in the selected category
plt.figure(figsize=(10, 6))
sns.barplot(x='seller_id', y='payment_value', data=selected_category_data.tail(10))
plt.title(f'Bottom 10 Sellers - Outsiders in {selected_category} Sales')
plt.xlabel('Seller ID')
plt.ylabel('Total Sales')
plt.show()
