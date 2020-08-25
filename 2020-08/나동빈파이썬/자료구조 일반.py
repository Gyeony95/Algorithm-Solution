from _collections import deque


def stackFun():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    # 가장 후입 삭제
    stack.pop()
    # 가장 선입 삭제
    stack.pop(-1)

    print(stack)  # 최하단 원소부터 출력
    print(stack[::-1])  # 최상단 원소부터 출력(역순)

def queueFun():
    #from _collections import deque로 큐 사용가능
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.popleft()#선입삭제

    print(queue)#정방향 출력
    queue.reverse()#역순으로 바꿈
    print(queue)#역순 출력
    list(queue)#리스트로 바꿈
    print(queue)#리스트로 출력
#38 57 52 26

   



























