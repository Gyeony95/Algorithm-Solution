a = range(10000)

b = list(a)

count = 0

def selfNum(c):
    count = 0
    # print(list(str(c)))

    for i in list(str(c)):
        count = count + int(i)
    count = count + c
    if(count in b):
        b.remove(count)

for i in range(0,10000):
    selfNum(i)

for i in b:
    print(i)