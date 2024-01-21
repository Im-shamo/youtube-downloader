import random
import dis
import time
# sorting
# In ascending order


def selection_sort(array):

    N = len(array)
    for i in range(N):
        key_index = i
        for j in range(i+1, N):
            if array[j] < array[key_index]:
                key_index = j
        swap(i, key_index, array)


def insertion_sort(array):
    N = len(array)
    for i in range(1, N):
        key = array[i]
        j = i
        while j > 0 and key < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = key


def bubble_sort(array):
    N = len(array)
    for i in range(N):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                swap(j, j+1, array)


# Quick sort

def parition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(i, j, array)

    swap(i+1, high, array)

    return i + 1


def quick_sort_inner(array, low, high):
    if low < high:
        pi = parition(array, low, high)
        quick_sort_inner(array, low, pi-1)
        quick_sort_inner(array, pi+1, high)


def quick_sort(array):
    start = 0
    end = len(array) - 1
    quick_sort_inner(array, start, end)


# merge sort

def merge_sort(array):
    if len(array) > 1:
        mid = (len(array))//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)
        
        array = merge(L,R)    
        



def merge(c1, c2):
    i = len(c1) - 1
    j = len(c2) - 1
    k = i + j + 1
    array = [0]*(k+1)


    while k >= 0:
        if (c1[i] > c2[j] or j == 0) and i >= 0:
            array[k] = c1[i]
            i -= 1
        else:
            array[k] = c2[j]
            j -= 1
        k -=1

    return array



def linear_search(array, value):
    N = len(array)
    for i in range(N):
        if value == array[i]:
            return i
    return -1


def binary_search(sorted_array, value):
    # In ascending order
    start = 0
    end = len(sorted_array)-1

    while start <= end:
        mid = (start+end)//2

        if sorted_array[mid] == value:
            return mid

        elif value > sorted_array[mid]:
            start = mid + 1

        else:
            end = end - 1

    return -1


def swap(a, b, array):
    # temp = array[a]
    # array[a] = array[b]
    # array[b] = temp
    
    (array[b], array[a]) = (array[a], array[b])


def genarate_list(n):
    return [random.randint(1, 1000) for _ in range(n)]


def main():
    a = genarate_list(10)
    b = genarate_list(10)

    start = time.time()
    test = merge(a, b)
    end = time.time()
    print(f"{(end - start):.2f}")
    print(test)




if __name__ == "__main__":
    main()
