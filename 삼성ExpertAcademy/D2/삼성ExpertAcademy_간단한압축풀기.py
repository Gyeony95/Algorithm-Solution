def soltion():
    T = int(input())

    for test_case in range(1, T + 1):
        print ("#"+str(test_case))
        repeat = int(input())
        answer = ""
        for i in range(repeat):
            eng, count = input().split()
            count = int(count)

            for i in range(count):
                answer = answer+eng

        answer = list(answer)
        ex_answer = ""
        print_count = 0
        for i in range(1,len(answer)+1,1):
            if i %10 ==0:
                ex_answer = ex_answer + answer[i - 1]
                print(ex_answer)
                ex_answer = ""
                print_count +=1
            else:
                ex_answer = ex_answer+answer[i-1]

        last_string = ""
        for i in range(print_count*10, len(answer),1):
            last_string = last_string+answer[i]
        print(last_string)

soltion()
