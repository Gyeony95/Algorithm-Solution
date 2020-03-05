
def soltion():
    T = int(input())
    answer = "1"
    for test_case in range(2, T + 1):
        k = list(str(test_case))
        clap= 0

        for i in range(0, len(k), 1):
            #print (int(k[i]),int(k[i]) %3)
            if int(k[i]) %3 == 0 and int(k[i]) != 0:
                clap += 1
        if clap == 0:
            answer = answer+" "+str(test_case)
        else :
            answer = answer +" "
            for kk in range(0, clap, 1):
                answer = answer+"-"

    print(answer)
soltion()




