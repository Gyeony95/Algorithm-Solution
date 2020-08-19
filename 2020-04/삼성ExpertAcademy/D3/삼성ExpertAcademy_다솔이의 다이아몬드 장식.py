def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        printString ="#"+ str(test_case)
        mString = input()
        mList = list(mString)

        s1 = ""
        for i in range(len(mList)):
            if i != len(mList)-1:#마지막문자가 아니라면
                s1 = s1+"..#."
            else:
                s1 = s1+"..#.."
        print(s1)

        s1 = ""
        for i in range(len(mList)):
            if i != len(mList) - 1:  # 마지막문자가 아니라면
                s1 = s1 + ".#.#"
            else:
                s1 = s1 + ".#.#."
        print(s1)

        s1 = ""
        for i in range(len(mList)):
            if i != len(mList) - 1:  # 마지막문자가 아니라면
                s1 = s1 + "#."+mList[i]+"."
            else:
                s1 = s1 + "#."+mList[i]+".#"
        print(s1)

        s1 = ""
        for i in range(len(mList)):
            if i != len(mList) - 1:  # 마지막문자가 아니라면
                s1 = s1 + ".#.#"
            else:
                s1 = s1 + ".#.#."
        print(s1)

        s1 = ""
        for i in range(len(mList)):
            if i != len(mList)-1:#마지막문자가 아니라면
                s1 = s1+"..#."
            else:
                s1 = s1+"..#.."
        print(s1)
soltion()