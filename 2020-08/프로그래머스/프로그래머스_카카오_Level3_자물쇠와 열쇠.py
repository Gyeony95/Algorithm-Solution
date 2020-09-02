def solution(key, lock):
    key_90 = rotate_90(key)
    key_180 = rotate_180(key)
    key_270 = rotate_270(key)
    global answer_0
    global answer_90
    global answer_180
    global answer_270
    answer_0 = True
    answer_90 = True
    answer_180 = True
    answer_270 = True

    arr = [[9] * len(lock)*3 for _ in range(len(lock)*3)]


    for i in range(len(lock),len(lock)*2,1):
        for j in range(len(lock),len(lock)*2,1):
            arr[i][j] = lock[i-len(lock)][j -len(lock)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(key)):
                for x in range(len(key)):
                    if arr[i][j] == 0 and key[k][x] == 1:
                        pass
                    else:
                        answer_0 = False
                    if arr[i][j] == 0 and key_90[k][x] == 1:
                        pass
                    else:
                        answer_90 = False
                    if arr[i][j] == 0 and key_180[k][x] == 1:
                        pass
                    else:
                        answer_180 = False
                    if arr[i][j] == 0 and key_270[k][x] == 1:
                        pass
                    else:
                        answer_270 = False
                print(answer_0,answer_90,answer_180,answer_270)
            if answer_0:
                return answer_0
            if answer_90:
                return answer_90
            if answer_180:
                return  answer_180
            if answer_270:
                return answer_270
            answer_0 = True
            answer_90 = True
            answer_180 = True
            answer_270 = True
    return False


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret

def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))