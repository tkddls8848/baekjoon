"""
n = input()
arr = []

for _ in range(int(n)):
    data = input().split(' ')
    arr.append(data)
print(arr)
"""
arr = [['학생1', 6], ['학생2', 11], ['학생3', 7], ['학생4', 2], ['학생5', 8]]

arr = sorted(arr, key=lambda arr:arr[1])
print(arr)
"""
def quick_sort(arr):
    if len(arr) <= 1:
        print('array',arr)
        return arr
    pivot = arr[0]
    tail = arr[1:]
    less, more = [], []
    for i in tail:
        if i[1] < pivot[1]:
            less.append(i)
        elif i[1] > pivot[1]:
            more.append(i)
    print('l',less, 'p',pivot, 'm',more)
    return quick_sort(less) + [pivot] + quick_sort(more)

print(quick_sort(arr))
"""

