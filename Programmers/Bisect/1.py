n=10
times = [3,8,3,6,9,2,4]
'''
1. 전체인원//창구 수가 지난 후의 창구에 따른 총 처리 예상 인원
2-1. 예상 인원이 오버일 경우 high = mid - 1로 놓고 다시 1로
2-2. 예상 인원이 언더일 경우 start = mid + 1로 놓고 다시 1로
'''
def solution(n, times):
    answer = 0
    times.sort()
    start, end = 1, n * times[-1]
    while start <= end:
        total_cnt = 0
        mid = (start+end)//2
        for _ in times:
            total_cnt += mid//_
            if total_cnt >= n:
                end = mid - 1
                answer = mid
                break
        if total_cnt < n:
            start = mid + 1
    return answer

solution(n,times)