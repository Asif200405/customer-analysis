from google.colab import files
uploaded=files.upload()

import pandas as pd
df=pd.read_csv('excel retail dataset (2).csv')
print(df.isnull().sum())

import pandas as pd
print(df.duplicated().sum())

df.fillna("en", inplace=True)

print(df.columns)
items_column = df['items']
items_column = df.get('items')

if items_column is not None:
    # Proceed with your operations
    print(items_column)
else:
    print("Column 'items' not found.")

import seaborn as sns
import matplotlib.pyplot as plt

# Count plot for the 'items' column
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='items', palette='viridis')

# Customize the plot
plt.title('Frequency of Each Item', fontsize=16)
plt.xlabel('Items', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()

# Show plot
plt.show()
# Bar plot for 'Item_Categories' and the count of 'items'
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Item_Categories', hue='items', palette='Set2')

# Customize the plot
plt.title('Items by Category', fontsize=16)
plt.xlabel('Item Categories', fontsize=12)
plt.ylabel('Count of Items', fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()

# Show plot
plt.show()
# Distribution plot for 'items' (assuming numeric data in 'items' column)
plt.figure(figsize=(10, 6))
sns.histplot(df['items'], kde=True, color='blue', bins=20)

# Customize the plot
plt.title('Distribution of Items', fontsize=16)
plt.xlabel('Items', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()

# Show plot
plt.show()
# Scatter plot between 'items' and 'Transaction_ID' (if applicable)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Transaction_ID', y='items', color='green')

# Customize the plot
plt.title('Items vs. Transaction ID', fontsize=16)
plt.xlabel('Transaction ID', fontsize=12)
plt.ylabel('Items', fontsize=12)
plt.tight_layout()

# Show plot
plt.show()
# Pie chart for the frequency of 'items'
item_counts = df['items'].value_counts()

# Plot pie chart
plt.figure(figsize=(8, 8))
item_counts.plot.pie(autopct='%1.1f%%', colors=sns.color_palette('Set3', len(item_counts)), startangle=90)

# Customize the plot
plt.title('Proportion of Each Item', fontsize=16)
plt.ylabel('')  # Hide the y-axis label
plt.tight_layout()

# Show plot
plt.show()
