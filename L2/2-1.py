print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("■ Lesson2 入門編 データ構造 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("")
print("2-1 複数データを並列にまとめる")
print("-------------------------")
print("")

print("| リストの基本を知ろう")
print("----------------------------------------")
print("対話型/リストの作成:")
l = [1, 20, 4, 50, 2, 1, 2]
print(l)

print("----------------------------------------")
print("対話型/インデックス:")
print(l[0])
print(l[1])

print("----------------------------------------")
print("対話型/負のインデックス:")
print(l[-1])
print(l[-2])

print("----------------------------------------")
print("対話型/スライスを試す:")
print(l[0:2])
print(l[:2])

print("----------------------------------------")
print("対話型/スライスを試す:")
print(l[2:5])

print("----------------------------------------")
print("対話型/スライスを試す:")
print(l[2:])
print(l[:])

print("----------------------------------------")
print("")

print('Point/存在しないインデックスを指定するとどうなる？:')
print("----------------------------------------")
print("対話型/IndexError:")
# print(l)
# print(l[100])
print("*** Error Output ***")
err_msg = """\
    print(l[100])
          ~^^^^^
IndexError: list index out of range\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("----------------------------------------")
print("対話型/スライスを試す:")
n = list(range(1, 11))
print(n)
print(n[::2])

print("----------------------------------------")
print("対話型/スライスを試す:")
print(n[::-1])

print("----------------------------------------")
print("")

print("<リストと関数>")
print("----------------------------------------")
print("対話型/len関数をを試す:")
print(len(l))

print("----------------------------------------")
print("対話型/type関数をを試す:")
print(type(l))

print("----------------------------------------")
print("対話型/list関数をを試す:")
print(list('abcdefg'))

print("----------------------------------------")
print("")

print("<リストのネスト（入れ子）>")
print("----------------------------------------")
print("対話型/リストのネスト:")
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print("----------------------------------------")
print("対話型/ネストしたリストのインデックス:")
print(x[0])
print(x[1])

print("----------------------------------------")
print("対話型/ネストしたリストのインデックス:")
print(x[0][1])
print(x[1][2])

print("----------------------------------------")
print("")

print("<リストのデータを操作しよう>")
print("----------------------------------------")
print("対話型/リストの作成:")
s = list('abcdefg')
print(s)

print("----------------------------------------")
print("対話型/リストの書き換え:")
print(s[0])
s[0] = 'X'
print(s)

print("----------------------------------------")
print("対話型/スライスで書き換え:")
print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)

print("----------------------------------------")
print("対話型/空のリストを入れる:")
s[2:5] = []
print(s)

print("----------------------------------------")
print("対話型/すべて空にする:")
s[:] = []
print(s)

print("----------------------------------------")
print("")

print("<メソッドによる挿入／削除>")
print("----------------------------------------")
print("対話型/appendメソッド:")
n = list(range(1, 11))
n.append(100)
print(n)

print("----------------------------------------")
print("対話型/insertメソッド:")
n.insert(0, 200)
print(n)

print("----------------------------------------")
print("対話型/popメソッド:")
print(n.pop())
print(n)

print("----------------------------------------")
print("対話型/最初を取り出す:")
print(n.pop(0))
print(n)

print("----------------------------------------")
print("対話型/最初を削除する:")
del n[0]
print(n)

print("----------------------------------------")
print("対話型/del文:")
# del n
# print(n)
print("*** Error Output ***")
err_msg = """\
    print(n)
          ^
NameError: name 'n' is not defined\
"""
print(err_msg)

print("----------------------------------------")
print("対話型/removeメソッド:")
n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)

print("----------------------------------------")
print("対話型/ValueError:")
n.remove(2)
n.remove(2)
print(n)
# n.remove(2)
print("*** Error Output ***")
err_msg = """\
    n.remove(2)
ValueError: list.remove(x): x not in list\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("<リストの結合>")
print("----------------------------------------")
print("対話型/リストの結合:")
a = list(range(1, 6))
b = list(range(6, 11))
print(a)
print(b)
x = a + b
print(x)

print("----------------------------------------")
print("対話型/リストの結合:")
print(a)
print(b)
a += b
print(a)

print("----------------------------------------")
print("対話型/extendメソッド:")
x = list(range(1, 6))
y = list(range(6, 11))
x.extend(y)
print(x)

print("----------------------------------------")
print("")

print("<リストのさまざまなメソッドを使おう>")
print("----------------------------------------")
print("c2_1_1/indexメソッド:")
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))

print("----------------------------------------")
print("c2_1_2/indexメソッド:")
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print("----------------------------------------")
print("c2_1_3/countメソッド:")
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.count(3))

print("----------------------------------------")
print("c2_1_4/in演算子による包含判定:")
r = [1, 2, 3, 4, 5, 1, 2, 3]
if 5 in r:
    print('exist')

print("----------------------------------------")
print("")

print("<リストのソート（並べ替え）>")
print("----------------------------------------")
print("c2_1_5/sortメソッド:")
r = [1, 2, 3, 4, 5, 1, 2, 3]
r.sort()
print(r)

print("----------------------------------------")
print("c2_1_6/逆順のソート:")
r = [1, 2, 3, 4, 5, 1, 2, 3]
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

print("----------------------------------------")
print("")

print("<文字列の分割>")
print("----------------------------------------")
print("c2_1_7/splitメソッド:")
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

print("----------------------------------------")
print("")

print("Point/区切り文字が存在しない場合")
print("----------------------------------------")
print("c2_1_8/splitメソッド:")
s = 'My name is Mike.'
to_split = s.split('!!!')
print(to_split)

print("----------------------------------------")
print("")

print("----------------------------------------")
print("c2_1_10/splitメソッド:")
s = 'My name is Mike.'
to_split = s.split('!!!')
print(to_split)
x = ' '.join(to_split)
print(x)

print("----------------------------------------")
print("c2_1_10/help関数:")
print(help(list))

print("----------------------------------------")
print("")

print("| リストのコピーに注意！")
print("----------------------------------------")
print("c2_1_11/コピー（代入）:")
i = list(range(1, 5))
j = i
j[0] = 100
print('j =', j)
print('i =', i)

print("----------------------------------------")
print("c2_1_12/copyメソッドを試す:")
x = list(range(1, 6))
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

print("----------------------------------------")
print("")

print("<値渡しと参照渡しの確認>")
print("----------------------------------------")
print("c2_1_12/オブジェクトidの確認:")
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

print("----------------------------------------")
print("c2_1_13/オブジェクトidの確認:")
X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)

print("----------------------------------------")
print("")

print("Point/スライスによるコピー")
print("----------------------------------------")
print("c2_1_15/スライスによるコピー:")
x = list(range(1, 6))
y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)

print("----------------------------------------")
print("")

print("| リストの具体的な利用例")
print("----------------------------------------")
print("対話型/空のリストの作成:")
seat = []
min = 0
max = 5
print(min <= len(seat) < max)
print(len(seat))

seat.append('p')
print(min <= len(seat) < max)
print(len(seat))

seat.append('p')
print(min <= len(seat) < max)
print(len(seat))

seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
print(len(seat))

seat.append('p')
print(min <= len(seat) < max)
print(len(seat))

print(seat.pop(0))
print(min <= len(seat) < max)

print("----------------------------------------")
print("2-1終了")