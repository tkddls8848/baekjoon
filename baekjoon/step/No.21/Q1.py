'''
5
4 1 5 2 3
5
1 3 7 9 5
'''

n = int(input())
list1 = list(map(int, input().split(' ')))
m = int(input())
list2 = list(map(int, input().split(' ')))

for i in range(len(list2)):
    tmp = list2[i]
    list1.sort()
    start, end = 0, len(list2)
    while True:
        mid = (start + end) // 2
        if mid >= end:
            print(0)
            break
        if list1[mid] == tmp:
            print(1)
            break
        elif list1[mid] < tmp:
            start = mid + 1
        elif list1[mid] > tmp:
            end = mid - 1



