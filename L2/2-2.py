print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("■ Lesson2 入門編 データ構造 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("")
print("2-2 変更できないリスト？いえ、タプルです")
print("-------------------------")
print("")

print("| タプルの基本を知ろう")
print("----------------------------------------")
print("対話型/タプルの作成:")
t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

print("----------------------------------------")
print("対話型/タプルに代入:")
# t[0] = 100
print("*** Error Output ***")
err_msg = """\
    t[0] = 100
    ~^^^
TypeError: 'tuple' object does not support item assignment\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("<タプルのメソッド>")
print("----------------------------------------")
print("対話型/インデックスやスライス、メソッド:")
print(t[0])
print(t[-2])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))

print("----------------------------------------")
print("")

print("Point/タプルにリストを入れる")
print("----------------------------------------")
print("対話型/タプルにリストを入れる:")
t = ([1, 2, 3], [4, 5, 6])
# print(t[0] = [1])
# t[0] = [1]
print("*** Error Output ***")
err_msg = """\
    t[0] = [1]
    ~^^^
TypeError: 'tuple' object does not support item assignment\
"""
print(err_msg)
print("")

t[0][0] = 100
print(t)

print("----------------------------------------")
print("")

print("<タプルの作成方法>")
print("----------------------------------------")
print("対話型/()を省略してタプルを作成):")
t = 1, 2, 3
print(type(t))
print(t)

print("----------------------------------------")
print("")

print("Point/カンマをつけるとタプルになる:")
print("----------------------------------------")
print("対話型/カンマをつけて変数に代入:")
t = 1,
print(t)
print(type(t))

print("----------------------------------------")
print("対話型/()を使ったときの挙動:")
t = ()
print(t)
print(type(t))
t = (1)
print(t)
print(type(t))

print("----------------------------------------")
print("対話型/1つだけ要素が入ったタプル:")
t = (1,)
print(t)
print(type(t))

print("----------------------------------------")
print("")

print("<タプルの結合>")
print("----------------------------------------")
print("対話型/タプルの結合:")
new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)

print("----------------------------------------")
print("対話型/タプルの結合:")
# new_tuple = (1) + (4, 5, 6)
# print(new_tuple)
print("*** Error Output ***")
err_msg = """\
    new_tuple = (1) + (4, 5, 6)
                ~~^~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'\
"""
print(err_msg)
print("")

new_tuple = (1,) + (4, 5, 6)
print(new_tuple)

print("----------------------------------------")
print("")

print("| タプルのアンパッキング")
print("----------------------------------------")
print("c2_2_1/タプルのアンパッキング:")
num_tuple = (10, 20)
x, y = num_tuple
print(x, y)

print("----------------------------------------")
print("c2_2_2/タプルのアンパッキング:")
x, y = 10, 20
print(x, y)

print("----------------------------------------")
print("")

print("Point/変数が多いときのアンパッキング")
print("----------------------------------------")
print("c2_2_3/変数が多いときの宣言の仕方:")
a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
print("c2_2_3: No output")

print("----------------------------------------")
print("c2_2_4/変数が多いときの宣言の仕方:")
a = 'Mike'
b = '1'
c = '1'
d = '1'
e = 'e'
f = 'f'

print("----------------------------------------")
print("c2_2_4: No output")

print("----------------------------------------")
print("c2_2_5/変数の入れ替え:")
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

print("----------------------------------------")
print("c2_2_6/変数の入れ替え:")
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

print("----------------------------------------")
print("")

print("| タプルはこうやって使う")
print("----------------------------------------")
print("c2_2_7/選択問題の作成:")
choose_from_three = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('C')
print(choose_from_three)
print(answer)

print("----------------------------------------")
print("c2_2_8/選択問題の作成（失敗例）:")
choose_from_three = ['A', 'B', 'C']
answer = []
choose_from_three.append('A')
choose_from_three.append('C')
print(choose_from_three)

print("----------------------------------------")
print("c2_2_9/選択問題の作成:")
# choose_from_three = ('A', 'B', 'C')
# answer = []
# choose_from_three.append('A')
# choose_from_three.append('C')
print("*** Error Output ***")
err_msg = """\
print(err_msg)
    choose_from_three.append('A')
    ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'\
"""
print(err_msg)

print("----------------------------------------")
print("2-2終了")