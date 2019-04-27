# Benson Thomas John, 2019
# Project researching Fisher's Iris data set

# import pandas library module
import pandas as pd

#import matplotlib.pyplot
import matplotlib.pyplot as plt

# read the csv dataset and store in dataset variable
dataset = pd.read_csv('iris.csv')

# Referenced:  https://github.com/RitRa/Project2018-iris

# Print the unique species
unique = dataset['species'].unique()
print(unique)

# Referenced: http://www.datasciencemadesimple.com/get-minimum-value-column-python-pandas/

# Print the minimum values for each of the attributes
print(dataset.min())

# Referenced: https://www.geeksforgeeks.org/python-pandas-dataframe-max/

# Print the maximum values for each of the attributes
print(dataset.max())

# Referenced: https://www.geeksforgeeks.org/python-pandas-dataframe-mean/

# Print the mean values for each of the attributes
print(dataset.mean())

# To print the first 5 rows from the dataset
print(dataset.head())

# To find the number of rows and columns in the dataset
print(dataset.shape)

# Adapted from https://stackoverflow.com/a/38863443

# To view statistical details like percentile, count, mean, standard deviation
summary = dataset.describe()

# To write rows as columns and vice-versa
summary = summary.transpose()

# Print the first 5 rows of the summary variable values from the dataset
print(summary.head())

# create histogram of the dataset
dataset.hist()

# displays the histogram plot
plt.show()