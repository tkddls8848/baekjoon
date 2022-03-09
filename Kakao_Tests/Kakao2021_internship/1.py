def solution(s):
    answer = s
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(arr)):
        answer = answer.replace(arr[i], str(i))

    return int(answer)