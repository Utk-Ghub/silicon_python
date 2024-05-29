print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson3 入門編 制御フロー ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("3-2 条件に応じて処理を分岐させよう")
print("-------------------------")
print("")

print("| if文、else文、elif文の使い方を知ろう")
print("<if文>")
print("----------------------------------------")
print("c3_2_1/:if文")
x = -10

if x < 0:
    print('negative')

print("----------------------------------------")
print("c3_2_2/if文の条件にあてはまらない場合: No Output")
x = 10

if x < 0:
    print('negative')

print("----------------------------------------")
print("")

print("<else文>")
print("----------------------------------------")
print("c3_2_3/else文:")
x = 10

if x < 0:
    print('negative')
else:
    print('positive')

print("----------------------------------------")
print("")

print("<elif文>")
print("----------------------------------------")
print("c3_2_4/:elif文")
x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

print("----------------------------------------")
print("c3_2_5/:複数のelif文")
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

print("----------------------------------------")
print("")

print("Point/複数の条件にあてはまる場合:")
print("----------------------------------------")
print("c3_2_6/複数のelif文:")
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10000000000')
elif x == 10:
    print('10')
else:
    print('positive')

print("----------------------------------------")
print("")

print("<if文のネスト>")
print("----------------------------------------")
print("c3_2_7/if文のネスト:")
a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

print("----------------------------------------")
print("")

print("Point/ネストしたif文のインデント:")
print("----------------------------------------")
print("c3_2_8/ネストしたif文のインデント:")
# a = 5
# b = 10
#
# if a > 0:
#     print('a is positive')
#     　if b > 0:
#         print('b is positive')
print("*** Error Output ***")
err_msg = """\
    　if b > 0:
    ^
SyntaxError: invalid non-printable character U+3000\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("| デバッガーを使って確認してみよう")
print("----------------------------------------")
print("No Output")

print("----------------------------------------")
print("")

print("| 比較演算子と論理演算子の使い方を知ろう")
print("<比較演算子>")
print("----------------------------------------")
print("c3_2_9/比較演算子==:")
a = 1
b = 1

print(a == b)

print("----------------------------------------")
print("c3_2_10/比較演算子!=:")
a = 1
b = 1
print(a != b)

print("----------------------------------------")
print("c3_2_11/比較演算子<:")
a = 1
b = 2
print(a < b)

print("----------------------------------------")
print("c3_2_12/比較演算子<=:")
a = 2
b = 2
print(a <= b)

print("----------------------------------------")
print("")

print("<論理演算子>")
print("----------------------------------------")
print("c3_2_13/論理演算子and:")
a = 2
b = 2
if a > 0 and b > 0:
    print('a and b are positve')

print("----------------------------------------")
print("")

print("Point/andを使わない場合:")
print("----------------------------------------")
print("c3_2_14/andを使わない場合:")
a = 2
b = 2
# a > 0 も b > 0 も真であれば真
if a > 0:
    if b > 0:
        print('a and b are positve')

print("----------------------------------------")
print("c3_2_15/論理演算子or:")
a = 1
b = -1
# a > 0 または b > 0 が真であれば真
if a > 0 or b > 0:
    print('a or b are positive')

print("----------------------------------------")
print("")

print("Point/orを使わない場合:")
print("----------------------------------------")
print("c3_2_16/orを使わない場合:")
a = 1
b = -1
# a > 0 または b > 0 が真であれば真
if a > 0:
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')

print("----------------------------------------")
print("")

print("| inとnotはこうやって使う")
print("----------------------------------------")
print("c3_2_17/in:")
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

print("----------------------------------------")
print("c3_2_18/not:")
y = [1, 2, 3]
x = 1

if 100 not in y:
    print('not in')

print("----------------------------------------")
print("c3_2_19/not:")
a = 1
b = 10

if not a == b:
    print('Not equal')

print("----------------------------------------")
print("c3_2_20/notではなく!=:")
a = 1
b = 10

if a != b:
    print('Not equal')

print("----------------------------------------")
print("")

print("<notのよくある使いどころ>")
print("----------------------------------------")
print("c3_2_21/Boolean型の変数をそのままif文に書く:")
is_ok = True

if is_ok:
    print('hello')

print("----------------------------------------")
print("c3_2_22/Boolean型の変数をnotで否定する: No Output")
is_ok = True

if not is_ok:
    print('hello')

print("----------------------------------------")
print("")

print("| 値が入っていないことを判定するテクニック")
print("----------------------------------------")
print("c3_2_23/Boolean型の変数をそのままif文に書く:True")
is_ok = True

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_24/変数に数値が入っていた場合のifの判定:1")
is_ok = 1

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_25/変数に0が入っていた場合のifの判定:0")
is_ok = 0

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_26/変数に数値が入っていた場合のifの判定:10020")
is_ok = 10020

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_27/変数に文字列が入っていた場合のifの判定:空文字列")
is_ok = ''

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_28/変数に文字列が入っていた場合のifの判定:afdafdsafdsa")
is_ok = 'afdafdsafdsa'

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_29/リストが空場合のifの判定:[]")
is_ok = []

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_30/リストに要素が入っていた場合のifの判定:[range(1, 5)]")
is_ok = list(range(1, 5))

if is_ok:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("c3_2_31/lenを使ったリストの中身の判定:[range(1, 5)]")
is_ok = list(range(1, 5))

if len(is_ok) > 0:
    print('OK!')
else:
    print('No!')

print("----------------------------------------")
print("")

print("| Noneを判定するテクニック")
print("----------------------------------------")
print("c3_2_32/Noneをhelpで確認する:")
is_empty = None
print(help(is_empty))

print("----------------------------------------")
print("c3_2_33/==によるNoneであるかどうかの判定:")
is_empty = None

if is_empty == None:
    print('None!!!')

print("----------------------------------------")
print("c3_2_34/isによるNoneであるかどうかの判定:")
is_empty = None

if is_empty is None:
    print('None!!!')

print("----------------------------------------")
print("c3_2_35/Noneではないことの判定:No Output")
is_empty = None

if is_empty is not None:
    print('None!!!')

print("----------------------------------------")
print("c3_2_36/==による比較:")
print(1 == True)

print("----------------------------------------")
print("c3_2_37/isによる比較:")
print(1 is True)
print(True is True)

print("----------------------------------------")
print("c3_2_38/isによる比較:")
print(None is None)

print("----------------------------------------")
print("3-2終了")