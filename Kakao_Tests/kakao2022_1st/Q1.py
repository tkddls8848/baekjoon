id_list = ["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2 #answer[2,1,1,0]

def solution(id_list, report, k):
    answer = []
    dic_reporting = {}
    dic_reported = {}
    for id in id_list:
        dic_reported[id] = []
        dic_reporting[id] = []
    for r in report:
        tmp = r.split(' ')
        dic_reporting[tmp[0]].append(tmp[1])
        dic_reported[tmp[1]].append(tmp[0])
    black_list = []
    print(dic_reporting, dic_reported)
    for d in dic_reported:
        tmp = set(dic_reported[d])
        cnt = 0
        for t in tmp:
            cnt += 1
            print(t)
        if cnt >= k:
            black_list.append(d)
    print(black_list)
    for d in dic_reporting:
        tmp = set(dic_reporting[d])
        letter_time = 0
        for t in tmp:
            if black_list.count(t) >= 1:
                letter_time += 1
        answer.append(letter_time)
    print(answer)
    return answer

print("FINAL", solution(id_list,report,k))