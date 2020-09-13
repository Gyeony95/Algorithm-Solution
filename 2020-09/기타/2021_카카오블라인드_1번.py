def solution(new_id):
    answer = ''
    arr = list(new_id)

    for i in range(len(arr)):

        #1
        if ord(arr[i]) >= 65 and ord(arr[i]) <= 90:
            arr[i] = chr(ord(arr[i]) + 32)
        #2
        if ord(arr[i]) < 97 or ord(arr[i]) > 122:
            if ord(arr[i]) < 48 or ord(arr[i]) > 57:
                if ord(arr[i]) == 126 or ord(arr[i]) == 95 or ord(arr[i]) == 46 or ord(arr[i]) == 45 or arr[i] == ' ':
                    pass
                else:
                    arr[i] = ' '
    arr = check(arr)
    # 3
    for i in range(len(arr)):
        if arr[i] == '.':
            for j in range(i + 1, len(arr)):
                if arr[j] == '.' or arr[j] == ' ':
                    arr[j] = ' '
                else:
                    break
    # 4
    if arr[0] == '.':
        arr[0] = ' '
    if arr[-1] == '.':
        arr[-1] = ' '
    arr = check(arr)

    # 5
    if len(arr) == 0:
        arr.append('a')

    # 6
    arr = arr[0:15]

    arr = check(arr)
    # 4
    if arr[0] == '.':
        arr[0] = ' '
    if arr[-1] == '.':
        arr[-1] = ' '
    arr = check(arr)
    # 7
    if len(arr) <= 2:
        while len(arr) != 3:
            arr.append(arr[-1])
    arr = check(arr)

    return "".join(arr)


def check(marr):
    text = "".join(marr)
    text2 = "".join(text.split())
    marr = list(text2)

    return marr

print(solution("abcdefghijklmn.p"))