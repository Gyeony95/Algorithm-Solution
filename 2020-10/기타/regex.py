import re
import pandas as pd
from konlpy.tag import Kkma

def apply_kko_regex(msg_list):
    kko_pattern = re.compile("\[([\S\s]+)\] \[(오전|오후) ([0-9:\s]+)\] ([^\n]+)")
    kko_date_pattern = re.compile("--------------- ([0-9]+년 [0-9]+월 [0-9]+일) ")

    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)





def apply_kko_regex(msg_list):
    """ 상단 생략 """

    kko_parse_result = list()
    cur_date = ""

    for msg in msg_list:
        # 날짜 부분인 경우
        if len(kko_date_pattern.findall(msg)) > 0:
            cur_date = dt.datetime.strptime(kko_date_pattern.findall(msg)[0], "%Y년 %m월 %d일")
            cur_date = cur_date.strftime("%Y-%m-%d")
        else:
            kko_pattern_result = kko_pattern.findall(msg)
            if len(kko_pattern_result) > 0:
                tokens = list(kko_pattern_result[0])
                # 이모지 데이터 삭제
                tokens[-1] = re.sub(emoji_pattern, "", tokens[-1])
                tokens.insert(0, cur_date)
                kko_parse_result.append(tokens)

    kko_parse_result = pd.DataFrame(kko_parse_result, columns=["Date", "Speaker", "timetype", "time", "contents"])
    kko_parse_result.to_csv("./result/kko_regex.csv", index=False)

    return kko_parse_result


def get_noun(msg_txt):
    kkma = Kkma()
    nouns = list()
    # ㅋㅋ, ㅠㅠ, ㅎㅎ
    pattern = re.compile("[ㄱ-ㅎㅏ-ㅣ]+")
    msg_txt = re.sub(pattern, "", msg_txt).strip()

    if len(msg_txt) > 0:
        pos = kkma.pos(msg_txt)
        for keyword, type in pos:
            # 고유명사 또는 보통명사
            if type == "NNG" or type == "NNP":
                nouns.append(keyword)
        print(msg_txt, "->", nouns)

    return nouns
