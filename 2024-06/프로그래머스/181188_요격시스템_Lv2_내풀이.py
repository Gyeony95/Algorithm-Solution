# 실패!
def solution(targets):
    launch_cnt = 0
    while len(targets) != 0:
        all_range = []
        double_range = []
        hit_range = []
        for i in targets:
            arr = get_range_num(i[0], i[1])
            all_range += arr
            double_range.append(arr)
        all_range = list(set(all_range))

        for i in all_range:
            hit_range.append(getHitCnt(double_range, i))

        launch_value = hit_range.index(max(hit_range))
        targets = [row for row in targets if not condition(row, all_range[launch_value])]
        launch_cnt += 1

    return launch_cnt


def get_range_num(s, e):
    step = 0.5
    current = s
    result = []

    while current <= e:
        result.append(round(current, 1))  # round to avoid floating-point arithmetic issues
        current += step
    result.pop(0)
    result.pop(len(result) - 1)
    return result


def condition(value, target):
    return target in get_range_num(value[0], value[1])


def getHitCnt(double_range, hit):
    hit_cnt = 0
    for i in double_range:
        if hit in i:
            hit_cnt += 1
    return hit_cnt


targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
print(solution(targets))
