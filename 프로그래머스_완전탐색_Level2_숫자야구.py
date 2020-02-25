def solution(baseball):
    answer=[]
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):#111부터 999중에서
                if (i==k or i==j or j==k):#중복을 제외하고
                    pass
                else:
                    answer.append(str(i*100+j*10+k))#나머지를 정답 배열에 저장
    for i in baseball:#질문의 횟수만큼 반복하고
        for j in range(len(answer)):#정답배열만큼 반복함
            st_cnt=0#스트라이크 카운트
            bl_cnt=0#볼 카운트
            for k in range(3):
                for l in range(3):#3*3 반복
                    if (answer[j][k]==str(i[0])[l] and k==l):
                        #answer[j][k]는 정답배열의 문자열 ex)123을 인덱스로 탐색
                        #str(i[0])[l]는 배열 i의0번째 인덱스를 문자열로 형변환 후, 그 문자열의 l번째인덱스를 가져와 비교
                        #완전 같아야해서 k==l
                        st_cnt+=1
                    elif (answer[j][k]==str(i[0])[l] and k!=l):
                        bl_cnt+=1
                        # 완전 같이 않아야해서 k !+ l
            if st_cnt==int(i[1]) and bl_cnt==int(i[2]):
                pass
            else:
                answer[j]=0
        answer=list(set(answer))
        if (0 in answer):
            answer.remove(0)
        else:
            pass
    return len(answer)

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])