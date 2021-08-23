

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info, query):
    answer = []
    i_dic = {}
    i_score_dic = {}
    q_dic = {}
    q_score_dic = {}
    for i in range(len(info)):
        info_dic = {}
        name = ["lang", "part", "career", "fav"]
        li= list(map(str, info[i].split(" ")))[0:-1]
        li_score = list(map(str, info[i].split(" ")))[-1]
        for l in range(len(li)):
            info_dic[name[l]] = li[l]
        i_dic[i] = info_dic
    print(i_dic)
    for q in range(len(query)):
        query_dic = {}
        name = ["lang", "part", "career", "fav"]
        li = list(map(str, query[q].split(" and ")))
        for l in range(len(li)):
            query_dic[name[l]] = li[l]
        q_dic[q] = query_dic
    print(q_dic)

    return answer

solution(info, query)