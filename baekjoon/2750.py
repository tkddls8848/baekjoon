arr = [5,2,4,3,1,9,7,6,8]

def selectSort():
    for i in range(0,len(arr)):
        pos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                pos = j
                print(arr[j])
        arr[i], arr[pos] = arr[pos], arr[i]
        print(arr)

selectSort()

before = [5,2,4,3,1,9,7,6,8]
after = []

def insertSort():
    for j in range(0, len(before)):
        pivot = before[j]
        after.append(pivot)
        for i in range(0, len(after)-1):
            if after[i] > after[len(after)-1]:
                after[i], after[len(after)-1] = after[len(after)-1], after[i]
                break
                print(after)

insertSort()