money = 4578
costs = [1, 4, 99, 35, 50, 1000]	##result2308

money = 1999
costs = [2, 11, 20, 100, 200, 600]	##result2798
import copy

def solution(money, costs):
    price = [1, 5, 10, 50, 100, 500]
    cost_DP = [0] * (money + 1)
    cost_DP[1] = 1
    ##cost_DP[4578] = min(cost_DP[4578-500]+1000, cost_DP[4578-100]+50, cost_DP[4578-50] + 35 ......)
    for test in range(1, money+1):
        tmp = []
        for c in range(len(costs)):
            #print("BEFORE", test, price[c], test - price[c], costs[c])
            if (test - price[c]) >= 0:
                #print("AFTER", test, price[c], test - price[c], costs[c])
                tmp.append(cost_DP[test - price[c]] + costs[c])
        cost_DP[test] = min(tmp)
    print(cost_DP)
    return 0

print("FINAL", solution(money, costs))
