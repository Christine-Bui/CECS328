'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 2
'''
import math
from tkinter import LEFT, RIGHT

user_input = 0
option = ''

def minHeapify(a, i):
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l <= heap_size and a[l] < a[i]:
        smallest = l
    else:
        smallest = i
    if r <= heap_size and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i] #swapping
        minHeapify(a, smallest)
        
def buildMinHeap(a):
    for i in range((math.floor(heap_size/2) - 1), -1, - 1):
        minHeapify(a,i)
        
def heapSort(a):
    buildMinHeap(a)
    for i in range(0, heap_size - 2) :
        a[1], a[i] = a[i], a[1] 
        heap_size -= 1
        minHeapify(a, 1)

def insert(a, user_input):
    pass
    
def pop(a, user_input):
    pass

while option != 'quit':
    if option == "insert":
        insert()
    elif option == 'pop':
        pop()
    elif option == 'build heap':
        buildMinHeap(user_input)
    elif option == 'heap sort':
        heapSort(user_input)
    else: 
        quit()
        
user_input = [1, 5, 7, 2, 3]          
heap_size = len(user_input)
