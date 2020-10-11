n = 99
memo = [0] * (n+1)
memo_b = [0] * (n+1)


def fibo_topdown(n):
    if n == 1 or n == 2:
        return 1
    if not memo[n] == 0:
        return memo[n]

    memo[n] = fibo_topdown(n - 1) + fibo_topdown(n - 2)
    return memo[n]

def fibo_bottomUp(n):
    memo_b[1], memo_b[2] = 1,1
    for i in range(3,n+1):
        memo_b[i] = memo_b[i-1] + memo_b[i-2]
    return memo_b[n]


print(fibo_topdown(n))
print(fibo_bottomUp(n))