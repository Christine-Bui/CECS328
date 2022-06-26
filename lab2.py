'''
Name: Christine Bui
Partner: Matthew Eskridge
Programming Assignment 2
'''
import math
import random
import timeit

heap_size = 0

def heapify(a, i):
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
        heapify(a, smallest)

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

###############################################################    

def insert(a, user_input):
    a.append(user_input)
    for i in range((math.floor(len(a)/2) - 1), -1, - 1):
        heapify(a, i)
    
def pop(a, user_input):
    a.pop(user_input)
    for i in range((math.floor(len(a)/2) - 1), -1, - 1):
        heapify(a, i)

def buildMinHeap(a):
    for i in range((math.floor(len(a)/2) - 1), -1, - 1):
        heapify(a,i)
    return a

def heapSort(a):
    buildMinHeap(a)
    for i in range(len(a)-2, 0, -1) :
        print("i:", i, "\n")
        a[1], a[i] = a[i], a[1] 
        global heap_size
        heap_size -= 1
        heapify(a, 1)

############################################################### 

a = [1, 5, 7, 2, 3]
b = []


print("""
      1. Create an empty min heap
      2. Create a min heap with integers you choose
      3. Insert an element
      4. Remove an element
      5. Sort heap
      6. Generate and sort random array of length n
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

        start1 = timeit.default_timer()
        heapSort(a)
        end1 = timeit.default_timer()
        time1 = end1 - start1

        start2 = timeit.default_timer()
        quickSort(a, 1, len(a) - 1)
        end2 = timeit.default_timer()
        time2 = end2 - start2

        print("Heap sort:")
        print(time1)
        print("Quick sort:")
        print(time2)


    print("""
      1. Create an empty min heap
      2. Create a min heap with integers you choose
      3. Insert an element
      4. Remove an element
      5. Sort heap
      6. Generate and sort random array of length n
      7. Quit
      """)
    option = int(input("Input an option: "))

print("\nHave a nice day!")