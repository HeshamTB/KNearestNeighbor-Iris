#!/bin/env python

# Hesham T. Banafa
# EE482 Assignment 1 (KNN on Iris dataset)
# Fall 2021

import sys

# Split 30 validation, 120 for training.
## Constants for readable access.
_setosa = 0
_versicolor = 1
_virginica = 2


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
                data.append(row)
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
    trainingList = data[:30]
    validationList = data[30:]
    return trainingList, validationList

if __name__ == '__main__':    
    data = readCSV('Iris.csv')
    dataTrain, x = splitData(data)
    print("All data elemtns ", len(data))
    print("dataTrain ", len(dataTrain))
    print("valdTrain ", len(x))