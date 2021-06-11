n = int(input())

h = 0
m = 0
s = 0
count = 0
while m != 60:
    while s != 60:
        if ('3' in list(str(s))) or ('3' in list(str(m))):
            count +=1
        s +=1
    s = 0
    m += 1

count = n * count
if n >=3:
    count += 3600

print(count)