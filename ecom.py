import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv('ecommerce_data.csv')

print(df.describe())

# Filter data for transactions made by a specific customer
specific_customer = df[df['customer_id'] == '12345']

# Filter data for transactions made in a specific month
specific_month = df[df['transaction_date'].str.startswith('2023-05')]

sorted_products = df.sort_values(by='revenue', ascending=False)

missing_values = df.isnull().sum()

df.groupby('product_category')['revenue'].sum().plot(kind='bar', title='Total Revenue by Product Category')

df = pd.read_csv("diabetes.csv")

df = pd.read_csv("diabetes.txt", sep="\s")
# Extracting the second sheet since Python uses 0-indexing
df = pd.read_excel('diabetes_multi.xlsx', sheet_name=1)
