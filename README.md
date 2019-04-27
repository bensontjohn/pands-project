# Project  - Iris dataset

This repository contains my Project for the module Programming and Scripting at GMIT [See here for the instructions] (https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

### How to download this repository:

1. Go to Github.
2. Click the download button.

### How to run the code:

1. Make sure you have Python installed.

### Project Design

This project is to do a research on the Iris dataset, summarise the dataset using a Python script and a quick summary of the investigation.

### Background information:

Iris dataset is a set of data introduced by Sir. R.A. Fisher, who was a British geneticist and statistician (1890-1962). He was one of the greatest scientist of the 20th generation and was one of the first to apply statistical procedures in designing scientific experimentation. The Iris dataset contains data from 50 samples each of three species of the Iris flower picked at random. The three species are:

1.	Iris Setosa
2.	Iris Versicolour
3.	Iris Virginica

Each species of flowers has 4 features/attributes in centimeters(cms). They are:

1.	Sepal length
2.	Sepal width
3.	Petal length
4.	Petal width

One type of iris plant is linearly separable from the other 2 but these 2 are not linearly separable from each other. This is one of the most widely known database used in pattern recognition works and Fisher’s paper on it is frequently referenced. 

The dataset was found in the given link in csv format: https://gist.github.com/curran/a08a1080b88344b0c8a7.

![](https://cdn-images-1.medium.com/max/1200/1*2uGt_aWJoBjqF2qTzRc2JQ.jpeg)

The libraries used in this project are:

1. Pandas - Open source, easy to use data structures and data analysis tool.
2. Matplotlib - Plotting library used to embedd plots into applications.

### The iris dataset is imported using the pandas library:

    import pandas as pd
    dataset = pd.read_csv('iris.csv')

### To find the number of rows and columns in the dataset:

    dataset.shape

### To read the first 5 lines of data:

    dataset.head()

### To read the last 5 lines of data:

    dataset.tail()

### Investigation of the data:

    dataset.min()
    dataset.max()
    dataset.mean()

### Summary statistics:

    summary = dataset.describe()
    summary = summary.transpose()
    summary.head()

![Table of Summary statistics](https://github.com/bensontjohn/pands-project/blob/master/summary_statistics.png)

### Below is the histogram of the plots for each measurement:


![Histogram](https://github.com/bensontjohn/pands-project/blob/master/Histogram.png)


To summarise this project research, different methods were used to analyse the iris dataset. The pandas library was used to read the iris dataset which is in a csv format, there are total 150 rows and 5 columns in the dataset for species. Minimum and Maximum values of the each of the attributes were calculate using min and max methods. Also, calculated mean, percentile of the attributes. A histogram plot of the dataset was also done.

### References:

1.	Fisher, RA (1936) The use of multiple measuremetns in taxonomic problems. Annals of Eugenics Vol 7, Issue 2  https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
2.	Sir Ronald Aylmer Fisher. Encylopedia Britannica, Last Updated Feb 13, 2019. https://www.britannica.com/biography/Ronald-Aylmer-Fisher
3.	 Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.   https://archive.ics.uci.edu/ml/datasets/iris
4.	Your First Machine Learning Project in Python Step-By-Step by Jason Brownlee on June 10, 2016 in Python Machine Learning https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
5. Python Iris project:  https://github.com/RitRa/Project2018-iris 
6. Python | Pandas Dataframe: https://www.geeksforgeeks.org/python-pandas-dataframe/
