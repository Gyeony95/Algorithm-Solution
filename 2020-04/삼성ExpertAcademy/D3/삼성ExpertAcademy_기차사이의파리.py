def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        d,a,b,f = map(int, input().split())
        count = 0
        while(True):
            if a+b <= d:
                count += 1
                d = d - (a+b)
            else:
                break

        answer = f*count +d/(a+b) * f



        print("#" + str(test_case), '%.10f' % answer)
soltion()
