k = 10
room_number = [1,3,4,1,3,1]

def solution(k, room_number):
    answer = []
    room = [False for i in range(k)]
    print(room)
    for i in range(len(room_number)):
        print(room_number[i])
        if not room[room_number[i]]:
            room[room_number[i]] = True
            answer.append(room_number[i])
        else:
            print('occupy')
            cnt = room_number[i]
            while room[cnt]:
                cnt += 1
            print('cnt',cnt)
            room[cnt] = True
            answer.append(cnt)
    print(room)
    print(answer)
    return answer

solution(k, room_number)