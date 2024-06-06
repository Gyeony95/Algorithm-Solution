def solution(bandage, health, attacks):
    original_health = health
    total_seconds = 0
    seconds_since_last_heal = 0

    bandage_interval = bandage[0]
    heal_amount = bandage[1]
    heal_bonus = bandage[2]

    last_attack_time = get_last_attack_time(attacks)
    attack_index = 0

    while total_seconds <= last_attack_time:
        total_seconds += 1
        seconds_since_last_heal += 1

        if attack_index < len(attacks) and attacks[attack_index][0] == total_seconds:
            damage = attacks[attack_index][1]
            health -= damage
            seconds_since_last_heal = 0
            attack_index += 1

            if health <= 0:
                return -1

            continue

        if seconds_since_last_heal == bandage_interval:
            health = heal(health, original_health, heal_amount + heal_bonus)
            seconds_since_last_heal = 0
        else:
            health = heal(health, original_health, heal_amount)

    return health


def heal(current_health, max_health, heal_amount):
    return min(max_health, current_health + heal_amount)


def get_last_attack_time(attacks):
    return attacks[-1][0] if attacks else 0


bandage = [1, 1, 1]
attacks = [[1, 2], [3, 2]]

print(solution(bandage, 5, attacks))
