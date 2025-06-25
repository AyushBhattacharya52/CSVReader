import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import re


filename = input("Enter the path to your CSV file: ")
df = pd.read_csv(filename)
print("File loaded successfully!")

# Display the first few rows of the DataFrame
print("Here are the first few rows of your data:")
print(df.head())
# Display basic information about the DataFrame
print("\nDataFrame Information:")
print(df.info())
# Display summary statistics of the DataFrame
print("\nSummary Statistics:")
print(df.describe(include='all'))
# Display the column names
print("\nColumn Names:")
print(df.columns.tolist())
# Display the number of missing values in each column
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
# Display the data types of each column
print("\nData Types of Each Column:")
print(df.dtypes)
# Display the number of unique values in each column
print("\nNumber of Unique Values in Each Column:")
print(df.nunique())
# Display the first few rows of the DataFrame again
print("\nFirst Few Rows of the DataFrame Again:")
print(df.head())
# Display the last few rows of the DataFrame
print("\nLast Few Rows of the DataFrame:")
print(df.tail())
# Display the shape of the DataFrame
print("\nShape of the DataFrame:")
print(df.shape)
# Display the memory usage of the DataFrame
print("\nMemory Usage of the DataFrame:")
print(df.memory_usage(deep=True))
# Display the index of the DataFrame
print("\nIndex of the DataFrame:")
print(df.index)
plot = input("Do you want to plot the data? (yes/no): ").strip().lower()
if plot.lower() == 'yes' or 'y' or 'yea' or 'yep' or 'sure' or 'ok' or 'okay':
    # Plotting the first few rows of the DataFrame
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df.head(10), palette='viridis')
    plt.title('First 10 Rows of Data')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.legend(title='Columns', loc='upper right')
    plt.show()