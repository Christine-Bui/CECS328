'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 1
'''

def bubbleSort(data):
    #pass
    for i in range(0, len(data) - 1):
        for j in range(len(data), i + 1, -1):
            if data[j-1] < data[j - 2]:
                placeholder = data[j - 1]
                data[j - 1] = data[j - 2]
                data[j - 2] = placeholder
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