import random
import string

def gen_rand_arr(n):
    return [random.randint(1, 100) for _ in range(n)]


# in acs
def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                (arr[j+1], arr[j]) = (arr[j], arr[j+1])


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                (arr[j], arr[j-1]) = (arr[j-1], arr[j])
            j -= 1


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[min_i] > arr[j]:
                min_i = j
        (arr[i], arr[min_i]) = (arr[min_i], arr[i])
        
def linear_search(arr, val):
    n = len(n)

    for i in range(n):
        if arr[i] == val:
            return i
    return -1

def binary_search(arr, val):
    n = len(arr)
    s = 0
    e = n-1

    while s <= e:
        m = (s + e)//2

        if arr[m] == val:
            return m

        elif arr[m] > val:
            e = m - 1

        else:
            s = m + 1
    return -1


    
arr = [2, 4, 3, 1, 2, 9]
print(arr)

i = binary_search(arr, 9)
print(i)
