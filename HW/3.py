# 3. 두 개의 정수 n (n >= 0), d (0 <= d <= 9) 를 입력으로 받습니다.
# 0 과 n 사이의 수를 제곱한 k**2 에서, 입력으로 받은 d 의 숫자를 모두 세어 리턴하는 함수를 작성하시오.
#
# ex 1)
# n = 10, d = 1, the k*k 는 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# 1, 16, 81, 100 이 1을 포함하고, 결과는 4입니다.
#
# ex 2)
# dig(25, 1):
# n 중 대상은 1, 4, 9, 10, 11, 12, 13, 14, 19, 21 입니다.
#  k*k 에서 다음 숫자가 결과 카운트에 포함됩니다.
# 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
# 결과는 11입니다.
# 121이 1을 두 개 포함하므로 카운트가 2번 되었다는 것을 명심하세요.
#
# ex) java
# public class TestClass {
#
#  public static int dig(int n, int d) {
#  // your code
#  }
# }

# 입력으로 받는다는 옵션이 있으니 두가지 변수 입력 받음
n,m = map(int, input().split())
def dig(n,m):
    a1 = []
    count = 0
    for i in range(n+1):
        a1.append(i**2)
    for i in a1:
        a2 = list(str(i))
        for j in a2:
            if j == str(m):
                count = count+1
    # print(count)
    return count

dig(n,m)
