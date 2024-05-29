# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson9 応用編 コードスタイル ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("9-2 さらにくわしくPythonの書き方を知ろう")
print("-------------------------")
print("")

print("| データ型に関するヒント、注意点")
print("<文字列の連結の書き方>")
print("----------------------------------------")
print("コード/文字列の連結(悪い例): No Output")
word = 'hello'
word2 = '!'

new_word = '{}{}'.format(word, word2)

print("----------------------------------------")
print("コード/文字列の連結: No Output")
new_word = word + word2

print("----------------------------------------")
print("コード/文字列の連結: No Output")
new_word = '{}$$$$${}!!!!!'.format(word, word2)
new_word = word + '$$$$$' + word2 + '!!!!!'

print("----------------------------------------")
print("コード/文字列の連結(悪い例):")
long_word = ""
for word in ['adsaf', 'dafa', 'dsfda']:
    long_word += "{}fdadfdsa".format(word)

print(long_word)

print("----------------------------------------")
print("コード/文字列の連結:")
long_word = []
for word in ['adsaf', 'dafa', 'dsfda']:
    long_word.append("{}fdadfdsa".format(word))

new_long_word = ''.join(long_word)
print(new_long_word)

print("----------------------------------------")
print("")

print("<リスト内包表記>")
print("----------------------------------------")
print("コード/リスト内包表記: No Output")
x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]

print("----------------------------------------")
print("")

print("<辞書型>")
print("----------------------------------------")
print("コード/辞書型のキーの存在確認:")
d = {'key1': 'value', 'key2': 'value2'}
if 'key1' in d.keys():
    print('test')

if 'key1' in d:
    print('test')

print("----------------------------------------")
print("コード/辞書型の変数名:")
for k, v in d.items():
    print(k, v)

print("----------------------------------------")
print("コード/辞書型の変数名: No Output")
# for name, count in ranking.tems():
#     print(name, count)

print("----------------------------------------")
print("")

print("<リストの初期化>")
print("----------------------------------------")
print("コード：ranking.py/get_most_popularのデフォルト引数: No Output")
print("コード：ranking.py/リストの初期化: No Output")
# def get_most_popular(self, not_list=None):
#     if not_list is None:
#         not_list = []

print("----------------------------------------")
print("")

print("<値の存在確認>")
print("----------------------------------------")
print("コード：ranking.py/get_most_popularのデフォルト引数: No Output")
# if not self.data:
#     return None

# if self.data == {}:
#     return None

print("----------------------------------------")
print("")

print("| 制御構文など「文」に関するヒント、注意点")
print("<インポートの注意点>")
print("----------------------------------------")
print("コード/importの書き方(悪い例): No Output")
import collections, csv, os

print("----------------------------------------")
print("コード/import: No Output")
# import os
# import sys
#
# import flask
#
# import roboter.controller.conversation
#
# import settings

print("----------------------------------------")
print("コード/import: No Output")
# from roboter.controller.conversation import talk_about_restaurant

print("----------------------------------------")
print("コード/import: No Output")
# import roboter.controller.conversation

print("----------------------------------------")
print("コード/import: No Output")
# from roboter.controller import conversation

print("----------------------------------------")
print("")

print("<if文やelse文を1行で書く>")
print("----------------------------------------")
print("コード/if文の書き方:")
if x:
    print('exit')
else:
    print('else')

if x: print('exit')
else: print('else')

print("----------------------------------------")
print("コード/代入文のifとelse:")
y = None
x = 1 if y else 2
print(x)

print("----------------------------------------")
print("コード/代入文のifとelse:")
y = 'faasdfaas'
x = 1 if y else 2
print(x)

print("----------------------------------------")
print("")

print("<例外処理>")
print("----------------------------------------")
print("コード/Exception(悪い例):")
try:
    roboter.controller.conversation.talk_about_restaurant()
except:
    print(exec)

print("----------------------------------------")
print("コード/Exception: No Output")
# class MainError(Exception):
#     pass
#
# def main():
#     try:
#         roboter.controller.conversation.talk_about_restaurant()
#         raise MainError

print("----------------------------------------")
print("")

print("| 関数に関するヒント、注意点")
print("<main関数の作成>")
print("----------------------------------------")
print("コード：main.py/main関数を作成しない: No Output")
# import roboter.controller.conversation
# roboter.controller.conversation.talk_about_restaurant()

print("----------------------------------------")
print("コード：main.py/main関数を作成する: No Output")
# import roboter.controller.conversation
#
# def main():
#     roboter.controller.conversation.talk_about_restaurant()
#
# if __name__ == '__main__':
#     main()

print("----------------------------------------")
print("")

print("<ジェネレーター>")
print("----------------------------------------")
print("コード/通常のforループ:")
def t():
    num = []
    for i in range(10):
        num.append(i)
    return num

for i in t():
    print(i)

print("----------------------------------------")
print("コード/yieldを利用:")
def t():
    for i in range(10):
        yield i

for i in t():
    print(i)

print("----------------------------------------")
print("")

print("<lambda>")
print("----------------------------------------")
print("コード/通常の関数定義を利用:")
def other_func(f):
    print(f(10))

def test_func(x):
    return x * 2

def test_func2(x):
    return x * 5

other_func(test_func)
other_func(test_func2)

print("----------------------------------------")
print("コード/lambdaを利用:")
def other_func(f):
    print(f(10))

other_func(lambda x: x * 2)
other_func(lambda x: x * 5)

print("----------------------------------------")
print("")

print("<クロージャー>")
print("----------------------------------------")
print("コード/クロージャー:")
def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10))
print(plus(30))

print("----------------------------------------")
print("コード/クロージャー:")
i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(10))
print(plus(30))

print("----------------------------------------")
print("コード/クロージャー:")
i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))

print("----------------------------------------")
print("")

print("<デコレーター>")
print("----------------------------------------")
print("コード/デコレーター: No Output")
# @_hello_decorator
# def recommend_restaurant(self):

print("----------------------------------------")
print("コード/デコレーター: No Output")
# recommend_restaurant = _hello_decorator(recommend_restaurant)

print("----------------------------------------")
print("")

print("| そのほかのヒント、注意点")
print("<ファイルのopenではwithを使う>")
print("<TODOコメント>")
print("----------------------------------------")
print("コード：ranking.py/ファイルのopen: No Output")
# def save(self):
#     """Save data to csv file."""
#     # TODO (jsakai) Use locking mechanism for avoiding dead lock issue
#     with open(self.csv_file, 'w+') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=self.column)
#         writer.writeheader()

print("----------------------------------------")
print("")

print("| docstringを書いてPylintでチェックしよう")
print("<docstring>")
print("----------------------------------------")
print("コード：console.py/: No Output")
"""Utils to display to be returned to the user on the console."""


def get_template_dir_path():
    """Return the path of the template's directory.

    Returns:
        str: The template dir path.
    """

print("----------------------------------------")
print("コード：ranking.py/docstring: No Output")
# def get_template_dir_path():
# class RankingModel(CsvModel):
#     """Definition of class that generates ranking model to write to CSV"""

print("----------------------------------------")
print("コード：ranking.py/docstring: No Output")
    # def get_csv_file_path(self):
    #     """Set csv file path.
    #
    #     Use csv path if set in settings, otherwise use default
    #     """

print("----------------------------------------")
print("コード：ranking.py/docstring: No Output")
    # def get_most_popular(self, not_list=None):
    #     """Fetch the data of the top ranking.
    #
    #     Args:
    #         not_list (list): Excludes the name on the list.
    #
    #     Returns:
    #         str: Returns the data of the top ranking
    #     """

print("----------------------------------------")
print("")

print("<Pylintでコードをチェックする>")
print("----------------------------------------")
print("ターミナル/pylintの実行:")
print("*** Error Output ***")
err_msg = """\
************* Module role_model.roboter.models.ranking
<パス省略>ranking.py:66:9: W0511: TODO (jsakai) Use locking mechanism for avoiding dead lock issue (fixme)
<パス省略>ranking.py:16:0: R0205: Class 'CsvModel' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
<パス省略>ranking.py:16:0: R0903: Too few public methods (0/2) (too-few-public-methods)
<パス省略>ranking.py:26:4: W1113: Keyword argument before variable positional arguments list in the definition of __init__ function (keyword-arg-before-vararg)
<パス省略>ranking.py:41:12: C0415: Import outside toplevel (settings) (import-outside-toplevel)
<パス省略>ranking.py:57:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
<パス省略>ranking.py:67:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

-----------------------------------
Your code has been rated at 8.75/10\
"""
print(err_msg)

print("----------------------------------------")
print("コード：ranking.py/CsvModelの定義: No Output")
class CsvModel(object):
    """Base csv model."""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()

print("----------------------------------------")
print("ターミナル/pylintの実行:")
print("*** Error Output ***")
err_msg = """\
************* Module role_model.roboter.models.ranking
<パス省略>ranking.py:62:9: W0511: TODO (jsakai) Use locking mechanism for avoiding dead lock issue (fixme)
<パス省略>ranking.py:16:0: R0205: Class 'CsvModel' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
<パス省略>ranking.py:16:0: R0903: Too few public methods (0/2) (too-few-public-methods)
<パス省略>ranking.py:26:4: W1113: Keyword argument before variable positional arguments list in the definition of __init__ function (keyword-arg-before-vararg)
<パス省略>ranking.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
<パス省略>ranking.py:37:12: C0415: Import outside toplevel (settings) (import-outside-toplevel)
<パス省略>ranking.py:53:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
<パス省略>ranking.py:63:13: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)

------------------------------------------------------------------
Your code has been rated at 8.57/10 (previous run: 8.75/10, -0.18)\
"""
print(err_msg)

print("----------------------------------------")
print("コード/docstringを書かないメソッド: No Output")
def add_num(self, x, y):
    return x + y

print("----------------------------------------")
print("9-2終了")
print("Lesson9終了")