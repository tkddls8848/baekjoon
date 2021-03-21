from itertools import combinations

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info, query):
    answer = []
    database = []
    databaseMatrix = []
    sql = []
    com = [0,1,2,3]
    for i in info:
        tmp = []
        for _ in list(map(str, i.split(" "))):
            tmp.append(_)
            print('0',tmp)
        database.append(tmp)
        for t in range(len(tmp)):
            print('1',tmp)
            tmp[t] = '-'
            database.append(tmp)

    print(database)


    for q in query:
        tmp = []
        for _ in list(map(str, q.split(" "))):
            if not _ == "and":
                tmp.append(_)
        sql.append(tmp)



    return answer

print("FINAL",solution(info, query))