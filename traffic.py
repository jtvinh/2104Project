# Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
file = "/home/ugrads/majors/jtvinh/cs2104/project/traffic.csv"
names = ['RTE_NM', 'Route Label', 'Street Name', 'Host RTE_NM', 'Class Quality Dir']  # Adjusted columns
dataset = pd.read_csv(file, usecols=names)

# Print the data types of the columns to check which ones are numeric
print("Data types of the columns:")
print(dataset.dtypes)

# Check for any missing data
print("\nMissing data in each column:")
print(dataset.isnull().sum())

# Filter out non-numeric columns for the scatter matrix plot
numeric_dataset = dataset.select_dtypes(include=[float, int])

# Check the first few rows of the numeric dataset
print("\nFirst few rows of the numeric dataset:")
print(numeric_dataset.head())

# If there are missing values in the numeric columns, we can fill or drop them
if numeric_dataset.isnull().sum().any():
    print("\nThere are missing values in the numeric columns.")
    # Option to fill missing values with the mean of the column
   # numeric_dataset = numeric_dataset.fillna(numeric_dataset.mean())
    # Alternatively, you could drop rows with missing values:
    numeric_dataset = numeric_dataset.dropna()

# Check again if the numeric dataset is empty
if numeric_dataset.empty:
    print("No valid numeric data available for plotting.")
else:
    # Scatter matrix for numeric data
    scatter_matrix(numeric_dataset)
    plt.savefig('matrix.png')

# Print the dimensions of the dataset
print("\nThe file " + file + " has data with dimensions: ")
print(dataset.shape)

# Prints the first 20 pieces of data
print("\nFirst 20 rows of the dataset:")
print(dataset.head(20))

# Count means deviations min median etc a summary of all the data
print("\nSummary statistics:")
print(dataset.describe())

# Class distribution (count of unique values in 'Route Label' column)
print("\nClass distribution by Route Label:")
print(dataset.groupby('Route Label').size())

# Box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.savefig('box.png')

# Histograms
dataset.hist()
plt.savefig('hist.png')

# Convert the dataset to HTML
html_table = dataset.to_html()

# Save the HTML output to a file
html_file_path = '/home/ugrads/majors/jtvinh/cs2104/project/traffic_table.html'
with open(html_file_path, 'w') as f:
    f.write(html_table)

html_file_path
