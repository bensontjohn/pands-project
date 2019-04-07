# Benson Thomas John, 2019
# Project entailing researching Fisher's Iris data set

# import pandas library module
import pandas

dataset = pandas.read_csv('iris.csv')

# To print the first 5 rows from the dataset

print(dataset.head())

# To find the number of rows and columns in the dataset
print(dataset.shape)
