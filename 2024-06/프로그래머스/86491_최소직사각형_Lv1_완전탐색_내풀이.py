def solution(sizes):
    max_w = 0
    max_h = 0
    calc_arr = []
    for w, h in sizes:
        calc_w = max(w, h)
        calc_h = min(w, h)
        calc_arr.append([calc_w, calc_h])

    for w, h in calc_arr:
        max_w = max(w, max_w)
        max_h = max(h, max_h)

    return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
