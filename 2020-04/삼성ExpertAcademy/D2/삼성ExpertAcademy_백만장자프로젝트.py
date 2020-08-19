#실패한코드, 테스트 10개중 9개맞음 1개 런타임에러인데 왜인지 모르겠음

def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n = input()
        mArr = input().split()
        answer = 0
        buy = 0
        max = mostCase(mArr, 0)
        for i in range(len(mArr)):
            if int(mArr[i]) != max:
                buy = buy + 1
                answer = answer - int(mArr[i])
            else:
                answer = answer + int(mArr[i]) * buy
                buy = 0
                max = mostCase(mArr, i + 1)

        print ("#"+str(test_case),answer)
def mostCase(arr,a):
    max = 0
    for i in range(a,len(arr),1):
        if int(arr[i]) > max:
            max = int(arr[i])
    return max
soltion()
