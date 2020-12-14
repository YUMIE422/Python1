import json #jsonファイルの読み込み
from urllib.request import urlopen #URLを開くためのライブラリ（urllibモジュールでWEBページを取得する）、urlopen()関数にURLを指定する,HTTP通信を実施する
from random import shuffle #引数に渡したリストの要素をシャッフルする
from flask import Flask, render_template #python用のマイクロウェブアプリケーションフレームワーク
from bs4 import BeautifulSoup #必要なデータを抜き出すライブラリ（シンプルでわかりやすいAPI）、bs4モジュールからBeautifulSoapクラスをインポートする

app = Flask(__name__) #APPにFlaskを定義する


@app.route("/") #app.route(‘/‘)でルートのアドレスにそれ以下のものを設置
def index(): #関数の定義
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    # from bs4 import BeautifulSoup    # importする
    # with open("index.html") as f:
    #     soup = BeautifulSoup(f, 'html.parser')
    # for h3 in soup.find_all("h3"):
    #     print(h3.get("href")), h3.text
    
    # """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""
    # """**** ここを実装します（基礎課題） ****"""

    #1. はてブのホットエントリーページのHTMLを取得する
    # res = urlopen.get('https://b.hatena.ne.jp/hotentry/all')
    #2. BeautifulSoupでHTMLを読み込む
    # soup = BeautifulSoup(res.text, 'html.parser')
    #3. 記事一覧を取得する
    # for h3 in soup.find_all("h3"):
            # print(h3.get("href")), h3.text
            # title_text = soup.find('entrylist-contents-title').get_text()
            # print(title_text.status_code)
    #4. ランダムに1件取得する
    
    # 5. 以下の形式で返却する.
    # return json.dumps({
    #             "content" : print(title_text).find("title").string,
    #             "link": print(title_text).get('rdf:about')
    # })
    
    # return json.dumps({
    #     "content" : "記事のタイトルだよー",
    #     "link" : "記事のURLだよー"
    # })
    
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("item")
    shuffle(items)
    item = items[0]
    print(item)
    return json.dumps({
        "content" : item.find("title").string,
        # "link" : item.find("link").string
        "link": item.get('rdf:about')
    })
    
@app.route("/api/xxxx")
def api_xxxx():
    """**** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=False, port=5004)
