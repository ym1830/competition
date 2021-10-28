import twint
from datetime import datetime, timedelta

today = datetime.today()
since = today - timedelta(weeks=364)

# Configure
c = twint.Config()
#特定のユーザー名
#c.Username = "Qiita"
#求めるツイートにあってほしい文字
#c.Search = "チルい","曲"　#and検索になるっぽい
c.Search = "cm","spotify"
#c.Search = "#名刺代わりの小説10選"  #検索ワードにハッシュタグをつけない場合、本文にあるときのみヒットする
#いつからのツイートか
c.Since = datetime.strftime(since, '%2021-%10-%01')
#実行日から数えて過去何日分のツイートを取得するか（やけに少なかった）
c.Limit = 365
#csv形式で保存するか
c.Store_csv = True
#保存ファイルの名前
c.Output = "cm_spotify1.csv"

# Run
twint.run.Search(c)