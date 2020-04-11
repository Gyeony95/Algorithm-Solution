def solution(id_list, k):
    answer = 0

    hash = {}#해시 선언
    for i in range(len(id_list)):
        mArr = id_list[i].split()
        for j in range(len(mArr)):
            hash[mArr[j]] = 0

    for i in range(len(id_list)):#아이디 리스트만큼 반복
        mArr = id_list[i].split()
        today = []
        for j in range(len(mArr)):#하루에 배달시킨 사람만큼 반복
            if hash[mArr[j]] <k and mArr[j] not in today:
                today.append(mArr[j])
                hash[mArr[j]] = hash[mArr[j]]+1

    for key,value in hash.items():#해시 밸류 합치기
        answer = answer + value

    print(answer)
    return answer

#solution(["A B C D", "A D", "A B D", "B D"], 2)
#solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3)
solution(["1", "1 1 1 1", "1 1 1", "1 2", "1 1 1", "1"], 7)