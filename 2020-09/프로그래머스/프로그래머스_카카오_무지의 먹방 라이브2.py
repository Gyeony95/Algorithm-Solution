#모범답안
import heapq
def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    #시간이 적은 음식부터 빼야 하므로 순서대로 정렬
    q = []
    for i in range(len(food_times)):
        #(음식시간, 음식번호)형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0#먹기위해 사용한 시간
    previous = 0#직전에 다먹은 시간
    lenth = len(food_times)#남은 음식의 갯수


    #sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식의 갯수 k와 비교
    while sum_value + ((q[0][0] - previous) * lenth) <= k:
        now= heapq.heappop(q)[0]
        sum_value += (now - previous) * lenth
        lenth -= 1
        previous = now

    result = sorted(q, key = lambda x:x[1]) #움식의 번호 기준으로 정렬
    return result[(k-sum_value) % lenth][1]

print(solution([3,1,2,5], 5))