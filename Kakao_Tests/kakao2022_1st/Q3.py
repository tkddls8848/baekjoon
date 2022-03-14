fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
## [14600, 34400, 5000]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
## [0, 591]

import math

def str_to_sec(s):
    arr_s = s.split(':')

    h, m = int(arr_s[0])*60, int(arr_s[1])
    return h + m

def solution(fees, records):
    answer = []
    dic_state = {}
    dic_time = {}
    dic_parking_time = {}
    dic_final_fee = {}
    for record in records:
        next_time, name, state = record.split(" ")
        dic_state[name] = ''
        dic_time[name] = ''
        dic_parking_time[name] = 0
        dic_final_fee[name] = 0
    for record in records:
        next_time, name, next_state = record.split(" ")
        current_state = dic_state[name]
        print(next_time, name, next_state, current_state)
        if current_state == '' and next_state == "IN":
            dic_state[name] = "IN"
            dic_time[name] = next_time
        elif current_state == "IN" and next_state == "OUT":
            if (str_to_sec(next_time) - str_to_sec(dic_time[name])) < 0:
                print("OVER NEXT 24", 24*60 + str_to_sec(next_time) - str_to_sec(dic_time[name]))
                dic_parking_time[name] += (str_to_sec(next_time) - str_to_sec(dic_time[name]))
            else:
                print("TIME PERIOD", str_to_sec(next_time) - str_to_sec(dic_time[name]))
                dic_parking_time[name] += (str_to_sec(next_time) - str_to_sec(dic_time[name]))
            dic_state[name] = "OUT"
            dic_time[name] = ''
        elif current_state == "OUT" and next_state == "IN":
            print("OUT and IN", dic_state, dic_time)
            dic_state[name] = "IN"
            dic_time[name] = next_time
            print("OUT and IN", dic_state, dic_time)
    print(dic_state, dic_time)
    for name in dic_state:
        if dic_state[name] == "IN":
            print("TIME PERIOD", str_to_sec("23:59") - str_to_sec(dic_time[name]))
            dic_parking_time[name] += (str_to_sec("23:59") - str_to_sec(dic_time[name]))
    print(dic_parking_time)
    for parking in dic_parking_time:
        if int(dic_parking_time[parking]) <= fees[0]:
            print("TOTAL", dic_parking_time[parking])
            dic_final_fee[parking] = fees[1]
        else:
            extra_time = (int(dic_parking_time[parking])-fees[0])
            print(extra_time)
            print("TOTAL", fees[1] + math.ceil(extra_time/fees[2])*fees[3])
            dic_final_fee[parking] = fees[1] + math.ceil(extra_time/fees[2])*fees[3]
    print(sorted(dic_final_fee.keys()))
    for _ in sorted(dic_final_fee.keys()):
        answer.append(dic_final_fee[_])
    return answer

print("FINAL", solution(fees, records))