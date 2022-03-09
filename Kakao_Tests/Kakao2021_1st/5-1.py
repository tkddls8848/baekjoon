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
def solution(play_time, adv_time, logs):

    new_play_time = strToTime(play_time)
    new_adv_time = strToTime(adv_time)
    DP = [0 for i in range(strToTime(play_time))]
    ini_DP = []
    data_str = []
    data_int = []
    for l in logs:
        li = list(map(str, l.split("-")))
        data_str.append(li)
    print(data_str)
    for data in data_str:
        tmp = []
        for _ in data:
            tmp.append(strToTime(_))
        for i in range(tmp[0], tmp[1]):
            DP[i] += 1
        data_int.append(tmp)
    print(data_int)
    ini_adv = 0
    if not new_play_time == new_adv_time:
        for i in range(1, new_play_time - new_adv_time):
            ini_adv -= DP[i]
            ini_adv += DP[i+new_adv_time]
            ini_DP.append(ini_adv)
        print(ini_DP)
        print(ini_DP.index(max(ini_DP)))
        cnt = ini_DP.index(max(ini_DP))
        return timeToStr(cnt+2)
    else:
        return "00:00:00"
def strToTime(str):
    l = list(map(int, str.split(':')))
    return l[0]*3600 + l[1]*60 + l[2]

def timeToStr(int):
    return '{0:02d}:{1:02d}:{2:02d}'.format(int // 3600,(int % 3600)//60,(int % 3600)%60)

solution(play_time,adv_time,logs)