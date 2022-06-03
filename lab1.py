'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 1
'''

def bubbleSort():
    pass

def insertionSort(data):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1

        while (j >= 0) and (data[j] < temp):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp


def quickSort():
    pass

# EXTRA CREDIT
def mergeSort():
    pass


arr = [2, 3, 4, 5, 6]
insertionSort(arr)
print(arr)