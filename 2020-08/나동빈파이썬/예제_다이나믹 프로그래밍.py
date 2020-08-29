#피보나치 수열로 보는 다이나믹 프로그래밍 (메모이제이션)
#큰문제를 해결하기위해 작은문제를 저장하고호출하는 탑다운 방식
d = [0] * 100

def fibo1(x):
    if x ==1 or x ==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo1(x-1) + fibo1(x-2)
    return d[x]



#반복문을 사용하여 작은 문제부터 차근차근 답을 도출하는 바텀업 방식

def fibo2(x):
    d[1] = 1
    d[2] = 1
    n = 99
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    print(d[n])