print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson7 入門編 ファイル操作とシステム ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("7-2 ファイルの便利な活用方法")
print("-------------------------")
print("")

print("| テンプレートを使って文章を作ってみよう")
print("----------------------------------------")
print("c7_2_1/テンプレートを使って文章を作成:")
import string

s = """\
Hi $name
$contents
Have a good day
"""

t = string.Template(s)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)

print("----------------------------------------")
print("")

print("<テンプレートの活用方法>")
print("----------------------------------------")
print("c7_2_2/テキストファイルをテンプレートとして読み込む:")
import string

with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)

print("----------------------------------------")
print("")

print("| CSVファイルを操作しよう")
print("<cSVファイルへの書き込み>")
print("----------------------------------------")
print("c7_2_3/CSVファイルを作成する:")
import csv

with open('test.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()

# 下記コード、test.csvに何が書かれるかを表示するため独自に追加
with open('test.csv', 'r') as c:
    print(c.read())

print("----------------------------------------")
print("c7_2_4/CSVファイルを作成する:No Output")
import csv

with open('test.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': '1'})
    writer.writerow({'Name': 'B', 'Count': '2'})

# 下記コード、test.csvに何が書かれるかを表示するため独自に追加
with open('test.csv', 'r') as c:
    print(c.read())

print("----------------------------------------")
print("")

print("<CSVファイルの読み込み>")
print("----------------------------------------")
print("c7_2_5/CSVファイルを読み込む:")
import csv

with open('test.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': '1'})
    writer.writerow({'Name': 'B', 'Count': '2'})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])

print("----------------------------------------")
print("")

print("| さまざまなファイル操作を試そう")
print("----------------------------------------")
print("c7_2_6/ファイルの存在を確認する:")
import os
print(os.path.exists('test.txt'))

print("----------------------------------------")
print("c7_2_7/ファイルかどうかを確認する:")
import os
print(os.path.isfile('test.txt'))

print("----------------------------------------")
print("c7_2_8/ディレクトリかどうかを確認する:")
import os
print(os.path.isdir('design'))

print("----------------------------------------")
print("")

print("<ファイル名の変更>")
print("----------------------------------------")
print("c7_2_9/ファイル名を変更する: No Output")
# 1ファイルで何度も実行するため
# test.txtがなければ作成する
if not os.path.isfile('test.txt'):
    with open('test.txt', 'w') as f:
        f.write('test')
os.rename('test.txt', 'renamed.txt')

print("----------------------------------------")
print("")

print("<シンボリックリンクやディレクトリ、ファイルの作成>")
print("----------------------------------------")
print("c7_2_10/シンボリックリンクを作成する: No Output")
# Windowsの場合、開発者モードにしないとエラーが出る
os.symlink('renamed.txt', 'symlink.txt')

print("----------------------------------------")
print("c7_2_11/ディレクトリを作成する: No Output")
os.mkdir('test_dir')

print("----------------------------------------")
print("c7_2_12/ディレクトリを削除する: No Output")
os.rmdir('test_dir')

print("----------------------------------------")
print("c7_2_13/中身が空のファイルを作成する: No Output")
import pathlib

pathlib.Path('empty.txt').touch()

print("----------------------------------------")
print("c7_2_14/ファイルを削除する: No Output")
import os

os.remove('empty.txt')

print("----------------------------------------")
print("")

print("<ファイルやディレクトリの列挙>")
print("----------------------------------------")
print("c7_2_15/ディレクトリの中のディレクトリを調べる:")
import os

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))

print("----------------------------------------")
print("c7_2_16/ディレクトリの中のファイルを調べる:")
import pathlib
import glob

pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# Windowsの場合、ディレクトリの境目は「\\」
print(glob.glob('test_dir\\test_dir2\\*'))

print("----------------------------------------")
print("")

print("<高度なファイル操作>")
print("----------------------------------------")
print("c7_2_17/ファイルをコピー:")
import shutil
import glob

shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir\\test_dir2\\*'))

print("----------------------------------------")
print("c7_2_1\8/ディレクトリの中身ごと削除:No Output")
import shutil

shutil.rmtree('test_dir')

print("----------------------------------------")
print("7-2終了")

while True:
    print("renamed.txt、test.csv、symlink.txtをこのレッスンで作成しました")
    file_remover = input('作成したこの3つのファイルを削除しますか（y/n）：')
    if file_remover == 'y':
        os.remove('renamed.txt')
        os.remove('test.csv')
        os.remove('symlink.txt')
        break
    elif file_remover == 'n':
        break
    else:
        print("yかnを入力してください")