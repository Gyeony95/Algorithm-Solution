def soltion():
    T = int(input())
    for test_case in range(1, T + 1):
        n,m = input().split()
        n = int(n);m = int(m)
        aArr = input().split()
        bArr = input().split()
        max = 0

        if n<m:
            for i in range(m-n+1):
                count = 0
                for j in range(len(aArr)):
                    count = count + int(aArr[j])*int(bArr[j])
                if count > max:
                    max = count
                aArr.insert(0,0)
        else:
            for i in range(n-m+1):
                count = 0
                for j in range(len(bArr)):
                    count = count + int(aArr[j])*int(bArr[j])
                if count > max:
                    max = count
                bArr.insert(0,0)

        print ("#"+str(test_case),max)
soltion()
