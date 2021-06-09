# 1. dash / underscore 로 분리하여 camel casting 을 하는 함수를 작성하시오.
# 제일 첫글자는 대문자일 경우에만 대문자로 출력되게 합니다.
#
# ex)
#
# toCamelCase("the-stealth-warrior"); // returns "theStealthWarrior"
#
# toCamelCase("The_Stealth_Warrior"); // returns "TheStealthWarrior"

def toCamelCase(str):

    for i in range(1, len(str)):
        if str[i] == "-" or str[i] == "_":
            try:
                if str[i+1].islower():
                    str[i+1] = str[i+1].upper()
            except:
                pass

    str = str.replace("_","").replace("-","")
    # print(str)
    return str


toCamelCase("the_Stealth_Warrior")