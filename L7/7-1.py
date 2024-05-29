print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson7 入門編 ファイル操作とシステム ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("7-1 ファイルの基本的操作")
print("-------------------------")
print("")

print("| ファイルを作成しよう")
print("----------------------------------------")
print("c7_1_1/ファイルを作成して書き込む:")
f = open('test.txt', 'w')
f.write('test')
f.close()

# 下記コード、test.txtに何が書かれるかを表示するため独自に追加
f = open('test.txt', 'r')
txt = f.read()
f.close()
print(txt)

print("----------------------------------------")
print("c7_1_2/ファイルを作成して書き込む:")
f = open('test.txt', 'w')
f.write('Test')
f.close()

# 下記コード、test.txtに何が書かれるかを表示するため独自に追加
f = open('test.txt', 'r')
txt = f.read()
f.close()
print(txt)

print("----------------------------------------")
print("c7_1_3/ファイルを作成して書き込む:")
f = open('test.txt', 'a')
f.write('Test')
f.close()

# 下記コード、test.txtに何が書かれるかを表示するため独自に追加
f = open('test.txt', 'r')
txt = f.read()
f.close()
print(txt)

print("----------------------------------------")
print("")

print("Point/print関数でもファイルに書き込める:")
print("----------------------------------------")
print("c7_1_4/ファイルを作成して書き込む:")
f = open('test.txt', 'w')
f.write('Test\n')
print('I am print', file=f)
f.close()

# 下記コード、test.txtに何が書かれるかを表示するため独自に追加
f = open('test.txt', 'r')
txt = f.read()
f.close()
print(txt)

print("----------------------------------------")
print("c7_1_5/ファイルを作成して書き込む:")
f = open('test.txt', 'w')
f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#',end='!', file=f)
f.close()

# 下記コード、test.txtに何が書かれるかを表示するため独自に追加
f = open('test.txt', 'r')
txt = f.read()
f.close()
print(txt)

print("----------------------------------------")
print("")

print("| with文を使ってファイルを開こう")
print("----------------------------------------")
print("c7_1_6/with文でファイルをopenする:")
with open('test.txt', 'w') as f:
    f.write('Test')

# 下記コード、test.txtに何が書かれるかを表示するため独自に追加
with open('test.txt', 'r') as f:
    print(f.read())

print("----------------------------------------")
print("")

print("| ファイルの内容を読み込もう")
print("----------------------------------------")
print("c7_1_7/ファイルを用意する:")
print("c7_1_8/ファイルを読み込む:")
s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as f:
    print(f.read())

print("----------------------------------------")
print("c7_1_9/ファイルを1行ずつ読み込む:")
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

print("----------------------------------------")
print("c7_1_10/ファイルを1行ずつ読み込む:")
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break

print("----------------------------------------")
print("c7_1_11/ファイルをチャンクごとに読み込む:")
with open('test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.readline(chunk)
        print(line)
        if not line:
            break

print("----------------------------------------")
print("")

print("| ファイル内の位置を移動しよう")
print("----------------------------------------")
print("c7_1_12/ファイルの現在位置を確認する:")
with open('test.txt', 'r') as f:
    print(f.tell())

print("----------------------------------------")
print("c7_1_13/ファイルの現在位置を確認する:")
with open('test.txt', 'r') as f:
    print(f.tell())
    print(f.read(1))

print("----------------------------------------")
print("c7_1_14/seek:")
with open('test.txt', 'r') as f:
    f.seek(5)
    print(f.read(1))

print("----------------------------------------")
print("c7_1_15/seek:")
with open('test.txt', 'r') as f:
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))

print("----------------------------------------")
print("")

print("| 書き込みと読み込みを同時に行いたいとき")
print("----------------------------------------")
print("c7_1_16/'w'でopenしたファイルを読み込む:")
# s = """\
# AAA
# BBB
# CCC
# DDD
# """
# with open('test.txt', 'w') as f:
#     f.write(s)
#     print(f.read())

print("*** Error Output ***")
err_msg = """\
    print(f.read())
          ^^^^^^^^
io.UnsupportedOperation: not readable\
"""
print(err_msg)

print("----------------------------------------")
print("c7_1_17/'w+'でopen: No Output")
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w+') as f:
    f.write(s)
    print(f.read())

print("----------------------------------------")
print("c7_1_18/'w'でopenしたファイルを読み込む: No Output")
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

print("----------------------------------------")
print("c7_1_19/'r+'でopen:")
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)

print("----------------------------------------")
print("c7_1_20/'r+'でopen:")
# with open('test2.txt', 'r+') as f:
#     print(f.read())
#     f.seek(0)
#     f.write(s)
print("*** Error Output ***")
err_msg = """\
    with open('test2.txt', 'r+') as f:
         ^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'test2.txt'\
"""
print(err_msg)

print("----------------------------------------")
print("7-1終了")

import os

while True:
    file_remover = input('作成したファイルを削除しますか（y/n）：')
    if file_remover == 'y':
        os.remove('test.txt')
        break
    elif file_remover == 'n':
        break
    else:
        print("yかnを入力してください")