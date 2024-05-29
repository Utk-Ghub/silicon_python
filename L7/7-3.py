print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson7 入門編 ファイル操作とシステム ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("7-3 圧縮ファイルを扱おう")
print("-------------------------")
print("")

# サンプルファイル準備
import os

os.mkdir('test_dir')
os.mkdir('test_dir/sub_dir')
os.mkdir('tmp')
with open('test_dir/test.txt', 'w') as f:
    f.write('test file')
with open('test_dir/sub_dir/sub_test.txt', 'w') as f:
    f.write('sub')

print("| tarファイルの圧縮と展開をしよう")
print("<圧縮してtarファイルを作成する>")
print("----------------------------------------")
print("c7_3_1/tarファイルを作成: No Output")
import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

print("----------------------------------------")
print("c7_3_2/tarファイルを展開: No Output")
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall('test_tar')

print("----------------------------------------")
print("")

print("Point/tarファイルを展開せずに中身を確認する:")
print("----------------------------------------")
print("c7_3_3/tarファイルの中身を確認:")
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())

print("----------------------------------------")
print("")

print("| zipファイルの圧縮と展開をしよう")
print("<圧縮してzipファイルを作成する>")
print("----------------------------------------")
print("c7_3_4/zipファイルを作成: No Output")
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir')
    z.write('test_dir/test.txt')

print("----------------------------------------")
print("c7_3_5/zipファイルを作成: No Output")
import zipfile
import glob

# c7_3_4と同じtest.zipを作成することとなるため
# c7_3_5では作成するzipファイル名をtest2.zipとした
with zipfile.ZipFile('test2.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)

print("----------------------------------------")
print("")

print("<zipファイルを展開する>")
print("----------------------------------------")
print("c7_3_6/zipファイルを展開: No Output")
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')

print("----------------------------------------")
print("")

print("Point/zipファイルを展開せずに中身を確認する:")
print("----------------------------------------")
print("c7_3_7/zipファイルの中身を確認:")
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())

print("----------------------------------------")
print("7-3終了")

import os
import shutil

while True:
    file_remover = input('作成したファイル/ディレクトリを削除しますか（y/n）：')
    if file_remover == 'y':
        os.remove('test.tar.gz')
        os.remove('test.zip')
        os.remove('test2.zip')
        shutil.rmtree('test_dir')
        shutil.rmtree('test_tar')
        shutil.rmtree('tmp')
        shutil.rmtree('zzz2')
        break
    elif file_remover == 'n':
        break
    else:
        print("yかnを入力してください")