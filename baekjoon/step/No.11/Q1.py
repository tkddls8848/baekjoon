'''
5 21
5 6 7 8 9
'''
from itertools import combinations

n, target = list(map(int, input().split()))
cards = list(map(int, input().split()))
nominee = 0
for c in combinations(cards,3):
    if sum(c) < target:
        nominee = max(sum(c), nominee)
    elif sum(c) > target:
        continue
    elif sum(c) == target:
        nominee = sum(c)
        break
print(nominee)