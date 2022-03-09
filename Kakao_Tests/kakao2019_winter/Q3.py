from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

def isMatch(user_id, banned_id):
    for i in range(len(user_id)):
        if not len(user_id[i]) == len(banned_id[i]):
            return False
        else:
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == '*':
                    continue
                elif not banned_id[i][j] == user_id[i][j]:
                    return False
    return True

def solution(user_id, banned_id):
    answer = []
    for per in permutations(user_id, len(banned_id)):
        if isMatch(per, banned_id):
            per = set(per)
            if per not in answer:
                answer.append(per)
    return len(answer)


solution(user_id, banned_id)
