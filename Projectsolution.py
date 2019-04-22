# Benson Thomas John, 2019
# Project entailing researching Fisher's Iris data set

# import pandas library module
import pandas as pd

#import matplotlib.pyplot
import matplotlib.pyplot as plt

# read the csv dataset and store in dataset variable
dataset = pd.read_csv('iris.csv')

# Adapted from https://github.com/RitRa/Project2018-iris

# Print the unique species
unique = dataset['species'].unique()
print(unique)

# Print the minimum values for each of the attributes
print(dataset.min())

# Print the maximun values for each of the attributes
print(dataset.max())

# Print the mean values for each of the attributes
print(dataset.mean())

# To print the first 5 rows from the dataset
print(dataset.head())

# To find the number of rows and columns in the dataset
print(dataset.shape)

# create histogram of the dataset
dataset.hist()

# displays the histogram plot
plt.show()
