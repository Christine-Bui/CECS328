'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 2
'''
import math

def minHeapify(a, i):
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l <= n and a[l] < a[i]:
        smallest = l
    else:
        smallest = i
    if r <= n and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i] #swapping
        minHeapify(a, smallest)
        
def buildMinHeap(a):
    for i in range((math.floor(n/2) - 1), -1, - 1):
        minHeapify(a,i)
        
def heapSort(a):
    buildMinHeap(a)
    for i in range(n, 0, - 2) :
        a[1], a[i] = a[i], a[1] 
        a.heap_size -= 1
        minHeapify(a, 1)

def insert(a, user_input):
    pass
    
def pop(a, user_input):
    pass

a = [1, 5, 7, 2, 3]          
n = len(a)

print("""
      1. Insert an element
      2. Remove an element
      3. Build heap
      4. Sort heap
      5. Quit
      """)
option = input("Input an option: ")

while option != 5:
    if option == 1:
        user_input = input("Enter an element to insert into heap: ")
        insert(a, user_input)
    elif option == 2:
        user_input = input("Enter an element to remove from heap: ")
        pop(a, user_input)
    elif option == 3:
        buildMinHeap(a)
    elif option == 4:
        heapSort(a)
    elif option == 5: 
        quit()
    else:
        print("Re-enter a valid option. ")