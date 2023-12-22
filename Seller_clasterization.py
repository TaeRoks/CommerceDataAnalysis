import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load order_items.csv, products.csv, and order_payments.csv
order_items = pd.read_csv('order_items.csv')
products = pd.read_csv('products.csv')
order_payments = pd.read_csv('order_payments.csv')

# Merge dataframes
merged_data = pd.merge(order_items, products, on='product_id', how='inner')
merged_data = pd.merge(merged_data, order_payments, on='order_id', how='inner')

# Calculate revenue for each seller
seller_revenue = merged_data.groupby('seller_id')['payment_value'].sum()

# Calculate total count of orders for each seller
seller_order_count = merged_data.groupby('seller_id')['order_id'].nunique()

# Create a new dataframe with revenue and order count
seller_data = pd.DataFrame({'Revenue': seller_revenue, 'OrderCount': seller_order_count})

# Normalize the data (optional, but often recommended for clustering)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
normalized_data = scaler.fit_transform(seller_data)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3)  # You can adjust the number of clusters as needed
seller_data['Cluster'] = kmeans.fit_predict(normalized_data)

# Visualize the clusters
plt.scatter(seller_data['Revenue'], seller_data['OrderCount'], c=seller_data['Cluster'], cmap='viridis')
plt.xlabel('Revenue')
plt.ylabel('Order Count')
plt.title('Seller Clustering based on Revenue and Order Count')
plt.show()
