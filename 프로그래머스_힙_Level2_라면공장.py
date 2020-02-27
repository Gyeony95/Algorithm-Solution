def solution(stock, dates, supplies, k):
    import heapq
    answer = 0
    idx = 0
    pq = []
    while stock < k:#스톡이 k넘으면의미없으니 거기까지만 반복
        for i in range(idx, len(dates)):#idx이전은 이미 지난거라서 거기부터만 시작
            if stock < dates[i]:#다음날짜까지 스톡이 못버틸때
                break#반복문 탈출
            heapq.heappush(pq, -supplies[i])#다음까지 버틸수 있으면 이번꺼는 힙에저장, 아마 최대힙으로 쓰려고 음수로 저장하는거같음
            idx = i + 1#인덱스 더해줌

        stock += (heapq.heappop(pq) * -1)#힙에서 제일 큰수 꺼내서 스톡에 더함
        answer += 1#스톡 받았으니 앤서 +1해줌
    return answer
print (solution(4, [4,10,15], [20,5,10], 30))