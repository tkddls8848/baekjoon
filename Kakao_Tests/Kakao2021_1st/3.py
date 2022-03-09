from collections import defaultdict

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info, query):
    answer = []
    data = []
    data.append(["cpp", "java", "python"])
    data.append(["backend", "frontend"])
    data.append(["junior", "senior"])
    data.append(["chicken", "pizza"])
    print(data)
    dic = defaultdict()
    dic_score = defaultdict()
    for _ in info:
        tmp = list(map(str, _.split(" ")))
        tmp, score = tmp[:-1], int(tmp[-1])
        dic_score.setdefault(score, [])
        dic_score[score].append(info.index(_))
        for t in tmp:
            dic.setdefault(t, [])
            dic[t].append(info.index(_))



    print(dic)
    print(dic_score)
    for q in range(len(query)):
        tmp = list(map(str, query(q).split(" ")))
        tmp, score = tmp[:-1], int(tmp[-1])
        tmp_dic = defaultdict()
        score_dic = defaultdict()
        tmp_dic.setdefault(tmp, [])
        score_dic.setdefault(score, [])
        


    return answer

print("FINAL",solution(info, query))