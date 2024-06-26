print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("■ Lesson2 入門編 データ構造 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("")
print("2-3 キーと値をセットで記憶する辞書型")
print("-------------------------")
print("")

print("| 辞書型の基本を知ろう")
print("----------------------------------------")
print("対話型/辞書型の作成:")
d = {'x': 10, 'y': 20}
print(d)

print("----------------------------------------")
print("対話型/辞書型の確認:")
print(type(d))

print("----------------------------------------")
print("対話型/辞書型の値を出力:")
print(d['x'])
print(d['y'])

print("----------------------------------------")
print("")

print("<辞書型の操作>")
print("----------------------------------------")
print("対話型/辞書型に値を代入:")
d['x'] = 100
print(d)
d['x'] = 'XXXXX'
print(d)

print("----------------------------------------")
print("対話型/辞書型に値を追加:")
d['z'] = 200
print(d)

print("----------------------------------------")
print("")

print("Point/キーに数字を設定する")
print("----------------------------------------")
d[1] = 10000
print(d)

print("----------------------------------------")
print("")

print("対話型/辞書型の作成:")
print("----------------------------------------")
print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))

print("----------------------------------------")
print("")

print("| 辞書型のメソッドを使おう")
print("----------------------------------------")
print("対話型/help関数:")
d = {'x': 10, 'y': 20}
print(d)
print(help(d))

print("----------------------------------------")
print("対話型/keysメソッド:")
print(d.keys())

print("----------------------------------------")
print("対話型/valuesメソッド:")
print(d.values())

print("----------------------------------------")
print("対話型/updateメソッドを試す:")
d2 = {'x': 1000, 'j': 500}
print(d)
print(d2)

print("----------------------------------------")
print("対話型/updateメソッドを試す:")
d.update(d2)
print(d)

print("----------------------------------------")
print("対話型/getメソッド:")
print(d['x'])
print(d.get('x'))

print("----------------------------------------")
print("対話型/getメソッド:")
# print(d['z'])
print("*** Error Output ***")
err_msg = """\
    print(d['z'])
          ~^^^^^
KeyError: 'z'\
"""
print(err_msg)
print("")
r = d.get('z')
print(type(r))

print("----------------------------------------")
print("対話型/popメソッド:")
print(d)
print(d.pop('x'))
print(d)

print("----------------------------------------")
print("対話型/del文:")
print(d)
del d['y']
print(d)

print("----------------------------------------")
print("対話型/del文:")
# del d
# d
print("*** Error Output ***")
err_msg = """\
    d
NameError: name 'd' is not defined. Did you mean: 'd2'?\
"""
print(err_msg)

print("----------------------------------------")
print("対話型/clearメソッド:")
d = {'x': 10, 'y': 20}
d.clear()
print(d)

print("----------------------------------------")
print("対話型/キーの存在確認:")
d = {'a': 100, 'b': 200}
print('a' in d)
print('j' in d)

print("----------------------------------------")
print("")

print("| 辞書のコピーに注意")
print("----------------------------------------")
print("c2_3_1/辞書のコピー（代入）:")
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

print("----------------------------------------")
print("c2_3_2/copyメソッドを試す:")
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

print("----------------------------------------")
print("")

print("| 辞書はこうやって使う")
print("----------------------------------------")
print("c2_3_3/果物の値段を辞書で作成:")
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}
print(fruits['apple'])

print("----------------------------------------")
print("")

print("<リストとの違い>")
print("----------------------------------------")
print("c2_3_4/果物の値段をリストで作成:")
l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]
print(l)

print("----------------------------------------")
print("2-3終了")