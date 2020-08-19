def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        n = int(input())
        if n %2 == 0:
            print(printString,"Even")
        else:
            print(printString, "Odd")


soltion()