enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

import math
from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    referral_dic = defaultdict(int)
    seller_income = defaultdict(int)

    for e, r in zip(enroll, referral):
        referral_dic[e] = r
        seller_income[e] = 0
    for s, a in zip(seller, amount):
        find(referral_dic, s, a*100, seller_income)
    for s in seller_income.values():
        answer.append(s)
    print(referral_dic,seller_income)
    print(answer)
    return answer

def find(referral_dic, seller, money, seller_income):
    referral_fee = math.floor(money / 10)
    net_income = money - referral_fee
    seller_income[seller] += net_income
    print(referral_fee, net_income)
    if not referral_dic[seller] == "-" and not referral_fee == 0:
        find(referral_dic, referral_dic[seller], referral_fee, seller_income)

solution(enroll, referral, seller, amount)