print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson5 入門編 モジュールとパッケージ ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("5-2 Pythonのライブラリの使い方")
print("-------------------------")
print("")

print("| すぐに使える便利な組み込み関数")
print("----------------------------------------")
print("c5_2_1/globals():")
print(globals())

print("----------------------------------------")
print("")

print("<sorted関数で並べ替える>")
print("----------------------------------------")
print("c5_2_2/辞書型のキーを表示する:")
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

for key in ranking:
    print(key)

print("----------------------------------------")
print("c5_2_3/キーの順番で辞書型を並べ替える:")
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

print(sorted(ranking))

print("----------------------------------------")
print("c5_2_4/バリューの順番で辞書型を並べ替える:")
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

print(sorted(ranking, key=ranking.get))

print("----------------------------------------")
print("")

print("Point/getメソッドの働き:")
print("----------------------------------------")
print("c5_2_5/get:")
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

print(ranking.get('A'))

print("----------------------------------------")
print("")

print("----------------------------------------")
print("c5_2_6/バリューが高い順に辞書型を並べ替える:")
ranking = {
    'A': 100,
    'B': 85,
    'C': 92
}

print(sorted(ranking, key=ranking.get, reverse=True))

print("----------------------------------------")
print("")

print("| Pythonの標準ライブラリを使ってみよう")
print("<defaultdictを使用する>")
print("----------------------------------------")
print("c5_2_7/文字列に含まれるアルファベットを教える:")
# s = "fadasaklfsalkfdjasslkdj"
#
# d = {}
# for c in s:
#     d[c] += 1
# print(d)
print("*** Error Output ***")
err_msg = """\
    d[c] += 1
    ~^^^
KeyError: 'f'\
"""
print(err_msg)

print("----------------------------------------")
print("c5_2_8/文字列に含まれるアルファベットを教える:")
s = "fadasaklfsalkfdjasslkdj"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

print("----------------------------------------")
print("c5_2_9/setdefault:")
s = "fadasaklfsalkfdjasslkdj"

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

print("----------------------------------------")
print("c5_2_10/defaultdict:")
s = "fadasaklfsalkfdjasslkdj"

from collections import defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)

print("----------------------------------------")
print("")

print("| サードパーティのライブラリを使ってみよう")
print("----------------------------------------")
print("c5_2_11/出力する文字の色を赤くする:")
# PyCharmの場合、ターミナルで`python L5/5-2.py`を実行しないと文字が赤くならない
from termcolor import colored

print(colored('test', 'red'))

print("----------------------------------------")
print("c5_2_12/サードパーティライブラリの関数の使い方を確認する:")
from termcolor import colored

print(help(colored))

print("----------------------------------------")
print("")

print("| ライブラリをインポートするときはここに注意")
print("<インポートの順番>")
print("----------------------------------------")
print("c5_2_13/複数のライブラリのインポート: No Output")
import collections, sys, os

print("----------------------------------------")
print("c5_2_14/複数のライブラリのインポート: No Output")
import collections
import sys
import os

print("----------------------------------------")
print("c5_2_15/複数のライブラリのインポート: No Output")
import collections
import sys
import os

import termcolor

print("----------------------------------------")
print("c5_2_16/複数のライブラリのインポート: No Output")
import collections
import sys
import os

import termcolor

import lesson_package

print("----------------------------------------")
print("c5_2_17/複数のライブラリのインポート: No Output")
import collections
import sys
import os

import termcolor

import lesson_package

import config

print("----------------------------------------")
print("")

print("<ライブラリの場所>")
print("----------------------------------------")
print("c5_2_18/ライブラリの場所を出力する:")
import collections

import termcolor

import lesson_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print("----------------------------------------")
print("c5_2_19/Python側がパッケージを読み込む場所を表示:")
import sys
print(sys.path)

print("----------------------------------------")
print("")

print("| スクリプトが読み込まれるときの注意点")
print("----------------------------------------")
print("c5_2_20/__name__:")
print(__name__)

print("----------------------------------------")
print("c5_2_21/config.pyの読み込み:")
import config

print('lesson:', __name__)

print("----------------------------------------")
print("c5_2_22/animal.pyの読み込み: print文即実行")
import lesson_package.talk.animal2

print('lesson:', __name__)

print("----------------------------------------")
print("c5_2_22/animal.pyの読み込み: if文つき")
import lesson_package.talk.animal

print('lesson:', __name__)

print("----------------------------------------")
print("c5_2_23/main関数を使った書き方:")
def main():
    import lesson_package.talk.animal

if __name__ == '__main__':
    main()

print("----------------------------------------")
print("5-2終了")
print("Lesson5終了")