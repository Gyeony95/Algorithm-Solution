def solution(key, lock):

    #모든 경우의 수를 포함 할 수 있게 배열 크기를 9배로 늘림
    arr = [[0] * len(lock)*3 for _ in range(len(lock)*3)]

    #배열 가운데에 원래 배열 넣음
    for i in range(len(lock),len(lock)*2,1):
        for j in range(len(lock),len(lock)*2,1):
            arr[i][j] = lock[i-len(lock)][j -len(lock)]
    for m in range(4):
        key = rotate(key)
        for i in range(len(lock)*2):
            for j in range(len(lock)*2):
                for x in range(len(key)):
                    for y in range(len(key[0])):
                        arr[i+x][j+y] = arr[i+x][j+y] + key[x][y]
                if check(arr):
                    return True
                else:
                    for x in range(len(key)):
                        for y in range(len(key[0])):
                            arr[i+x][j+y] = arr[i+x][j+y] - key[x][y]

    return False

def check(new_lock):
    lock_lenth = len(new_lock)//3
    for i in range(lock_lenth, lock_lenth*2):
        for j in range(lock_lenth, lock_lenth*2):
            if new_lock[i][j] !=1:
                return False
    return True


def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))