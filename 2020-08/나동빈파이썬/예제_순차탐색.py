#순차탐색
def search(n, target, arr):
    #각 원소를 하나씩 확인
    for i in range(n):
        #현재원소와 찾고자 하는 원소가 동일한 경우
        if arr[i] == target:
            return i+1 #현재 위치 반환

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])#원소의 갯수
target = input_data[1]#찾고자 하는 문자열

print('앞서 적은 원소 갯수만큼 문자열을 입력하세요. 구분은 띄어쓰기 입니다.')
arr = input().split()

#결과 표시
print(search(n,target,arr))
