# Benson Thomas John, 2019
# Project entailing researching Fisher's Iris data set

# import pandas library module
import pandas as pd

#import matplotlib.pyplot
import matplotlib.pyplot as plt

import numpy

df = pd.read_csv (r'iris.csv')
# print(df)
# read the csv dataset and store in dataset variable
dataset = pd.read_csv('iris.csv')

# Adapted from https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
mean1 = df['sepal_length'].mean()
print("Mean of the sepal length of the 3 species: " +str(mean1))

# To print the first 5 rows from the dataset

print(dataset.head())

# To find the number of rows and columns in the dataset
print(dataset.shape)

# create histogram of the dataset
dataset.hist()

# displays the histogram plot
plt.show()
