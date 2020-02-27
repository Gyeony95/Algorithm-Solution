def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]#뒤집어줌


    n = len(truck_weights)#트럭이 몇대인지?
    passing_weight = [0] * n#각 트럭이 다리에 오르는 순간부터 얼마의 시간이 흘렀는지를 나타내는 리스트
    passed = []
    passing = []

    i = 0
    j = -1
    while len(passed) < n:#트럭이 다 지나간거 아니면 반복
        if len(truck_weights) > 0 and sum(passing) + truck_weights[-1] <= weight:#남은 트럭이 1대이상이고, 다리위트럭과 다음트럭 무게를 합쳐도 버틸수 있을때
            passing.append(truck_weights.pop())#트럭 하나 대기에서 이동중으로 옮김
            j += 1
        passing_weight[:j + 1] = [passing_weight[z] + 1 for z in range(j + 1)]
        #0부터 j까지 반복  -> 1씩 올려서 저장
        if passing_weight[i] == bridge_length:
            passed.append(passing[0])
            passing = passing[1:]
            i += 1

    return passing_weight[0] + 1
print (solution(2, 10, [7,4,5,6]))