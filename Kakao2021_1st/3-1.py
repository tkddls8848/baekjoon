

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info, query):
    answer = []
    info_dic = {}
    info_dic_num = {}
    for _ in info:
        l = _.split(" ")
        tmp = 1
        for _ in l[:-1]:
            info_dic[_] = tmp
            tmp += 1
        l[-1:]
    return answer

solution(info, query)