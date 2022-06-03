'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 1
'''

def bubbleSort(data):
    #pass
    for i in (1, len(data) - 1):
        for j in (len(data), i + 1, -1):
            if data[j] < data[j - 1]:
                placeholder = data[j]
                data[j] = data[j - 1]
                data[j - 1] = placeholder
    return data

def insertionSort():
    pass

def quickSort():
    pass

# EXTRA CREDIT
def mergeSort():
    pass

data = [4, 3, 6, 2, 7, 4, 12, 8, 9]
print(bubbleSort(data))