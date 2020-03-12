from datetime import date

def soltion():
    T = int(input())

    for test_case in range(1, T + 1):
        mArr = list(map(int,input().split()))
        d0 = date(2019, mArr[2], mArr[3])  # date 객체1
        d1 = date(2019, mArr[0], mArr[1])  # date 객체2
        delta = d0 - d1  # 빼기
        print("#"+str(test_case),delta.days+1)
soltion()
