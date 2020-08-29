import sys
n,m = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
start, end = 1, max(arr)
while start <= end:
   mid = (start+end)//2
   total = 0
   for i in arr:
       total += i//mid
   if total >= m:
       start = mid+1
   else:
       end = mid-1
print(end)