board = [[1,0,0,0,0],[2,0,0,0,0],[2,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]]
moves = [1,1,1]

def solution(board, moves):
    answer = 0
    stack = ['start']
    for _ in moves:
        move = _-1
        for i in range(len(board)):
            print(move,i,stack)
            if not board[i][move] == 0:
                if not stack[-1] == board[i][move]:
                    stack.append(board[i][move])
                    board[i][move] = 0
                    break
                else:
                    stack.pop()
                    answer += 2
                    board[i][move] = 0
                    break
    print(stack)
    for _ in board:
        print(_)
    return answer

print(solution(board, moves))