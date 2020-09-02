def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n+3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_90(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        print(x,y,i,j, len(new_lock))
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

#90도 회전
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def check(new_lock):
    lock_lenth = len(new_lock)//3
    for i in range(lock_lenth, lock_lenth*2):
        for j in range(lock_lenth, lock_lenth*2):
            if new_lock[i][j] !=1:
                return False
    return True

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))