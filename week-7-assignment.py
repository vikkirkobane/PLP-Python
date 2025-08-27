import pandas as pd

   # Load the Iris dataset from sklearn
   from sklearn.datasets import load_iris
   import pandas as pd

import matplotlib.pyplot as plt
   import seaborn as sns

   iris = load_iris()
   df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
   df['species'] = iris.target

   # Alternatively, load from a CSV file
   # df = pd.read_csv('path/to/iris.csv')
print(df.head())

# Check data types and missing values
   print(df.info())
   print(df.isnull().sum())

# Fill missing values (if any)
   # df.fillna(method='ffill', inplace=True)

   # Or drop missing values
   df.dropna(inplace=True)

# Basic statistics of numerical columns
   print(df.describe())

# Compute the mean of a numerical column for each species
   mean_by_species = df.groupby('species').mean()
   print(mean_by_species)

# Example: Shown for concept
   plt.figure(figsize=(10, 5))
   plt.plot(df['Date'], df['Sales'], marker='o')
   plt.title('Sales Over Time')
   plt.xlabel('Date')
   plt.ylabel('Sales')
   plt.xticks(rotation=45)
   plt.grid()
   plt.show()

# Bar Chart
plt.figure(figsize=(10, 5))
   mean_by_species['sepal length (cm)'].plot(kind='bar')
   plt.title('Average Sepal Length per Species')
   plt.xlabel('Species')
   plt.ylabel('Average Sepal Length (cm)')
   plt.xticks(rotation=0)
   plt.show()

# Histogram
plt.figure(figsize=(10, 5))
   df['sepal length (cm)'].plot(kind='hist', bins=10, alpha=0.7)
   plt.title('Distribution of Sepal Length')
   plt.xlabel('Sepal Length (cm)')
   plt.ylabel('Frequency')
   plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
   sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='species', style='species')
   plt.title('Sepal Length vs Sepal Width')
   plt.xlabel('Sepal Length (cm)')
   plt.ylabel('Sepal Width (cm)')
   plt.show()
