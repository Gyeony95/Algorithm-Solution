
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n = input()
        n = int(n)
        answer = 0
        for i in range(1, n+1, 1):
            if i %2 == 0:
                answer = answer - i
            else:
                answer = answer + i
        print("#"+str(test_case)+" "+str(answer))


soltion()




