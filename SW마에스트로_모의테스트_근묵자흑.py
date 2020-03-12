def solution():
    N, K = input().split()
    K = int(K)
    mArr = input().split()
    count = 1

    for i in range(K):
        mArr.pop()

    while True:
        if len(mArr) >= K-1:
            count += 1
            for j in range(K-1):
                mArr.pop()
        elif len(mArr) == 0:
            break
        else:
            count += 1
            break
    print(count)

solution()
