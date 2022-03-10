##tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]

from collections import deque

def solution(tickets):
    answer = []
    course = []
    tickets.sort()
    q = deque()
    used_ticket = [False for x in range(len(tickets))]
    for ticket in tickets:
        tmp = used_ticket
        if ticket[0] == "ICN":
            tmp[tickets.index(ticket)] = True
            q.append([ticket, tmp])
            tmp[tickets.index(ticket)] = False
            print(q)
            course.append(ticket)
    while q:
        print(q)
        tmp = q.pop()
        start, end, route = tmp[0][0], tmp[0][1], tmp[1]
        print("tmp", start, end, route)
        for ticket in tickets:
            if end == ticket[0] and route[tickets.index(ticket)] == False:
                route[tickets.index(ticket)] = True
                q.appendleft([[start, end], route])





    return answer

print("FINAL", solution(tickets))