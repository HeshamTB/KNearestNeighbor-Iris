#!/bin/env python

# Hesham T. Banafa
# EE482 Assignment 1 (KNN on Iris dataset)
# Fall 2021

import sys
import numpy

# Split 30 validation, 120 for training.
## Constants for readable access.
_setosa = 0
_versicolor = 1
_virginica = 2

# TODO: Correct validation/testing split
# TODO: Implemnt KNN with L1, L2 and K = 1, 3, 5 ...
# TODO: Check results (Accuracy, )

## Read dataset Comma sep val
## This is only for this use case, not general use.
## Returns full data set with data points as rows.
def readCSV(filename)-> list:
    import csv
    data = list()
    with open(filename,'r') as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            #print(row, type(row))
            if (type(row) == list and len(row) == 6): # Sanity checks
                try:
                    # This removes ID col
                    row = [float(row[1]),float(row[2]),float(row[3]),float(row[4]),row[5]]
                    data.append(row)
                except ValueError as ex:
                    pass # probably first line
            else:
                print('error reading file', file=sys.stderr)
                exit(1)
    return data

"""
Returns (120, 30) random split
"""
def splitData(data:list[list])-> (list, list):
    # Goal is to split 30/120
    # one way is to random shuffle then take 30/120
    import random
    random.shuffle(data)
    validationList = data[:30]
    trainingList = data[30:]
    return trainingList, validationList

def NearestNieghbor(training:list, test:list) -> int:
    # Perform L2 distance (Sum of squared diff)
    for i in range(training):
        diff = numpy.subtract(test[:4], training[0][:4])
    #print(diff)

if __name__ == '__main__':
    data = readCSV('Iris.csv')
    dataTrain, dataTest = splitData(data)
    #n = numpy.subtract(dataTrain[0][:4], dataTest[0][:4])
    #print(n)
    # Loop every test data point
    # and classify
    # In reality, we have the label, but we want to predict as if we don't know.
    for row in range(len(dataTest)):
        print(row ,dataTest[row])
        #result = NearestNieghbor(dataTrain, dataTest[row])