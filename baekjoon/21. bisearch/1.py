record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    ID = {}
    final = []
    for _ in record:
        l = list(map(str, _.split(" ")))
        if l[0] == "Enter":
            ID[l[1]] = l[2]
        if l[0] == "Change":
            ID[l[1]] = l[2]
            continue
        answer.append(l[1] + " " + l[0])
##    print(ID)
    for a in answer:
        l = list(map(str, a.split(" ")))
        l[0] = ID[l[0]]
        if l[1] == "Enter":
            l[1] = "들어왔습니다."
        else:
            l[1] = "나갔습니다."
        final.append(l[0]+"님이 "+l[1])
    return final

print(solution(record))