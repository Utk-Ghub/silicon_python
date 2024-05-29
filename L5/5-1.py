print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson5 入門編 モジュールとパッケージ ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("5-1 作成したパッケージをインポートしよう")
print("-------------------------")
print("")

print("| コマンドライン引数の使い方を知ろう")
print("<ターミナルからPythonのスクリプトを実行する>")
print("----------------------------------------")
print("c5_1_1/printの処理を記述:")
print('test')

print("----------------------------------------")
print("")

print("<スクリプト実行時に引数を渡す>")
print("----------------------------------------")
print("c5_1_2/引数を表示する:")
import sys

print(sys.argv)

print("----------------------------------------")
print("c5_1_3/スクリプトの処理:")
import sys

for i in sys.argv:
    print(i)

print("----------------------------------------")
print("")

print("| import文の使い方を学ぼう")
print("----------------------------------------")
print("c5_1_4/インポートした関数の呼び出し:")
import lesson_package.tools.utils

r = lesson_package.tools.utils.say_twice('hello')
print(r)

print("----------------------------------------")
print("c5_1_5/fromを使ったモジュールの読み込み:")
from lesson_package.tools import utils, utils as u

r = utils.say_twice('hello')
print(r)

print("----------------------------------------")
print("c5_1_6/関数だけをインポートする:")
from lesson_package.tools.utils import say_twice

r = say_twice('hello')
print(r)

print("----------------------------------------")
print("")

print("<asを使って違う名前で読み込む>")
print("----------------------------------------")
print("c5_1_7/asを使って読み込む:")

r = u.say_twice('hello')
print(r)

print("----------------------------------------")
print("")

print("| インポートするときのパスの書き方を知ろう")
print("----------------------------------------")
print("c5_1_8/モジュールの読み込み:")
from lesson_package.talk import human

print(human.sing())

print("----------------------------------------")
print("c5_1_9/関数の呼び出し:")
from lesson_package.talk import human

print(human.cry())

print("----------------------------------------")
print("")

print("| __init__.pyとアスタリスクを使ったインポート")
print("----------------------------------------")
print("c5_1_10/アスタリスクを使ったモジュールの読み込み:")
from lesson_package.talk import *

print(animal.sing())
print(animal.cry())

print("----------------------------------------")
print("c5_1_11/アスタリスクを使ったモジュールの読み込み:")
from lesson_package.talk import *

print(animal.sing())
print(animal.cry())
print(human.sing())
print(human.cry())

print("----------------------------------------")
print("")

print("| ImportErrorが発生した場合の対処法")
print("----------------------------------------")
print("c5_1_12/モジュールの読み込み:No Output")
from lesson_package.tools import utils

print("----------------------------------------")
print("c5_1_13/モジュールの読み込み:")
# from lesson_package import utils
print("*** Error Output ***")
err_msg = """\
    from lesson_package import utils
ImportError: cannot import name 'utils' from 'lesson_package' (省略)\
"""
print(err_msg)

print("----------------------------------------")
print("c5_1_14/モジュールの読み込み: No Output")
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

print("----------------------------------------")
print("")

print("| 自分が作ったパッケージをまとめてみよう")
print("<setup.pyの作成>")
print("----------------------------------------")
print("No Output")

print("----------------------------------------")
print("5-1終了")