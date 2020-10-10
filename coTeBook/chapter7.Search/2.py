arr = [8,5,7,9,1,4,16,12,39,26,32]
array = sorted(arr)

def binary_search(arr, start, end, target):
    middle = (start + end) // 2
    if target > array[middle]:
        binary_search(arr, middle+1,end,target)
    elif target < array[middle]:
        binary_search(arr, start, middle-1,target)
    elif target == array[middle]:
        for i in range(len(arr)):
            if arr[i] == array[middle]:
                print(i+1)
        return array[middle]

binary_search(arr,0,len(arr)-1,7)
