n = 8
arr = [1,3,1,8,2,6,3,7]
DP = [0] * (n+1)

def raid(arr):
    total = 0
    DP[1] = arr[0]
    DP[2] = max(arr[0], arr[1])
    for i in range(len(arr)):
        DP[i+1] = max(DP[i-2]+arr[i], DP[i-1])
    print(DP[len(DP)-1])

raid(arr)
print(DP)



