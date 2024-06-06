def solution(board, h, w):
    answer = 0
    keyword = board[h][w]
    if h != 0:
        if board[h - 1][w] == keyword:
            answer = answer + 1
    if h != (len(board) - 1):
        if board[h + 1][w] == keyword:
            answer = answer + 1
    if w != 0:
        if board[h][w - 1] == keyword:
            answer = answer + 1
    if w != (len(board[h]) - 1):
        if board[h][w + 1] == keyword:
            answer = answer + 1
    return answer


board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]

print(solution(board, 1,2))