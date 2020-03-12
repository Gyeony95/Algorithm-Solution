import heapq

def solution(scoville, K):
    answer = 0#정답배열
    heap = []#힙에 쓸 배열
    for i in scoville:#힙에 값 쌓음
        heapq.heappush(heap, i)
    while heap[0] <K:#최소힙이니까 그중 첫번째가 제일 작은거, 그게 K보다 작을때
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)#안매운거 두개빼서 하나는 2곱하고 두개 더해서 푸시
        except:#아무리해도 안돼서 인덱스 에러나면 -1리턴
            return -1
        answer+=1#순조롭게 계산되는중이면 -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 123))