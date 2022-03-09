k = 100
room_number = [1,3,4,1,3,1]


def solution(k, room_number):
    answer = []
    checklist = {}

    def check_avail_room(room):
        tmp = []
        while checklist.get(room) is not None:
            tmp.append(checklist.get(room))
            room = checklist.get(room)
        print(tmp,checklist)
        for t in tmp:
            checklist[t] = room + 1
        checklist[room] = room + 1
        return room
    for r in room_number:
        answer.append(check_avail_room(r))

    return answer

print(solution(k, room_number))
