'''
12
Junkyu 50 60 100
Sangdeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 90
nsj 80 80 80
Taewhan 50 60 90
국 내림, 영 오름, 수 내, 이름 사전순 오름
'''

n = int(input())
scorelist = []
for i in range(n):
    scorelist.append(list(input().split()))

scorelist.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for _ in scorelist:
    print(_)