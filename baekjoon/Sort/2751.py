arr = [5,7,9,0,3,6,1,2,4,8]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less_list, list, more_list = [],[],[]
    for i in arr:
        if i == pivot:
            list.append(i)
        elif i < pivot:
            less_list.append(i)
        elif i > pivot:
            more_list.append(i)
    return quicksort(less_list) + list + quicksort(more_list)


print(quicksort(arr))


