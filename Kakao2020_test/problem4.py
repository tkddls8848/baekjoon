'''
1.글자 길이에 맞는 문자열만 남긴다
2.검색문의 접미 혹은 접두의 길이를 이분탐색으로 범위탐색한다
3-1.나머지 검색문이 접미어일떄 뒤어서부터 한글자씩 탐색문에서 제외해나간다.while
3-2.나머지 검색문을 첫글자부터 앞에서부터 한글자씩 탐색문에서 제외해나간다.while
'''
from collections import deque
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
def solution(words, queries):
    answer = []
    nominee = deque()
    nominee2 = []
    ##queries중 한글자에 대해서 검색
    for a in range(len(queries)):
        query = queries[a]
        print(query)
        prefix_hidden = False
        surfix_hidden = False
        if query[0] == '?':
            prefix_hidden = True
        else:
            surfix_hidden = True
        ##1.글자 길이에 맞는 문자열만 남긴다
        for _ in words:
            if len(query) == len(_):
                nominee.append(_)
        ##2.검색문의 접미 혹은 접두의 길이를 이분탐색으로 범위설정
        position = search(query) + 1
        search_position = []
        if surfix_hidden:
            search_position.append(1)
            search_position.append(position-1)
        elif prefix_hidden:
            search_position.append(position+1)
            search_position.append(len(query))
        print(nominee, search_position)
        ##3-1.나머지 검색문이 접미어일떄 뒤어서부터 한글자씩 탐색문에서 제외해나간다.while
        ##3-2.나머지 검색문을 첫글자부터 앞에서부터 한글자씩 탐색문에서 제외해나간다.while
        while nominee:
            test = nominee.popleft()
            for i in range(search_position[0]-1,search_position[1]):
                if not test[i] == query[i]:
                    print(_,query,'incorrect')
                else:
                    print()





        answer.append(len(nominee))
        nominee.clear()
        print(answer)
    return answer


def search(word):
    start, end = 0, len(word)
    pivot = 0
    if word[start] == '?':
        for i in range(0, end-1):
            if not word[i+1] == '?':
                pivot = i
                break
    else:
        for i in range(0, end-1):
            if word[i+1] == '?':
                pivot = i+1
                break
    return pivot

solution(words, queries)