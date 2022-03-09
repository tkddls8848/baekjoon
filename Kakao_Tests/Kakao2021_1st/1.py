new_id = input()
def solution(new_id):
    answer = ''
    ## 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    stage1 = ''
    for _ in new_id:
        stage1 += _.lower()

    ## 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    checklist = list("abcdefghijklmnopqrstuvwxyz0123456789-_.")

    stage2 = ''
    for _ in stage1:
        if not checklist.count(_) == 0:
            stage2 += _
    ##print(2,stage2)

    ## 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    stage3 = ''
    tmp1 = ''
    tmp2 = ''
    for _ in stage2:
        tmp2 = tmp1
        tmp1 = _

        ##print(tmp1,tmp2)
        if tmp1 == '.' and tmp2 == '.':
            continue
        else:
            stage3 += tmp2
    stage3 += tmp1

    ##print(3, stage3)
    ## 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    stage4 = ''
    if stage3[0] == '.':
        stage3 = stage3[1:]
    if not stage3 == '' and stage3[-1] == '.':
        stage3 = stage3[0:-1]
    stage4 = stage3
    ##print(4,stage4)

    ## 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    stage5 = ''
    if stage4 == '':
        stage5 += 'a'
    else:
        stage5 = stage4
    ##print(5,stage5)
    ## 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    ##      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    stage6 = ''
    if len(stage5) >= 16:
        stage6 = stage5[0:15]
        if stage6[-1] == '.':
            stage6 = stage6[0:-1]
    else:
        stage6 = stage5
    ##print(6, stage6)
    ## 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    stage7 = ''
    if len(stage6) <= 2:
        tmp = stage6[-1]
        stage7 = stage6
        while not len(stage7) == 3:
            stage7 += tmp
    else:
        stage7 = stage6
    ##print(7, stage7)
    answer = stage7
    ##print(answer)
    return answer
