print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson4 入門編 関数と例外処理 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("4-4 変数の有効範囲")
print("-------------------------")
print("")

print("| 変数の有効範囲について知ろう")
print("----------------------------------------")
print("c4_4_1/グローバル変数:")
animal = 'cat'
print(animal)

print("----------------------------------------")
print("c4_4_2/関数内からグローバル変数を呼び出す:")
animal = 'cat'

def f():
    print(animal)

f()

print("----------------------------------------")
print("c4_4_3/関数内でグローバル変数に値を入れる:")
# animal = 'cat'
#
# def f():
#     print(animal)
#     animal = 'dog'
#     print('after:', animal)
#
# f()

print("*** Error Output ***")
err_msg = """\
    print(animal)
          ^^^^^^
UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value\
"""
print(err_msg)

print("----------------------------------------")
print("c4_4_4/関数内でグローバル変数に値を入れる:")
animal = 'cat'

def f():
    animal = 'dog'
    print('after:', animal)

f()
print('global:', animal)

print("----------------------------------------")
print("")

print("Point/関数内からグローバル変数を書き換える:")
print("----------------------------------------")
print("c4_4_5/関数内でグローバル変数に値を入れる:")
animal = 'cat'

def f():
    global animal
    animal = 'dog'
    print('local:', animal)

f()
print('global:', animal)

print("----------------------------------------")
print("")

print("| ローカル変数やグローバル変数を出力する")
print("----------------------------------------")
print("c4_4_6/ローカル変数を出力する:")
def f():
    animal = 'dog'
    print('local:', locals())

f()

print("----------------------------------------")
print("c4_4_7/ローカル変数を出力する:")
def f():
    print('local:', locals())

f()

print("----------------------------------------")
print("c4_4_8/グローバル変数を出力する:")
animal = 'cat'
def f():
    print('global:', globals())

f()

print("----------------------------------------")
print("c4_4_9/グローバル変数を出力する: No Output")
print("4-4-9.pyファイル単体で実行しないと__doc__にdocstringが入らないため、別途4-4-9.pyファイルを準備した")

print("----------------------------------------")
print("c4_4_10/__name__や__doc__を出力する:")
animal = 'cat'

def f():
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)

f()
print('global:', __name__)

print("----------------------------------------")
print("4-4終了")