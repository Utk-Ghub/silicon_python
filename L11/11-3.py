# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson11 応用編 Webとネットワーク ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("11-3 PythonでWebサーバーを作ろう")
print("-------------------------")
print("")

print("1ファイルで全コードを実行不可となるため、コードごとにファイルを分割した")

print("| FlaskでWebサーバーを立ち上げよう")
print("----------------------------------------")
print("コード/Flaskのimport: No Output")
print("コード/Flaskの利用: No Output")
print("c11_3_1/Flaskの実行:")

print("----------------------------------------")
print("Point/サーバー名とポート番号のデフォルト値:")

print("----------------------------------------")
print("c11_3_2/Flaskのhello_world関数:")
print("c11_3_3/Flaskの処理の作成:")
print("c11_3_4/Flaskの処理の作成:")
print("c11_3_5/Flaskの処理の作成:")

print("----------------------------------------")
print("")

print("<テンプレートを作成する>")
print("----------------------------------------")
print("hello.html")
print("c11_3_6/テンプレートの利用:")

print("----------------------------------------")
print("")

print("<HTTPメソッドを使用する>")
print("----------------------------------------")
print("hello.html")
print("c11_3_6/テンプレートの利用:")
print("c11_3_7/HTTPメソッドを使用した処理の作成:")
print("コード：test_flask_post.py/POSTでアクセス:")
print("ターミナル/POSTでアクセス：")
post_access = """\
CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('username', 'mike')])])\
"""
print(post_access)

print("----------------------------------------")
print("c11_3_8/返り値として値のみを返す:")
print("ターミナル/POSTでアクセス：")
print("コード：test_flask_put.py/PUTでアクセス:")
print("コード：test_flask_delete.py/DELETEでアクセス:")
post_access = """\
mike
"""
print(post_access)

print("----------------------------------------")
print("コード：test_flask_put.py/PUTでアクセス:")
print("*** Error Output ***")
err_msg = """\
<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>\
"""
print(err_msg)

print("----------------------------------------")
print("")


print("| データベースを利用する")
print("----------------------------------------")
print("コード/sqlite3のインポート: No Output")
print("コード/データベースに接続する処理: No Output")
print("コード/データベースへの接続を閉じる処理: No Output")
print("c11_3_9/データベースを利用する関数の準備:")

print("----------------------------------------")
print("コード/データベースへの接続とテーブルの作成: No Output")
print("コード/GET時の処理: No Output")
print("コード/POST時の処理: No Output")
print("コード/PUT時の処理: No Output")
print("コード/DELETE時の処理: No Output")
print("c11_3_10/データベースを利用する処理:")
print("コード：test_flask_db.py/さまざまなメソッドで呼び出し:")
print("ターミナル/それぞれのメソッドで呼び出し")
db_msg = """\
No
created jun
updated jun: sakai
deleted sakai\
"""
print(db_msg)

print("----------------------------------------")
print("11-3終了")