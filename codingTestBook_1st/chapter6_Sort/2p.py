"""
n = input()

arr = []
for _ in range(int(n)):
    arr.append(input())
"""
arr = [8,5,7,9,1,4]

def select_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            print(arr)
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print()
    print(arr)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    less_pivot, more_pivot = [],[]
    for i in arr:
        if i < pivot:
            less_pivot.append(i)
        elif i > pivot:
            more_pivot.append(i)
    return quick_sort(less_pivot) + [pivot] + quick_sort(more_pivot)



def count_sort(arr):
    counter = [0] * max(arr)

    for _ in arr:
        counter[_-1] += 1
    print(counter)
    for i in range(len(counter)):
        while not counter[i] == 0:
            print(i+1, end=' ')
            counter[i] -= 1
count_sort(arr)