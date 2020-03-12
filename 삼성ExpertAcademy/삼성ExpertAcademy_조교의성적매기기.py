
def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n, k = input().split()
        n = int(n)
        k = int(k)
        grade = []
        answer = []
        score = 0
        for mCase in range(1, n + 1,1):
            a, b, c = input().split()
            a = int(a)
            b = int(b)
            c = int(c)
            grade.append(a * 35 + b * 45 + c * 20)
            answer.append(a * 35 + b * 45 + c * 20)
        grade.sort(reverse = True)
        for mCase in range(1, n + 1,1):
            if answer[k - 1] == grade[mCase - 1]:
                score = mCase
                break
        mGrade = n / 10
        mAnswer = "#"+str(test_case)
        if score / mGrade <=1:
            mAnswer = mAnswer+" A+"
        elif score / mGrade>1 and score / mGrade<=2:
            mAnswer = mAnswer+" A0"
        elif score / mGrade>2 and score / mGrade<=3:
            mAnswer = mAnswer+" A-"
        elif score / mGrade>3 and score / mGrade<=4:
            mAnswer = mAnswer+" B+"
        elif score / mGrade>4 and score / mGrade<=5:
            mAnswer = mAnswer+" B0"
        elif score / mGrade > 5 and score / mGrade <= 6:
            mAnswer = mAnswer+" B-"
        elif score / mGrade > 6 and score / mGrade <= 7:
            mAnswer = mAnswer+" C+"
        elif score / mGrade > 7 and score / mGrade <= 8:
            mAnswer = mAnswer+" C0"
        elif score / mGrade > 8 and score / mGrade <= 9:
            mAnswer = mAnswer+" C-"
        else:
            mAnswer = mAnswer+" D0"
        print (mAnswer)


soltion()




