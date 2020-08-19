n = input()

m = []
n = list(n)
count = 0

if n[0] == 'a':
    m.append(1)
    m.append(int(n[1]))
elif n[0] == 'b':
    m.append(2)
    m.append(int(n[1]))
elif n[0] == 'c':
    m.append(3)
    m.append(int(n[1]))
elif n[0] == 'd':
    m.append(4)
    m.append(int(n[1]))
elif n[0] == 'e':
    m.append(5)
    m.append(int(n[1]))
elif n[0] == 'f':
    m.append(6)
    m.append(int(n[1]))
elif n[0] == 'g':
    m.append(7)
    m.append(int(n[1]))
elif n[0] == 'h':
    m.append(8)
    m.append(int(n[1]))

if m[0] -2 >= 1 and m[1] -1 >= 1:
    count = count+1
if m[0] -2 >= 1 and m[1] +1 <= 8:
    count = count + 1
if m[0] +2 <= 8 and m[1] +1 <= 8:
    count = count + 1
if m[1] +2 <= 8 and m[0] -1 >= 1:
    count = count + 1
if m[0] -1 >= 1 and m[1] -2 >= 1:
    count = count+1
if m[0] -1 >= 1 and m[1] +2 <= 8:
    count = count + 1
if m[0] +1 <= 8 and m[1] +2 <= 8:
    count = count + 1
if m[1] +1 <= 8 and m[0] -2 >= 1:
    count = count + 1

print(count)