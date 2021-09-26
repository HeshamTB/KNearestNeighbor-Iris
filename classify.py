#!/bin/env python

# Hesham T. Banafa, Al-Fahad Filmban
# EE482 Assignment 1 (KNN on Iris dataset)
# Fall 2021

import sys
import numpy
import math

# Split 30 validation, 120 for training.
## Constants for readable access.
_setosa = 0
_versicolor = 1
_virginica = 2

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

#manual hack
def vote(topK:list[list]):
    seto = 0
    vers = 0
    virg = 0
    for entry in topK:
        label = entry[1][4]
        if label == 'Iris-setosa': seto += 1
        elif label == 'Iris-versicolor': vers += 1
        elif label == 'Iris-virginica': virg += 1
        else: raise ValueError
    counts = list()
    counts.append([seto,'Iris-setosa']); counts.append([vers, 'Iris-versicolor'])
    counts.append([virg, 'Iris-virginica'])
    counts.sort(reverse=True, key=lambda count: count[0])
    return counts[0][1]

def NearestNieghbor(training:list, test:list) -> int:
    # Perform L2 distance (Sum of squared diff)
    for i in range(training):
        diff = numpy.subtract(test[:4], training[0][:4])
    #print(diff)

def EuclideanD(Mypoint=[],MappedPoint=[]):

    #I have four variable W, X, Y, Z
    #Euclidean Distance d = root( (X2-X1)^2  + (Y2-Y1)^2 +....   )
    Distance=math.sqrt( math.pow((MappedPoint[0]-Mypoint[0]),2)+
        math.pow((MappedPoint[1]-Mypoint[1]),2)+
        math.pow((MappedPoint[2]-Mypoint[2]),2)+
        math.pow((MappedPoint[3]-Mypoint[3]),2))
    return Distance

if __name__ == '__main__':
    data = readCSV('Iris.csv')
    predictions = list()
    try:
        K = int(sys.argv[1])
    except IndexError:
        K = 3 # Default
    # This is highly not scalable.
    print('K: ', K)
    for i in range(0, 50, 10):
        # Validation split
        #print('Fold ', int(i/10 +1)) 
        dataValidate = list()
        dataValidate = data[i:i+10]
        dataValidate.extend(data[i+50:i+50+10])
        dataValidate.extend(data[i+100:i+100+10])
        # i is the pivot. i, i+50, i+100
        # this is 'manual'. I am sure there is better solution.
        dataTrain = list()
        data_temp1 = data[0:50]
        del data_temp1[i:i+10]
        dataTrain.extend(data_temp1)
        data_temp2 = data[50:100]
        del data_temp2[i:i+10]
        dataTrain.extend(data_temp2)
        data_temp3 = data[100:150]
        del data_temp3[i:i+10]
        dataTrain.extend(data_temp3)

        # At this point we have data ready to be classifed for Kth fold.
        for i, testPoint in enumerate(dataValidate):
            distanceList = list() # This list should mapped directly to dataValidate list
            for j, trainPoint in enumerate(dataTrain): # For every train point
                distance = EuclideanD(testPoint, trainPoint) # L2 distance
                #print(distance)
                distanceList.append([distance, trainPoint, testPoint])
            distanceList.sort(key=lambda dist: dist[0])
            topK = distanceList[:K]
            #for j in topK: 
                #print(j)
            label = vote(topK)
            #print(label)
            predictions.append([label, testPoint[4], label == testPoint[4]]) # Pred, Actual, correct
            # Again redundant. For time.
            #print()
        #print('='*24)
            #print(distanceList)
    TPCount = 0
    for i in predictions: 
        #print(i)
        if i[2]: TPCount += 1
    print('Accuracy: ', (TPCount/len(predictions)*100))
    print()