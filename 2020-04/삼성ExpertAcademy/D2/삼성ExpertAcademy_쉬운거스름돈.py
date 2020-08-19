def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        money = input()
        money = int(money)

        a50000 = 0
        a10000 = 0
        a5000 = 0
        a1000 = 0
        a500 = 0
        a100 = 0
        a50 = 0
        a10 = 0

        while True:
            if money/50000 >= 1:
                a50000 += 1
                money = money - 50000
            else:
                break
        while True:
            if money/10000 >= 1:
                a10000 += 1
                money = money - 10000
            else:
                break
        while True:
            if money/5000 >= 1:
                a5000 += 1
                money = money - 5000
            else:
                break
        while True:
            if money/1000 >= 1:
                a1000 += 1
                money = money - 1000
            else:
                break
        while True:
            if money/500 >= 1:
                a500 += 1
                money = money - 500
            else:
                break
        while True:
            if money/100 >= 1:
                a100 += 1
                money = money - 100
            else:
                break
        while True:
            if money/50 >= 1:
                a50 += 1
                money = money - 50
            else:
                break
        while True:
            if money/10 >= 1:
                a10 += 1
                money = money - 10
            else:
                break



        print ("#"+str(test_case))
        print (a50000,a10000,a5000,a1000,a500,a100,a50,a10)
soltion()
