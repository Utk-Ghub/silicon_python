# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson7 入門編 ファイル操作とシステム ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("7-4 さらに高度なファイルに関する操作")
print("-------------------------")
print("")

print("| 一時ファイルを活用しよう")
print("<一時ファイルの作成>")
print("----------------------------------------")
print("c7_4_1/処理終了後に消去される一時ファイルを作成:")
import tempfile

with tempfile.TemporaryFile(mode="w+") as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

print("----------------------------------------")
print("c7_4_2/処理終了後も残る一時ファイルを作成:")
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

print("----------------------------------------")
print("")

print("<一時ディレクトリの作成>")
print("----------------------------------------")
print("c7_4_3/処理終了後に消去される一時ディレクトリを作成:")
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

print("----------------------------------------")
print("c7_4_4/処理終了後も残る一時ディレクトリを作成:")
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)

print("----------------------------------------")
print("")

print("| Pythonでターミナルのコマンドを実行しよう")
print("<リストを使ったコマンドの実行>")
print("----------------------------------------")
print("c7_4_5/コマンドの実行:")
# PyCharm on Windowsで実行する場合、
# まずshell=Trueが必要
# かつ、文字化けするので、PyCharmの設定から、
# エディター > ファイルエンコーディング > プロジェクトのエンコーディングにて
# ShiftJISを選ぶ
import subprocess

# subprocess.run(['dir'], shell=True)
subprocess.run(['dir'], shell=True)

print("----------------------------------------")
print("c7_4_6/オプションを指定したコマンドの実行:")
import subprocess

subprocess.run(['dir', '/ah'], shell=True)

print("----------------------------------------")
print("")

print("Point/osによるコマンドの実行:")
print("----------------------------------------")
print("c7_4_7/osライブラリを使ったコマンドの実行:")
import os

os.system('dir')

print("----------------------------------------")
print("")

print("<shel=Trueを使ったコマンドの実行>")
print("----------------------------------------")
print("c7_4_8/shell=Trueを用いたコマンドの実行:")
import subprocess

subprocess.run('dir', shell=True)

print("----------------------------------------")
print("c7_4_9/パイプラインの実行:")
# Windowsにはgrepコマンドがないため、
# grepの代わりにfindstrコマンドを使用した
import subprocess

subprocess.run('dir | findstr test', shell=True)

print("----------------------------------------")
print("c7_4_10/コマンド実行時のエラー:")
import subprocess

subprocess.run('lsa', shell=True)
print('###')

print("----------------------------------------")
print("c7_4_11/コマンド実行時のエラー:")
import subprocess

r = subprocess.run('lsa', shell=True)
print(r.returncode)

print("----------------------------------------")
print("c7_4_12/コマンド実行時のエラー:")
# import subprocess
#
# subprocess.run('lsa', shell=True, check=True)

print("*** Error Output ***")
err_msg = """\
'lsa' は、内部コマンドまたは外部コマンド、
操作可能なプログラムまたはバッチ ファイルとして認識されていません。
Traceback (most recent call last):
  File "<パス省略>", line 110, in <module>
    subprocess.run('lsa', shell=True, check=True)
  File "<パス省略>", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'lsa' returned non-zero exit status 1.\
"""
print(err_msg)
print("----------------------------------------")
print("c7_4_13/コマンド実行時のエラー:")
# import subprocess
#
# subprocess.run(['lsa'])

print("*** Error Output ***")
err_msg = """\
Traceback (most recent call last):
  File "<パス省略>", line 128, in <module>
    subprocess.run(['lsa'])
  File "<パス省略>", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<パス省略>", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "<パス省略>", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] 指定されたファイルが見つかりません。
\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("Point/Popenを使ったパイプラインの実行:")
print("----------------------------------------")
print("c7_4_14/Popenを使ったパイプラインの実行:")
import subprocess

p1 = subprocess.Popen(['dir', '/ah'], shell=True, stdout=subprocess.PIPE)
p2 = subprocess.Popen(['findstr', 'test'], shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)

print("----------------------------------------")
print("")

print("| 時間にまつわるライブラリとバックアップファイル")
print("<datetimeの使い方>")
print("----------------------------------------")
print("c7_4_15/時間の表示:")
import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())

print("----------------------------------------")
print("c7_4_16/時間の表示:")
import datetime

now = datetime.datetime.now()
print(now.strftime('%d/%m/%y-%H%M%S%f'))

print("----------------------------------------")
print("c7_4_17/年月日の表示:")
import datetime

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

print("----------------------------------------")
print("c7_4_18/任意の時刻の表示:")
import datetime

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H%M%S%f'))

print("----------------------------------------")
print("")

print("<日付・時刻の計算>")
print("----------------------------------------")
print("c7_4_19/時間の計算:")
import datetime

now = datetime.datetime.now()
print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)

print("----------------------------------------")
print("c7_4_20/時間の計算:")
import datetime

now = datetime.datetime.now()
print(now)
d = datetime.timedelta(weeks=1)
print(now -d)

print("----------------------------------------")
print("c7_4_21/時間の計算:")
import datetime

now = datetime.datetime.now()
print(now)
d = datetime.timedelta(days=365)
print(now - d)

print("----------------------------------------")
print("")

print("<timeの使い方>")
print("----------------------------------------")
print("c7_4_22/sleep:")
import time

print('#####')
time.sleep(2)
print('#####')

print("----------------------------------------")
print("c7_4_23/エポックタイム:")
import time

print(time.time())

print("----------------------------------------")
print("")

print("<バックアップファイルの作成>")
print("----------------------------------------")
print("c7_4_24/時間をファイル名に含んだバックアップファイルの作成:")
import os
import shutil
import datetime

now = datetime.datetime.now()

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
    ))

with open(file_name, 'w') as f:
    f.write('test')

print("----------------------------------------")
print("7-4終了")
print("Lesson7終了")

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