# Benson Thomas John, 2019
# Project entailing researching Fisher's Iris data set

# import pandas library module
import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('iris.csv')

# To print the first 5 rows from the dataset

print(dataset.head())

# To find the number of rows and columns in the dataset
print(dataset.shape)

dataset.hist()
plt.show()