def solution(board, h, w):
    answer = 0
    keyword = board[h][w]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    for dh, dw in directions:
        nh, nw = h + dh, w + dw
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]) and board[nh][nw] == keyword:
            answer += 1

    return answer


board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]]

print(solution(board, 1, 2))