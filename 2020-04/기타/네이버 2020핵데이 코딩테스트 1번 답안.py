def solution(n, delivery):
    answer = ''


    have = []#재고있음
    nohave = []#재고없음
    donknow = []#모름

    for i in range(len(delivery)):#have배열 채우는 포문
        if delivery[i][2] == 1:#두 상품 모두 있음
            have.append(delivery[i][0])
            have.append(delivery[i][1])

    for i in range(len(delivery)):#nohave배열 채우는 포문
        if delivery[i][2] == 0:#배송안되는 애들
            if delivery[i][0] in have:
                nohave.append(delivery[i][1])
            elif delivery[i][1] in have:
                nohave.append(delivery[i][0])

    for i in range(len(delivery)):#donknow배열 채우는 포문
        if delivery[i][2] == 0:
            if delivery[i][0] not in have and delivery[i][1] not in have:
                if delivery[i][0] in nohave and delivery[i][1] not in nohave:
                    donknow.append(delivery[i][1])
                elif delivery[i][1] in nohave and delivery[i][0] not in nohave:
                    donknow.append(delivery[i][0])

    for i in range(1,n+1,1):#없는 값 판별
        isempty = True
        for j in range(len(delivery)):
            if delivery[j][0] == i or delivery[j][1] == i:
                isempty = False
        if isempty:
            donknow.append(i)

    # 정답 문자열 만드는부분
    for i in range(1,n+1,1):

        if i in have:
            answer = answer+"O"
        elif i in nohave:
            answer = answer+"X"
        elif i in donknow:
            answer = answer+"?"

    print (answer)
    return answer





solution(3,[[1,3,1]])
#solution(6,[[1,3,1],[3,5,0],[5,4,0],[2,5,0]])
#solution(7,[[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]	)