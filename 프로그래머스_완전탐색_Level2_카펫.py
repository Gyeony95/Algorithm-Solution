def solution(brown, red):
    amount = brown + red
    vertical = 0
    horizontal = 0
    for i in range(1, amount + 1):  # 약수판단
        if amount % i == 0 and i > 2 and amount / i > 2:
            if (int(round(float(amount / i))) - 2) * (i - 2) == red:
                if amount / i >= i:
                    horizontal = int(round(float(amount / i)))
                    vertical = i

                else:
                    horizontal = i
                    vertical = int(round(float(amount / i)))

    answer = [horizontal, vertical]
    return answer

print (solution(24, 24))