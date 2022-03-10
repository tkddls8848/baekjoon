##begin = "hit"
##target = "cog"
##words = ["hot", "dot", "dog", "lot", "log", "cog"]
##words = ["hot", "dot", "dog", "lot", "log"]

begin = "hit" ## answer 1
target = "hot"
words = ["hit", "hot", "lot"]
from collections import deque

def solution(begin, target, words):
    answer = []
    visited = [False] * len(words)
    nominee = []
    depth = 1
    word_length = len(begin)
    for word in words:
        cnt = 0
        for c, w in zip(begin, word):
            if c == w:
                cnt += 1
        if cnt == word_length - 1:
            nominee.append([word, depth])
            visited[words.index(word)] = False
        elif cnt == word_length:
            answer.append(depth)
    while nominee:
        current_word, current_depth = nominee.pop()
        depth = current_depth + 1
        print(current_word, current_depth, nominee)
        for word in words:
            cnt = 0
            for c, w in zip(current_word, word):
                if c == w:
                    cnt += 1
            if cnt == word_length - 1 and visited[words.index(word)] == False:
                if word == target:
                    print("TARGET", word, current_depth+1, nominee)
                    answer.append(depth)
                    break
                visited[words.index(word)] = True
                nominee.append([word, current_depth+1])
    print(answer)
    if len(answer) == 0:
        return 0
    else:
        return min(answer)


print("FINAL", solution(begin, target, words))