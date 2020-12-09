'''
72
1122223

74
1122223

73
1234567
'''
space = ' '
n, x = map(int, space.join(input().split()))
arr = list(map(int, space.join(input().split())))

def first(arr, target, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target and arr[mid - 1] < target:
        return mid
    elif arr[mid] < target:
        return first(arr,target,mid+1,end)
    else:
        return first(arr,target,start,mid-1)

def last(arr,target,start,end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == target and arr[mid +1] > target:
        return mid
    elif arr[mid] > target:
        return last(arr, target, start,mid-1)
    else:
        return last(arr, target, mid+1, end)


def len():
    if last(arr, x, 0, n-1) != -1 and first(arr, x, 0, n-1)+1 != -1:
        return last(arr, x, 0, n-1)-first(arr, x, 0, n-1)+1
    else:
        return -1

print(len())