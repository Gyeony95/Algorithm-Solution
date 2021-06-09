# 2. a1, a2 두 개의 문자열 배열이 주어지고, a2 에 포함되는 a1 의 문자열 배열을 사전순서대로 정렬하여 리턴하는 함수를 작성하시오.
#
# #Example 1: a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# #Example 2: a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []
#
# 안내:
# 결과 문자열 배열에는 중복 문자열이 없게합니다.
# 함수에서 입력으로 받는 문자열 배열의 조작은 금지합니다.
#
# ex) java
# public class TestClass {
#
# 	public static String[] inArray(String[] array1, String[] array2) {
#  // your code
# 	}
#
# }

def TestClass(a1, a2):
    a3 = []

    for i in range(len(a2)):
        for j in range(len(a1)):
            if a1[j] in a2[i]:
                a3.append(a1[j])
    a3 = set(a3)
    a3 = sorted(a3)
    # print(a3)
    return a3



a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

TestClass(a1,a2)
