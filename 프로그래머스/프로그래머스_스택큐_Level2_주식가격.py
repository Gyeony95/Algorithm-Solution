def solution(prices):
    answer = []#정답배열
    count = 0#가격안떨어진 초 기록
    for i in range(0, len(prices), 1):
        for j in range(i + 1, len(prices), 1):
            if prices[i] <= prices[j] and i != j:#뒤에 수들이 나보다 연달아 크거나 같으면 카운트 +1
                count += 1
            else:#뒤에가 나보다 작으면 카운드 +1만하고 브레이크
                count += 1
                break
        answer.append(count)#정답배열에 추가
        count = 0#카운트초기화

    return answer

solution([1, 2, 3, 2, 3])