'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 2
'''
import math
import random
import time
import heapq

heap_size = 0

def minHeapify(a, i):
    l = 2 * i 
    r = 2 * i + 1
    
    if l < len(a) and a[l] < a[i]:
        smallest = l
    else:
        smallest = i
    if r < len(a) and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i] #swapping
        minHeapify(a, smallest)

###############################################################    

def insert(a, user_input):
    a.append(user_input)
    for i in range((math.floor(len(a)/2) - 1), -1, - 1):
        minHeapify(a, i)
    
def pop(a, user_input):
    a.pop(user_input)
    for i in range((math.floor(len(a)/2) - 1), -1, - 1):
        minHeapify(a, i)

def buildMinHeap(a):
    for i in range((math.floor(len(a)/2) - 1), -1, - 1):
        minHeapify(a,i)
    return a

def heapSort(a):
    buildMinHeap(a)
    for i in range(len(a)-2, 0, -1) :
        print("i:", i, "\n")
        a[1], a[i] = a[i], a[1] 
        global heap_size
        heap_size -= 1
        minHeapify(a, 1)

############################################################### 

a = [1, 5, 7, 2, 3]
b = []


print("""
      1. Create an empty min heap
      2. Create a min heap with integers you choose
      3. Insert an element
      4. Remove an element
      5. Sort heap
      6. Enter length n
      7. Quit
      """)
option = int(input("Input an option: "))
print()

while option != 7:
    if option == 1:
        a = b #buildMinHeap(b)
        print("Min heap created!")
        print(a, "\n")

    elif option == 2:
        storage = str(input("Enter integers:\n"))
        storage2 = storage.split(",")
        a = []
        for i in storage2:
            a.append(int(i))
        a = buildMinHeap(a)
        print(a)

    elif option == 3:
        user_input = int(input("Enter an element to insert into heap: "))
        insert(a, user_input)
        print("Element inserted!")
        print(a, "\n")

    elif option == 4:
        user_input = int(input("Enter an node to remove from heap: "))
        pop(a, user_input)
        print("Element removed!")
        print(a, "\n")

    elif option == 5: 
        heapSort(a)
        print("Heap sorted!")
        print(a, "\n")

    elif option == 6:
        n = int(input("Enter a number as length for array: "))
        a = []
        for i in range(n):
            a.append(random.randint(-1000, 1000))

        start_time1 = time.time()
        heapSort(a)
        time1 = time.time() - start_time1

        start_time2 = time.time()
        heapq.heappush(a, random.randint(-1000, 1000))
        time2 = time.time() - start_time2

        print("Our heap sorting:")
        print(time1)
        print("Standard library sorting:")
        print(time2)


    print("""
      1. Create an empty min heap
      2. Create a min heap with integers you choose
      3. Insert an element
      4. Remove an element
      5. Sort heap
      6. Enter length n
      7. Quit
      """)
    option = int(input("Input an option: "))

print("\nHave a nice day!")