n = 1260

count = 0

list = [500, 100, 50, 10]

for coin in list:
    count += n//coin #해당화폐로 거슬러줄 수 있는 동전의 갯수
    n %= coin

print(count)