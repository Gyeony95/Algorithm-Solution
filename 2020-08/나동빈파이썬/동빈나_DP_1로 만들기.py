#모범답안, 점화식의 도출법을 아직 잘 이해못함
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i -1]+1#1을 더한다음 2,3,5로 나눈값중 가장 작은 걸 d[i]에 저장하는 방식
    if i %2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i %3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i %5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
