import pandas as pd

def load_data(file_path):
    """
    Load the dataset into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the dataset file.
        
    Returns:
        pandas.DataFrame: DataFrame containing the dataset.
    """
    df = pd.read_csv(file_path)
    return df

def describe_data(df):
    """
    Generate descriptive statistics for the DataFrame.
    
    Parameters:
        df (pandas.DataFrame): DataFrame to describe.
    """
    print(df.describe())

def filter_by_customer(df, customer_id):
    """
    Filter data for transactions made by a specific customer.
    
    Parameters:
        df (pandas.DataFrame): DataFrame to filter.
        customer_id (str): ID of the customer to filter by.
        
    Returns:
        pandas.DataFrame: DataFrame containing transactions made by the specific customer.
    """
    return df[df['customer_id'] == customer_id]

def filter_by_month(df, year_month):
    """
    Filter data for transactions made in a specific month.
    
    Parameters:
        df (pandas.DataFrame): DataFrame to filter.
        year_month (str): Year and month to filter by in 'YYYY-MM' format.
        
    Returns:
        pandas.DataFrame: DataFrame containing transactions made in the specific month.
    """
    return df[df['transaction_date'].str.startswith(year_month)]

def sort_by_revenue(df):
    """
    Sort DataFrame by revenue in descending order.
    
    Parameters:
        df (pandas.DataFrame): DataFrame to sort.
        
    Returns:
        pandas.DataFrame: DataFrame sorted by revenue in descending order.
    """
    return df.sort_values(by='revenue', ascending=False)

def count_missing_values(df):
    """
    Count missing values in the DataFrame.
    
    Parameters:
        df (pandas.DataFrame): DataFrame to check for missing values.
        
    Returns:
        pandas.Series: Series containing counts of missing values for each column.
    """
    return df.isnull().sum()

def plot_total_revenue_by_category(df):
    """
    Plot total revenue by product category.
    
    Parameters:
        df (pandas.DataFrame): DataFrame containing the dataset.
    """
    df.groupby('product_category')['revenue'].sum().plot(kind='bar', title='Total Revenue by Product Category')

def load_text_data(file_path):
    """
    Load text-based dataset into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the text-based dataset file.
        
    Returns:
        pandas.DataFrame: DataFrame containing the text-based dataset.
    """
    df = pd.read_csv(file_path, sep="\s")
    return df

def load_excel_data(file_path, sheet_name):
    """
    Load Excel dataset into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str or int): Name or index of the sheet to read.
        
    Returns:
        pandas.DataFrame: DataFrame containing the Excel dataset.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

# Usage examples:
df = load_data('ecommerce_data.csv')
describe_data(df)
specific_customer = filter_by_customer(df, '12345')
specific_month = filter_by_month(df, '2023-05')
sorted_products = sort_by_revenue(df)
missing_values = count_missing_values(df)
plot_total_revenue_by_category(df)
df_text = load_text_data("diabetes.txt")
df_excel = load_excel_data('diabetes_multi.xlsx', sheet_name=1)
