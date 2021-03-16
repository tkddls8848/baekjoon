from itertools import combinations
from collections import Counter

orders = 	["XYZ", "XWY", "WXA"]
course = [2,3,4]

def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            group = combinations(sorted(order), c)
            tmp += group
        counter = Counter(tmp)
        print(counter)
        for count in counter.keys():
            if len(counter) != 1 and counter.get(count) == max(counter.values()) and counter.get(count) != 1:
                string = ""
                for _ in count:
                    string += _
                    print(string, _)
                    print(list(_))
                answer.append(string)
    print('a',sorted(answer))
    return sorted(answer)

solution(orders, course)