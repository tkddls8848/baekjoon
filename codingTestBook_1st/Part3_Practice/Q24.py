'''
4
5 1 7 9
'''

n = int(input())
homelist = list(map(int, input().split()))
homelist.sort()

print('answer',homelist[(n-1)//2])



