
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        answer = 1
        n = input()
        n = list(n)
        printString ="#"+ str(test_case)+ " "
        full_len = len(n) #총길이
        half_len = int(len(n)/2) #길이의 반, 길이가 홀수면 반에서 -0.5
        if full_len%2 == 0:#길이가 짝수일때
            for i in range(half_len):
                if n[i] != n[full_len-1-i]:
                    answer = 0
        else:#길이가 홀수일때
            for i in range(0, half_len+1, 1):
                if n[i] != n[full_len-1-i]:
                    answer = 0
        print(printString +str(answer))

soltion()




