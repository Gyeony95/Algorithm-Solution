def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        mTime = input().split()
        hour = int(mTime[0]) + int(mTime[2])
        minute = int(mTime[1]) + int(mTime[3])
        if minute >= 60:
            minute = minute -60
            hour = hour+1
        if hour > 12:
            hour = hour -12
        print ("#"+str(test_case),hour,minute)
soltion()
