money = 5
costs = [2, 11, 20, 100, 200, 600]
##2798


def solution(money, costs):
    answer = 0
    price = [500,100,50,10,5,1]
    tmp_queue = []
    result_queue = []
    for i in range(len(price)):
        tmp_count = [0,0,0,0,0,0]
        money -= price[i]
        if money >= 0:
            tmp_count[i] += 1
            tmp_queue.append([money, tmp_count])
        money += price[i]
    tmp = tmp_queue.pop()
    cur_m, cur_c = tmp[0], tmp[1]
    while tmp_queue:
        for i in range(len(price)):
            next_m = cur_m - price[i]
            cur_c[i] += 1
            next_c = cur_c

            if next_m > 0:
                tmp_queue.append([next_m, next_c])
                print(tmp_queue)

            elif next_m == 0:
                result_queue.append([next_m,next_c])
            else:
                continue
    print(result_queue)



    return answer

print("FINAL", solution(money, costs))