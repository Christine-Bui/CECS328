'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 1
'''

from cmath import inf
import math
import timeit
from xml.etree.ElementTree import QName
#from numpy import place
# import numpy as np


def bubbleSort(data):
    for i in range(0, len(data) - 1):
        for j in range(len(data), i + 1, -1):
            if data[j-1] > data[j - 2]:
                placeholder = data[j - 1]
                data[j - 1] = data[j - 2]
                data[j - 2] = placeholder
    return data

def insertionSort(data):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1

        while (j >= 0) and (data[j] < temp):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp
    return data

def quickSort(data, s, e):
    if s > e:
        part = partition(data, s, e)
        quickSort(data, s, part - 1)
        quickSort(data, part + 1, e)
    return data

def partition(data, s, e):
    x = data[e]
    i = s - 1
    for j in range(s, e - 1):
        if data[j] <= x:
            i += 1
            placeholder = data[i]
            data[i] = data[j]
            data[j] = placeholder
    placeholder = data[i + 1]
    data[i + 1] = data[e]
    data[e] = placeholder
    return i + 1

# EXTRA CREDIT
def merge(data, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [1] * (n1 + 1)
    R = [1] * (n2 + 1)
    
    for i in range(1, n1):
        L[i] = data[l + i - 1]
    for j in range(1, n2):
        R[j] = data[m + j]
    L[n1 + 1] = inf
    R[n2 + 1] = inf
    i = j = 1
    for k in range(l, r):
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
    return data

def mergeSort(data, l, r):
    if l < r:
        m = math.floor((l + r) / 2) 
        mergeSort(data, l, m)
        mergeSort(data, m + 1, r)
        merge(data, l, m, r)
    return data



acc_data = list(range(1, 1001))
dec_data = list(range(1, 10001)[::-1])
rand_data1 = np.random.randint(1,101,1000)
rand_data2 = np.random.randint(1,101,10000)

############## BUBBLE SORT ###############
print("---------------------------------------------------")
print("Bubble sort: \n")
start = timeit.default_timer()
print("Ascending input: ")
bubbleSort(acc_data)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Descending input: ")
bubbleSort(dec_data)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Random input (1000 elements): ")
bubbleSort(rand_data1)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Random input (10000 elements): ")
bubbleSort(rand_data2)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")
print("---------------------------------------------------")

############# INSERTION SORT ##############
print("Insertion sort: \n")
start = timeit.default_timer()
print("Ascending input: ")
insertionSort(acc_data)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Descending input: ")
insertionSort(dec_data)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Random input (1000 elements): ")
insertionSort(rand_data1)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Random input (10000 elements): ")
insertionSort(rand_data2)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")
print("---------------------------------------------------")

############### QUICK SORT ################
print("Quick sort: \n")
start = timeit.default_timer()
print("Ascending input: ")
quickSort(acc_data, 1, len(acc_data) - 1)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Descending input: ")
quickSort(dec_data, 1, len(dec_data) - 1)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Random input (1000 elements): ")
quickSort(rand_data1, 1, len(rand_data1) - 1)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print("Random input (10000 elements): ")
quickSort(rand_data2, 1, len(rand_data2) - 1)
stop = timeit.default_timer()
print("Time:", stop - start, "\n")
print("---------------------------------------------------")

############## EXTRA CREDIT ###############
# print("Merge Sort: \n")
# start = timeit.default_timer()
# print("Ascending input: ")
# mergeSort(acc_data, 1, len(acc_data) - 1)
# stop = timeit.default_timer()
# print("Time:", stop - start, "\n")

# start = timeit.default_timer()
# print("Descending input: ")
# mergeSort(dec_data, 1, len(dec_data) - 1)
# stop = timeit.default_timer()
# print("Time:", stop - start, "\n")

# start = timeit.default_timer()
# print("Random input (1000 elements): ")
# merge(rand_data1, 1, len(rand_data1) - 1)
# stop = timeit.default_timer()
# print("Time:", stop - start, "\n")

# start = timeit.default_timer()
# print("Random input (10000 elements): ")
# merge(rand_data2, 1, len(rand_data2) - 1)
# stop = timeit.default_timer()
# print("Time:", stop - start, "\n")