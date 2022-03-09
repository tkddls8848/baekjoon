bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque(list(0 for x in range(bridge_length)))
    time = 0
    bridge_sum = 0
    while bridge:
        time += 1
        tmp = bridge.popleft()
        bridge_sum -= tmp
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                tmp = truck_weights.pop(0)
                bridge_sum += tmp
                bridge.append(tmp)
            else:
                bridge.append(0)
        else:
            if bridge_sum == 0:
                break
        print(bridge, time, truck_weights)
    print(time)
    return time

solution(bridge_length, weight,truck_weights)