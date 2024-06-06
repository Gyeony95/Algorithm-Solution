def solution(bandage, health, attacks):
    oring_h = health
    total_sec = 0
    heal_sec = 0

    bandage_sec = bandage[0]
    heal_cnt = bandage[1]
    heal_bonus = bandage[2]
    hit_cnt = 0
    last_attack = last_attack_time(attacks)
    while True:
        total_sec += 1
        heal_sec += 1
        _hit = find_second_element(attacks, total_sec)

        if hit_cnt == len(attacks):
            break

        if _hit != 0:
            health = hit(health, _hit)
            heal_sec = 0
            hit_cnt += 1
            if health <= 0: return -1
            if total_sec == last_attack:
                break
            continue

        if heal_sec == bandage_sec:
            health = add(oring_h, health, heal_cnt)
            health = add(oring_h, health, heal_bonus)
            heal_sec = 0
        else:
            health = add(oring_h, health, heal_cnt)

        if total_sec == last_attack:
            break

    return health


def add(origin, health, heal):
    if origin < health + heal: return origin
    return health + heal


def hit(health, d):
    return health - d


def find_second_element(attacks, target):
    for sub_array in attacks:
        if sub_array[0] == target:
            return sub_array[1]
    return 0


def last_attack_time(attacks):
    length = len(attacks)
    return attacks[length - 1][0]


bandage = [1, 1, 1]
attacks = [[1, 2], [3, 2]]

print(solution(bandage, 5, attacks))
