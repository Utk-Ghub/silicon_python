print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson4 入門編 関数と例外処理 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("4-3 内包表記でリストをシンプルに生成しよう")
print("-------------------------")
print("")

print("| リスト内包表記の書き方を知ろう")
print("----------------------------------------")
print("c4_3_1/タプルから要素を取り出してリストにする:")
t = tuple(range(1, 6))

r = []
for i in t:
    r.append(i)
print(r)

print("----------------------------------------")
print("c4_3_2/リスト内包表記:")
t = tuple(range(1, 6))

r = [i for i in t]
print(r)

print("----------------------------------------")
print("c4_3_3/タプルから偶数の要素を取り出してリストにする:")
t = tuple(range(1, 6))

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

r = [i for i in t if i % 2 == 0]

print(r)

print("----------------------------------------")
print("")

print("<2つのforループのリスト内包表記>")
print("----------------------------------------")
print("c4_3_4/2つのforループでリストを作成する:")
t = tuple(range(1, 6))
t2 = tuple(range(5, 11))

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

print("----------------------------------------")
print("c4_3_4/2つのforループのリスト内包表記:")
t = tuple(range(1, 6))
t2 = tuple(range(5, 11))

r = [i * j for i in t for j in t2]

print(r)

print("----------------------------------------")
print("")

print("| 辞書包括表記の書き方を知ろう")
print("----------------------------------------")
print("c4_3_6/2つのリストから辞書を作成する:")
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

print("----------------------------------------")
print("c4_3_7/辞書包括表記:")
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {x:y for x, y in zip(w, f)}

print(d)

print("----------------------------------------")
print("")

print("| 集合内包表記の書き方を知ろう")
print("----------------------------------------")
print("c4_3_8/forループで集合を作成する:")
s = set()

for i in range(10):
    s.add(i)

print(s)

print("----------------------------------------")
print("c4_3_9/集合内包表記:")
s = {i for i in range(10)}
print(s)

print("----------------------------------------")
print("c4_3_10/if文を使った集合内包表記:")
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

print("----------------------------------------")
print("")

print("| ジェネレーター内包表記の書き方を知ろう")
print("----------------------------------------")
print("c4_3_11/forループでジェネレーターを作成する:")
def g():
    for i in range(10):
        yield i

g = g()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("----------------------------------------")
print("c4_3_12/ジェネレーター内包表記:")
g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("----------------------------------------")
print("")

print("Point/内包表記でタプルを作成する:")
print("----------------------------------------")
print("c4_3_13/内包表記でタプルを作成する:")
g = tuple(i for i in range(10))
print(type(g))
print(g)

print("----------------------------------------")
print("")

print("----------------------------------------")
print("c4_3_14/if文を使ったジェネレーター内包表記:")
g = (i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)

print("----------------------------------------")
print("4-3終了")