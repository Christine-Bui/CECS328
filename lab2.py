'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 2
'''
import math
from tkinter import LEFT, RIGHT

def heapify(a, i):
    l = LEFT(i)
    r = RIGHT(i)
    
    if l <= heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i] #swapping
        heapify(a, largest)
        
def buildHeap(a):
    heap_size = len(a)
    for i in range(0, math.floor(len([a]/2)) - 1):
        heapify(a,i)
        
def heapSort(a):
    buildHeap(a)
    for i in range(0, len(a) - 2) :
        a[1], a[i] = a[i], a[1] 
        heap_size -= 1
        heapify(a, 1)

def insert():
    pass

def pop():
    pass

def quit():
    exit()



def menu():
    options = {
        0: 'insert',
        1: 'pop',
        2: 'buildHeap',
        3: 'heapSort',
        4: 'quit'
    }

a = [1, 5, 7, 2, 3]          
heap_size = len(a)
