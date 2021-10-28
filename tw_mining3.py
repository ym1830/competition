import twint

c = twint.Config()

c.Search = 'サバ缶','今日'
c.Limit = 10000
c.Store_csv = True
c.Output = "result2.csv"

twint.run.Search(c)