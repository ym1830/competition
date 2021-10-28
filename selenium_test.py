from selenium import webdriver #モジュールのインポート

browser = webdriver.Chrome() #ブラウザの立ち上がる
browser.get('https://news.google.com/topstories?tab=wn&hl=ja&gl=JP&ceid=JP:ja') #google newsを開く
top = browser.find_element_by_class_name('DY5T1d') #クラスでトップ記事の見出しを取得

print(top.text) #タグの中身の文字を取得

from selenium import webdriver #モジュールのインポート
from selenium.webdriver.common.keys import Keys #キーボード操作のためのモジュール

browser = webdriver.Chrome() #ブラウザの立ち上がる
browser.get('https://google.com') #google newsを開く
search = browser.find_element_by_tag_name('input') #タグの名前で検索窓要素を取得
search.send_keys('Tommy Emmanuel') #検索窓にTommy Emmanuelと入力
search.send_keys(Keys.ENTER) #エンターキーを押す