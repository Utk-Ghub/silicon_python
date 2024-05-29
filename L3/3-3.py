print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson3 入門編 制御フロー ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("3-3 繰り返し処理でデータを一気に処理しよう")
print("-------------------------")
print("")

print("| while文、continue文、break文の使い方をしろう")
print("<while文>")
print("----------------------------------------")
print("c3_3_1/while文:")
count = 0
while count < 5:
    print(count)
    count += 1

print("----------------------------------------")
print("")

print("<break文>")
print("----------------------------------------")
print("c3_3_2/break文:無限ループによりNo Output")
# count = 0
# while True:
#     print('XXX')

print("----------------------------------------")
print("c3_3_3/break文:")
count = 0
while True:
    if count >= 5:
        break

    print(count)
    count += 1

print("----------------------------------------")
print("")

print("<continue文>")
print("----------------------------------------")
print("c3_3_4/continue文:")
count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

print("----------------------------------------")
print("")

print("| while else文の使い方を知ろう")
print("----------------------------------------")
print("c3_3_5/while else文:")
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('Done')

print("----------------------------------------")
print("c3_3_6/while else文とbreak文:")
count = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('Done')

print("----------------------------------------")
print("")

print("| ユーザーの入力を受け取るinput関数")
print("----------------------------------------")
print("c3_3_7/input関数:")
while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')

print("----------------------------------------")
print("c3_3_8/input関数での入力を数値として扱う:")
while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')

print("----------------------------------------")
print("")

print("| for文の使い方で知ろう")
print("----------------------------------------")
print("c3_3_9/while文でリストの中身を取り出す:")
some_list = list(range(1, 6))

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

print("----------------------------------------")
print("c3_3_10/for文でリストの中身を取り出す:")
some_list = list(range(1, 6))

for i in some_list:
    print(i)

print("----------------------------------------")
print("c3_3_11/for文で文字列を取り出す:")
for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    print(word)

print("----------------------------------------")
print("")

print("Point/for文とbreak文、continue文:")
print("----------------------------------------")
print("c3_3_12/for文とbreak文:")
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)

print("----------------------------------------")
print("c3_3_13/for文とcontinue文:")
for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

print("----------------------------------------")
print("")

print("| for else文の使い方を知ろう")
print("----------------------------------------")
print("c3_3_14/for else文:")
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all.')

print("----------------------------------------")
print("c3_3_15/for else文とbreak文:")
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all.')

print("----------------------------------------")
print("")

print("| 回数が決まったループにはrange関数を使おう")
print("----------------------------------------")
print("c3_3_16/数値を1つずつ出力する:")
num_list = list(range(10))

for i in num_list:
    print(i)

print("----------------------------------------")
print("c3_3_17/range関数:")
for i in range(10):
    print(i)

print("----------------------------------------")
print("c3_3_18/range関数で開始位置を指定する:")
for i in range(2, 10):
    print(i)

print("----------------------------------------")
print("c3_3_19/range関数で数値をとばして取り出す:")
for i in range(2, 10, 3):
    print(i)

print("----------------------------------------")
print("c3_3_20/range関数の活用:")
for i in range(10):
    print('hello')

print("----------------------------------------")
print("")

print("Point/rangeの数値をループ内で使わない場合:")
print("----------------------------------------")
print("c3_3_21/range関数の活用:")
for _ in range(10):
    print('hello')

print("----------------------------------------")
print("")

print("| リストのインデックスも取り出すenumerate関数")
print("----------------------------------------")
print("c3_3_22/インデックス番号を表示数する:")
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

print("----------------------------------------")
print("c3_3_23/enumerate関数:")
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

print("----------------------------------------")
print("")

print("| 複数のリストをまとめるzip関数")
print("----------------------------------------")
print("c3_3_24/複数のリストから1つずつ要素を取り出す:")
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

print("----------------------------------------")
print("c3_3_25/zip関数:")
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

print("----------------------------------------")
print("")

print("| 辞書をfor文で処理する")
print("----------------------------------------")
print("c3_3_26/辞書をfor文で処理する:")
d = {'x': 100, 'y': 200}

for v in d:
    print(v)

print("----------------------------------------")
print("c3_3_27/辞書をfor文で処理する:")
d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)

print("----------------------------------------")
print("")

print("Point/itemsの中身:")
print("----------------------------------------")
print("c3_3_28/items()の中身を確認する:")
d = {'x': 100, 'y': 200}
print(d.items())

print("----------------------------------------")
print("3-3終了")
print("Lesson3終了")