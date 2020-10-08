arr = [5,7,9,9,3,6,1,2,4,8]

def count_sort(arr):
    cnt_arr = [0] * (max(arr)+1)
    for i in arr:
        cnt_arr[i] += 1
    print(cnt_arr)
    for j in range(len(cnt_arr)):
        for k in range(cnt_arr[j]):
            print(j, end=' ')


count_sort(arr)