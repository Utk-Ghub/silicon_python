# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson11 応用編 Webとネットワーク ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("11-1 Webでよく使うファイル形式")
print("-------------------------")
print("")

print("| JSONファイルを操作しよう")
print("----------------------------------------")
print("c11_1_1/:")
import json


j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

print(j)
print("##########")
print(json.dumps(j))

print("----------------------------------------")
print("")

print("<JSONファイルに書き込む>")
print("----------------------------------------")
print("c11_1_2/JSONファイルの書き込み: No Output")
with open('test.json', 'w') as f:
    json.dump(j, f)

print("----------------------------------------")
print("")

print("<JSONファイルを読み込む>")
print("----------------------------------------")
print("c11_1_3/JSONファイルの読み込み:")
with open('test.json', 'r') as f:
    print(json.load(f))

print("----------------------------------------")
print("c11_1_4/JSON形式を辞書型に変換:")
a = json.dumps(j)
print(a)
print("@@@@@@@@@@")
print(json.loads(a))

print("----------------------------------------")
print("")
print("11-1終了")

import os

while True:
    file_remover = input('作成したファイルを削除しますか（y/n）：')
    if file_remover == 'y':
        os.remove('test.json')
        break
    elif file_remover == 'n':
        break
    else:
        print("yかnを入力してください")