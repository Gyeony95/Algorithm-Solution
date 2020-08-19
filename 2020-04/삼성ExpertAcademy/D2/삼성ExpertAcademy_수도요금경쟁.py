def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        p,q,r,s,w = map(int, input().split())

        first = p*w
        second = q
        if w<r:
            pass
        else:
            second = second + (w-r)*s

        if first > second:
            print("#"+str(test_case),second)
        else:
            print("#" + str(test_case), first)



soltion()
