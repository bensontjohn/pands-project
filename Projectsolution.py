# Benson Thomas John, 2019
# Project entailing researching Fisher's Iris data set

# import pandas library module
import pandas

#import matplotlib.pyplot
import matplotlib.pyplot as plt

# read the csv dataset and store in dataset variable
dataset = pandas.read_csv('iris.csv')

# To print the first 5 rows from the dataset

print(dataset.head())

# To find the number of rows and columns in the dataset
print(dataset.shape)

# create histogram of the dataset
dataset.hist()

# displays the histogram plot
plt.show()
