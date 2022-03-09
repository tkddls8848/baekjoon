'''
play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
'''
play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
'''
play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
'''
def correction(li):
    tmp = 3600*int(li[0]) + 60*int(li[1]) + (int(li[2]))
    return tmp

def re_correction(num):
    tmp = ""
    num1 = num//3600
    str1 = num%3600
    num2 = str1//60
    str2 = str1%60
    num3 = str2
    str3 = num3
    if num1 < 10:
        num1 = "0"+str(num1)
    if num2 < 10:
        num2 = "0"+str(num2)
    if num3 < 10:
        num3 = "0"+str(num3)
    tmp = str(num1)+':'+str(num2)+':'+str(num3)
    return tmp

def solution(play_time, adv_time, logs):
    answer = ""
    new_play_time = correction(play_time.split(':'))
    new_adv_time = correction(adv_time.split(':'))
    new_logs = []
    for _ in logs:
        tmp=_.split('-')
        tmp1 = []
        for t in tmp:
            tmp1.append(correction(t.split(':')))
        new_logs.append(tmp1)
    DP = [0] * int(new_play_time)
    print(new_adv_time,new_adv_time,new_logs)
    for _ in new_logs:
        tmp = _[0]
        while not tmp == _[1]:
            DP[tmp] += 1
            tmp += 1
    start = 0
    end = start + new_adv_time
    for _ in new_logs:
        for i in range(_[0], _[1]):
            DP[i] += 1
    print(DP)
    tmp = 0
    for i in range(start, end):
        tmp += DP[i]
    print(tmp)
    tmp = 0
    start = 1
    end = start + new_adv_time
    for i in range(start, end):
        tmp += DP[i]
    print(tmp)
    return answer

print(solution(play_time, adv_time, logs))