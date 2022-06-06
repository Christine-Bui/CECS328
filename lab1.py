'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 1
'''

import math
import timeit
#from numpy import place


def bubbleSort(data):
    #pass
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
    #pass
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
def mergeSort(data, l, r, m):
    n1 = m - l + 1
    n2 = r - m
    L = []
    R = []
    for i in range(1, n1):
        L[i] = data[l + i - 1]
        for j in range(n2):
            R[i] = data[m + j]
    return

def merge(data, l, r):
    if l < r:
        m = math.floor((l + r) / 2) 
        mergeSort(data, l, m)
        mergeSort(data, m + 1, r)
        merge(data, l, m, r)
    return



data = [4, 3, 6, 2, 7, 4, 12, 8, 9]

start = timeit.default_timer()
print(f"\nBubble sort: {bubbleSort(data)}")
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print(f"Insertion sort: {insertionSort(data)}")
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

start = timeit.default_timer()
print(f"Quick sort: {quickSort(data, 1, len(data) - 1)}")
stop = timeit.default_timer()
print("Time:", stop - start, "\n")

#start = timeit.default_timer()
#print(f"Merge sort: {mergeSort(data, 1, len(data) // 2, len(data) - 1)}")
#stop = timeit.default_timer()
#print("Time:", stop - start, "\n")