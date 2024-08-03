import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('abc.csv', skiprows=4)

# Select the required columns (Country Name and a specific year, e.g., 2020)
data = data[['Country Name', '2020']]

# Drop rows with missing values
data.dropna(inplace=True)

# Rename columns for better readability
data.columns = ['Country', 'Population']

# Sort data by population
data = data.sort_values('Population', ascending=False).head(10)  # Top 10 countries

# Create the bar chart
plt.figure(figsize=(12, 8))
sns.barplot(x='Population', y='Country', data=data, palette='viridis')
plt.title('Top 10 Countries by Population in 2020')
plt.xlabel('Population')
plt.ylabel('Country')
plt.show()
