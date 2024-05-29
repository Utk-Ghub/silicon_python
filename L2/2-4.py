print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("■ Lesson2 入門編 データ構造 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  ■")
print("")
print("2-4 データ同士の演算ができる集合")
print("-------------------------")
print("")

print("| 集合型の基本を知ろう")
print("----------------------------------------")
print("対話型/集合の作成:")
a = {1, 2, 3, 4, 5, 6}
print(a)
print(type(a))

print("----------------------------------------")
print("対話型/集合の差:")
print(a)
b = {2, 3, 3, 6, 7}
print(b)
print(a - b)

print("----------------------------------------")
print("対話型/集合の差:")
print(b - a)

print("----------------------------------------")
print("対話型/集合の積:")
print(a & b)

print("----------------------------------------")
print("")

print("Point/集合に+を使うとエラーになる:")
print("----------------------------------------")
print("対話型/+を使う:")
# print(a + b)
print("*** Error Output ***")
err_msg = """\
    print(a + b)
          ~~^~~
TypeError: unsupported operand type(s) for +: 'set' and 'set'\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("----------------------------------------")
print("対話型/集合の和:")
print(a | b)

print("----------------------------------------")
print("対話型/集合の対称差:")
print(a ^ b)

print("----------------------------------------")
print("")

print("| 集合のメソッドを使おう")
print("----------------------------------------")
print("対話型/インデックス:")
s = set(range(1, 6))
# s[0]
print("*** Error Output ***")
err_msg = """\
    s[0]
    ~^^^
TypeError: 'set' object is not subscriptable\
"""
print(err_msg)

print("----------------------------------------")
print("対話型/addメソッド:")
s.add(6)
print(s)
s.add(6)
print(s)

print("----------------------------------------")
print("対話型/removeメソッド:")
s.remove(6)
print(s)

print("----------------------------------------")
print("対話型/clearメソッド:")
s.clear()
print(s)

print("----------------------------------------")
print("")

print("| 集合はこうやって使う")
print("----------------------------------------")
print("c2_4_1/共通の友人を求める:")
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

print("----------------------------------------")
print("c2_4_2/リストから重複を削除する:")
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

print("----------------------------------------")
print("2-4終了")
print("Lesson2終了")