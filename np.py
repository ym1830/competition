from janome.tokenizer import Tokenizer
import pandas as pd

#too many open filesエラー対策（以下２文）
import resource
from pandas._libs.missing import NAType
resource.setrlimit(resource.RLIMIT_NOFILE, (8192, 9223372036854775807))

# 極性辞書の作成
dict_polarity = {}
with open('./pn_ja.dic.txt', 'r', encoding='shift_jis') as f:
    line = f.read()
    lines = line.split('\n')
    for i in range(len(lines)):#55125行目が怪しい
        try:
            line_components = lines[i].split(':')
            dict_polarity[line_components[0]] = line_components[3]
        except IndexError:
            print(i)

 

# ネガポジ分析用の関数の作成
def judge_polarity(text):#print表示のみ。評価対象文字数で結果を割っている
    count = 0
    t = Tokenizer()
    tokens = t.tokenize(text)
    pol_val = 0
    for token in tokens:
        word = token.surface
        pos = token.part_of_speech.split(',')[0]
        if word in dict_polarity:
            count+=1
            pol_val = pol_val + float(dict_polarity[word])
    try:
        pol_val = pol_val/count
    except ZeroDivisionError:
        pol_val = pol_val
    print(text)
    print("評価対象語数",count)

    if pol_val > 0.3:
        print("Positive. Score："+str(pol_val))
    elif pol_val < -0.3:
        print("Negative. Score："+str(pol_val))
    else:
        print("Neutral. Score："+str(pol_val))
    print()

def judge_polarity2(text):#結果を変数へ出力する用
    count = 0
    t = Tokenizer()
    tokens = t.tokenize(text)
    pol_val = 0
    for token in tokens:
        word = token.surface
        pos = token.part_of_speech.split(',')[0]
        if word in dict_polarity:
            print(word)#評価対象語の表示
            count+=1
            pol_val = pol_val + float(dict_polarity[word])
    try:
        pol_val = pol_val/count
    except ZeroDivisionError:
        pol_val = pol_val
    print(text)
    print("評価対象語数",count)
    print(pol_val)

    return pol_val
    
 
# ネガポジ分析の実行
judge_polarity("気品溢れる英傑")
judge_polarity("不遇の境遇を嘆く")
#judge_polarity("普通")
judge_polarity("嫌い")
judge_polarity("嫌いじゃない")
judge_polarity("わかるー！！Spotifyのcmで流れてて一目惚れしてずっとリピしてる…(●︎´▽︎`●︎)サビすごいすこ…！！")

#twitterの文章のネガポジ判定
df = pd.read_csv('creepy.csv')
df = df.query("language=='ja'")#日本語のものだけ抽出
df_ja = df.iloc[:, 10:11]#ツイートだけ抽出

#text = str(df_ja.iloc[1])
#print(text)
#judge_polarity(text)

#ネガポジ判定のリスト作成
NP = []
for i in range(len(df_ja)):
    NP.append(judge_polarity2(str(df_ja.iloc[i])))

#ネガポジリストを日本語だけのデータフレームに追加
df["np"] = NP
df.to_csv("creepy_np.csv")