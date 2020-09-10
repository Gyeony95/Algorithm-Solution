#100점
def solution(n):
    answer = []
    data = [[0]*n for _ in range(n)]

    x = -1
    y = -1
    num = 0
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x +=1
                y +=1
            elif i % 3 == 1:
                y -=1
            elif i % 3 == 2:
                x -=1

            num +=1
            data[x][y] = num
    for i in range(n):
        for j in range(n-1, -1, -1):
            if data[i][j] != 0:
                answer.append(data[i][j])
    return answer



print(solution(5))
