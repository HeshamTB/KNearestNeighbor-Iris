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


def NearestNieghbor(training:list, test:list) -> int:
    # Perform L2 distance (Sum of squared diff)
    for i in range(training):
        diff = numpy.subtract(test[:4], training[0][:4])
    #print(diff)

if __name__ == '__main__':
    data = readCSV('Iris.csv')
    for i in range(0, 40, 10):
       print(i, i+10)
       print(i+50, i+50+10)
       print(i+100, i+100+10)
       dataValidate = data[i:i+10]
       dataValidate.extend(data[i+50:i+50+10])
       dataValidate.extend(data[i+100:i+100+10])
       for j, v in enumerate(dataValidate):
           print(i ,j, v)