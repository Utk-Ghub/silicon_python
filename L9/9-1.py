# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson9 応用編 コードスタイル ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("9-1 Pythonのコードスタイル")
print("-------------------------")
print("")

print("| コードスタイルをチェックするツールを使おう")
print("----------------------------------------")
print("コード/コードスタイル違反: No Output")
# import roboter.controller.conversation
# roboter.controller.conversation.talk_about_restaurant()
#
# import os
# y       =1
# x = {'fasdafsd',        "dafas"}

print("----------------------------------------")
print("ターミナル/pycodestyleの実行:")
print("*** Error Output ***")
err_msg = """\
C:\<パス省略>\main.py:4:1: E402 module level import not at top of file
C:\<パス省略>\main.py:5:2: E221 multiple spaces before operator
C:\<パス省略>\main.py:5:10: E225 missing whitespace around operator
C:\<パス省略>\main.py:6:33: W292 no newline at end of file\
"""
print(err_msg)

print("----------------------------------------")
print("ターミナル/flake8の実行:")
print("*** Error Output ***")
err_msg = """\
<パス省略>/main.py:4:1: F401 'os' imported but unused
<パス省略>/main.py:4:1: E402 module level import not at top of file
<パス省略>/main.py:5:2: E221 multiple spaces before operator
<パス省略>/main.py:5:10: E225 missing whitespace around operator
<パス省略>/main.py:6:33: W292 no newline at end of file\
"""
print(err_msg)

print("----------------------------------------")
print("ターミナル/flake8の実行:")
print("*** Error Output ***")
err_msg = """\
************* Module role_model.main
<パス省略>\main.py:6:0: C0304: Final newline missing (missing-final-newline)
<パス省略>\main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
<パス省略>\main.py:1:0: E0401: Unable to import 'roboter.controller.conversation' (import-error)
<パス省略>\main.py:1:0: E0611: No name 'controller' in module 'roboter' (no-name-in-module)
<パス省略>\main.py:2:0: I1101: Module 'roboter' has no 'controller' member, but source is unavailable. Consider adding this module to extension-pkg-allow-list if you want to perform analysis based on run-time introspection of living objects. (c-extension-no-member)
<パス省略>\main.py:4:0: C0413: Import "import os" should be placed at the top of the module (wrong-import-position)
<パス省略>\main.py:5:0: C0103: Constant name "y" doesn't conform to UPPER_CASE naming style (invalid-name)
<パス省略>\main.py:4:0: C0411: standard import "import os" should be placed before "import roboter.controller.conversation" (wrong-import-order)
<パス省略>\main.py:4:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 0.00/10\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("| コードスタイルのルールを知ろう")
print("<行の終わりにセミコロンはつけない>")
print("----------------------------------------")
print("コード/行の終わりにセミコロンをつける: No Output")
x = 1;
y = 2;

print("----------------------------------------")
print("")

print("<行の長さは80文字以内に>")
print("----------------------------------------")
print("コード/行の終わりにセミコロンをつける: No Output")
x = 1;
y = 2;

print("----------------------------------------")
print("コード/1行が長くなる場合: No Output")
print("コード/コメントにURLを記載する場合: No Output")
def test_runc(x, y, z,
              fadalskfdweoiasldkfaslkjgaslk='test'):
    """

    :param x:
    :param y:
    :param z:
    :param fadalskfdweoiasldkfaslkjgaslk:
    :return:

    See details at http://xxxxxxxxxx.com/document/fajaskldjfjkasdkflaslkdfasdlkjfaslkdjfalkjfa
    """
    pass

print("----------------------------------------")
print("")

print("<if文の条件における()の使い方>")
print("----------------------------------------")
print("コード/if文の条件における()の使い方:")
if (x and y) or (x or y):
    print('exist')

print("----------------------------------------")
print("コード/if文の条件における()の使い方(悪い例):")
if (x and y):
    print('exist')

if (x):
    print('exist')

print("----------------------------------------")
print("コード/辞書型の中のインデント: No Output")
x = {
    'test': 'sss'
}

print("----------------------------------------")
print("")

print("<コロンやカンマの後ろのスペース>")
print("----------------------------------------")
print("コード/コロンの後ろのスペース: No Output")
x = {'test': 'sss'}
print("----------------------------------------")
print("コード/カンマの後ろのスペース: No Output")
def test_func(x, y, z):
    pass

print("----------------------------------------")
print("コード/コロンの後ろのスペース: No Output")
x, y = y, x

print("----------------------------------------")
print("")

print("<演算子の前後のスペース>")
print("----------------------------------------")
print("コード/演算子の前後のスペース: No Output")
# x = y
# x + y

print("----------------------------------------")
print("コード/演算子の前後のスペース: No Output")
def test_func(x, y, z='test'):
    pass

print("----------------------------------------")
print("コード/イコールの位置をそろえる: No Output")
x     = 100
yyyyy = 200

print("----------------------------------------")
print("コード/演算子の前後のスペース: No Output")
x     = 100
yyyyy = 200
zzzzzzzzzzzzzzzz = 300

print("----------------------------------------")
print("コード/演算子の前後のスペース: No Output")
x = 100
yyyyy = 200
zzzzzzzzzzzzzzzz = 300

print("----------------------------------------")
print("")

print("<行間の空け方>")
print("----------------------------------------")
print("コード：console.py/関数やクラスの行間: No Output")
# class NoTemplateError(Exception):
#     """No Template Error"""
#
#
# def find_template(temp_file):
#     """Find for template file in the given location.
#
#     Returns:
#         str: The template file path
#
#     Raises:
#         NoTemplateError: If the file does not exist.
#     """
#     template_dir_path = get_template_dir_path()
#     temp_file_path = os.path.join(template_dir_path, temp_file)
#     if not os.path.exists(temp_file_path):
#         raise NoTemplateError('Could not find {}'.format(temp_file))
#     return temp_file_path
#
#
# def get_template(template_file_path, color=None):

print("----------------------------------------")
print("コード：robot.py/メソッドの行間: No Output")
# class RestaurantRobot(Robot):
#     """Handle data model on restaurant."""
#
#     def __init__(self, name=DEFAULT_ROBOT_NAME):
#         super().__init__(name=name)
#         self.ranking_model = ranking.RankingModel()
#
#     def _hello_decorator(func):
#         """Decorator to say a greeting if you are not greeting the user."""
#         def wrapper(self):
#             if not self.user_name:
#                 self.hello()
#             return func(self)
#         return wrapper
#
#     @_hello_decorator
#     def recommend_restaurant(self):

print("----------------------------------------")
print("コード：robot.py/メソッドの行間: No Output")
# """Defined a robot model """
# from roboter.models import ranking
# from roboter.views import console
#
#
# DEFAULT_ROBOT_NAME = 'Roboko'

print("----------------------------------------")
print("")

print("<シングルクォートとダブルクォート>")
print("----------------------------------------")
print("コード/シングルクォートとダブルクォート: No Output")
print('fddsaafs')
print("fasf'fasda")

print("----------------------------------------")
print("コード/シングルクォートとダブルクォート: No Output")
print("ddasaf {} asfsadfa".format('test'))

print("----------------------------------------")
print("")

print("<クラスや関数など命名規則>")
print("----------------------------------------")
print("コード：robot.py/クラス名: No Output")
# class RestaurantRobot(Robot):

print("----------------------------------------")
print("コード：robot.py/関数名: No Output")
# def recommend_restaurant(self):

print("----------------------------------------")
print("コード/プロパティ名: No Output")
@property
def user_name(self):
    return self._user_name

print("----------------------------------------")
print("コード：robot.py/グローバル変数: No Output")
# DEFAULT_ROBOT_NAME = 'Roboko'

print("----------------------------------------")
print("9-1終了")