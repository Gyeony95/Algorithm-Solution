# 4. 노드가 비어있지 않고 0을 포함한 양의 정수를 표현하는 2개의 linked list 를 입력으로 받습니다. 정수가 역순으로 저장되어 있으며 각각의 노드에는 숫자 한개가 있습니다.
# 2개의 숫자를 합하여 다시 역순의 linked list 를 리턴하는 함수를 작성하시오.
#
# ex 1)
#
# 2 -> 4 -> 3
# 5 -> 6 -> 4
# -----------
# 7 -> 0 -> 8
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# ex 2)
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# ex 3)
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# 안내:
# 각 linked list 범위는 [1, 100] 입니다.
# 각 노드의 값은 0 <= Node.val <= 9 과 같습니다.
# 0자체를 빼고는, 0으로 시작하는 정수는 입력으로 들어가지 않습니다. ex. 2 -> 1 -> 0 : 012
#
# 아래 함수(add)를 완성하세요.
# !! 중요 !! 코멘트를 참고해서 ListNode 를 정의하세요.
#
# ex) python3
# # class ListNode:
# # def __init__(self, val=0, next=None):
# # self.val = val
# # self.next = next
# class Solution:
#  def add(self, l1: ListNode, l2: ListNode) -> ListNode:
#  // your code

# 노드 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 링크드 리스트 정의
class SList(object):
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

    def appendleft(self, value):
        if self.is_empty():
            self.head = ListNode(value)
        else:
            self.head = ListNode(value, self.head)
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = ListNode(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = ListNode(value)
            target.next = newtail
            self.size += 1

    def insert(self, value, idx):
        if self.is_empty():
            self.head = ListNode(value)
            self.size += 1
        elif idx == 0:
            self.head = ListNode(value, self.head)
            self.size += 1
        else:
            target = self.selectNode(idx - 1)
            if target == None:
                return
            newNode = ListNode(value)
            tmp = target.next
            target.next = newNode
            newNode.next = tmp
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del (target)
            self.size -= 1
        else:
            target = self.selectNode(idx - 1)
            deltarget = target.next
            target.next = target.next.next
            del (deltarget)
            self.size -= 1

    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.val, '-> ', end='')
                target = target.next
            else:
                print(target.val)
                target = target.next

class Solution():
    def add(self, l1: SList, l2: SList) -> SList:
        # 정답으로 사용랑 링크드 리스트
        l3 = SList()
        # 스위칭을 위한 임시 리스트
        test_place = SList()

        # switch
        if l1.size <= l2.size:
            test_place = l1
            l1 = l2
            l2 = test_place

        carry = 0
        # 크기가 작은 링크드 리스트 먼저 비우면서 더해감
        while (l2.size > 0):
            sum = l1.head.val + l2.head.val + carry
            carry = 0
            if sum >= 10:
                carry = sum // 10
                sum = sum - 10
            l3.appendleft(sum)
            l1.delete(0)
            l2.delete(0)
        # 크기가 큰 링크드 리스트의 잔여물을 비우면서 l3에 값을 추가해감
        while (l1.size > 0):
            sum = l1.head.val + carry
            carry = 0
            if sum >= 10:
                carry = sum // 10
                sum = sum - 10
            l3.appendleft(sum)
            l1.delete(0)
        if carry != 0:
            l3.appendleft(carry)
        return l3


#배열 입력받듯 사용한 링크드 리스트의 값을 순서대로 입력받음
a1 = list(map(int,input().split()));a2 = list(map(int,input().split()))
l1 = SList()
l2 = SList()


# 입력 받은 값들을 링크드 리스트에 추가해줌
for i in range(len(a1)):
    l1.append(a1[i])
for i in range(len(a2)):
    l2.append(a2[i])

#정답 링크드 리스트를 리턴 받아 프린트 해줌
Solution.add(0, l1, l2).printlist()




