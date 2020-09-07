def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    count = 0
    while True:
        for i in range(len(food_times)):
            if food_times[i] > 0:
                if count == k:
                    return i + 1
                food_times[i] -= 1
                count += 1

print(solution([3,1,2,5], 5))