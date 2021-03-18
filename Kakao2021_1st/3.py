info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def solution(info, query):
    answer = []
    database = []
    for i in info:
        tmp = [True] + list(map(str, i.split(" ")))
        database.append(tmp)

    for q in query:
        sql = [" "] + list(map(str, q.split(" ")))
        sql.remove('and')
        sql.remove('and')
        sql.remove('and')

        for data in database:

            cnt = 1
            while not cnt == 5:

                if not sql[cnt] == '-':
                    if not data[cnt] == sql[cnt]:
                        data[0] = False
                        break
                cnt += 1
            if not (data[0] and int(data[5]) >= int(sql[5])):
                data[0] = False
        ans = 0
        for d in database:
            if not d[0]:
                d[0] = True
            else:
                ans += 1
        answer.append(ans)

    return answer

print("FINAL",solution(info, query))