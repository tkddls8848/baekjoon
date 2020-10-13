N = 10
DP = [0] * (N+1)
Time = [1,1,1,1,1,1,1,1,1,1]
Price = [1,2,3,4,5,6,7,8,9,10]
"""
Time = [5,5,5,5,5,5,5,5,5,5]
Price = [10,9,8,7,6,10,9,8,7,6]
Time = [5,5,5,5,5,5,5,5,5,5]
Price = [10,9,8,7,6,10,9,8,7,6]
Time = [3,5,1,1,2,4,2]
Price = [10,20,10,20,15,40,200]
##f(n) = f((n-1)Time=1)+f((n-2)Time=2)+...
"""
def quit(N):
    for i in range(0, N):
        if (i+Time[i]) <= N:
            DP[i+Time[i]] = DP[i]+Price[i]
            print(DP,Price[i],Time[i])
    print(DP[-1])

quit(N)