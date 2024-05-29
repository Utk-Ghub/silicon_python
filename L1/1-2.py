print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson1 入門編 Pythonの基本 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("1-2 文字列のさまざまな操作方法")
print("-------------------------")
print("")

print("| 文字列の基本的な使い方を身につけよう")
print("<文字列を表示する>")
print("----------------------------------------")
print("c1_2_1/文字列の出力:")
s = 'hello'
print(s)

print("----------------------------------------")
print("c1_2_2/文字列の出力:")
print('hello')

print("----------------------------------------")
print("")

print("<文字列の囲み方>")
print("----------------------------------------")
print("c1_2_3/シングルクォートとダブルクォート:")
print('hello')
print("hello")

print("----------------------------------------")
print("c1_2_4/ダブルクォートの中にシングルクォート:")
print("I don't know")

print("----------------------------------------")
print("c1_2_5/シングルクォートの中にシングルクォート:")
# print('I don't know'')
print("*** Error Output ***")
err_msg = """\
    print('I don't know'')
          ^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?\
"""
print(err_msg)

print("----------------------------------------")
print("c1_2_6/シングルクォートの前にバックスラッシュ:")
print('I don\'t know')

print("----------------------------------------")
print("c1_2_7/シングルクォートの中にダブルクォート:")
print('say "I don\'t know"')

print("----------------------------------------")
print("c1_2_8/ダブルクォートの中にダブルクォート:")
# print("say "I don\'t know"")
print("*** Error Output ***")
err_msg = """\
    print("say "I don\'t know"")
          ^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?\
"""
print(err_msg)

print("----------------------------------------")
print("c1_2_9/ダブルクォートの前にバックスラッシュ:")
print("say \"I don't know\"")

print("----------------------------------------")
print("")

print("<文字列の途中に改行を入れる>")
print("----------------------------------------")
print("c1_2_10/改行:")
print('hello. \nHow are you?')

print("----------------------------------------")
print("c1_2_11/意図せぬ改行:")
print('C:\name\name')

print("----------------------------------------")
print("c1_2_12/意図せぬ改行の回避:")
print(r'C:\name\name')

print("----------------------------------------")
print("")

print("<複数行にわたる文字列の出力>")
print("----------------------------------------")
print("c1_2_13/複数行にわたる文字列の出力:")
print("""
line1
line2
line3
""")

print("----------------------------------------")
print("c1_2_14/複数行にわたる文字列の出力:")
print("##########")
print("""
line1
line2
line3
""")
print("##########")

print("----------------------------------------")
print("c1_2_15/複数行にわたる文字列の出力:")
print("##########")
print("""line1
line2
line3""")
print("##########")

print("----------------------------------------")
print("c1_2_16/複数行にわたる文字列の出力:")
print("##########")
print("""\
line1
line2
line3\
""")
print("##########")

print("----------------------------------------")
print("")

print("<文字列を連結する>")
print("----------------------------------------")
print("c1_2_17/文字列を繰り返し出力する:")
print('Hi.' * 3)

print("----------------------------------------")
print("c1_2_18/文字列を連結する:")
print('Hi.' * 3 + 'Mike.')

print("----------------------------------------")
print("c1_2_19/リテラル同士を連結する:")
print('Py' + 'thon')
print('Py''thon')

print("----------------------------------------")
print("c1_2_20/変数とリテラルを連結する:")
prefix = 'Py'
# print(prefix'thon')
print("*** Error Output ***")
err_msg = """\
    print(prefix'thon')
                ^^^^^^
SyntaxError: invalid syntax\
"""
print(err_msg)

print("----------------------------------------")
print("c1_2_21/変数とリテラルを連結する:")
prefix = 'Py'
print(prefix + 'thon')

print("----------------------------------------")
print("Point/複数行にわたる文字列の連結:")
print("c1_2_22/複数行にわたる文字列の連結:")
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

print("----------------------------------------")
print("c1_2_23/複数行にわたる文字列の連結:")
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

print("----------------------------------------")
print("")

print("| 文字列のインデックスとスライスを使おう")
print("<文字列のインデックス>")
print("----------------------------------------")
print("c1_2_24/文字列のインデックス:")
word = 'python'
print(word[0])

print("----------------------------------------")
print("c1_2_25/文字列のインデックス:")
word = 'python'
print(word[1])

print("----------------------------------------")
print("c1_2_26/文字列のインデックス:")
word = 'python'
print(word[-1])

print("----------------------------------------")
print("")

print("<文字列のスライス>")
print("----------------------------------------")
print("c1_2_27/文字列のスライス:")
word = 'python'
print(word[0:2])

print("----------------------------------------")
print("c1_2_28/文字列のスライス:")
word = 'python'
print(word[2:5])

print("----------------------------------------")
print("c1_2_29/文字列のスライス:")
word = 'python'
print(word[0:2])
print(word[:2])

print("----------------------------------------")
print("c1_2_30/文字列のスライス:")
word = 'python'
print(word[2:])

print("----------------------------------------")
print("c1_2_31/存在しないインデックスの指定:")
# word = 'python'
# print(word[100])
print("*** Error Output ***")
err_msg = """\
    print(word[100])
          ~~~~^^^^^
IndexError: string index out of range\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("Point/文字列の一部は書き換えられない:")
print("----------------------------------------")
print("c1_2_32/文字列の一部を書き換える:")
# word = 'python'
# word[0] = 'j'
print("*** Error Output ***")
err_msg = """\
    word[0] = 'j'
    ~~~~^^^
TypeError: 'str' object does not support item assignment\
"""
print(err_msg)

print("----------------------------------------")
print("c1_2_33/文字列の一部を書き換える:")
word = 'python'
word = 'j' + word[1:]
print(word)

print("----------------------------------------")
print("c1_2_34/文字のスライス:")
word = 'python'
print(word[:])

print("----------------------------------------")
print("")

print("Point/len関数:")
print("----------------------------------------")
print("c1_2_35/文字列の長さを調べる:")
word = 'python'
n = len(word)
print(n)

print("----------------------------------------")
print("")

print("| 文字列のメソッドを使おう")
print("----------------------------------------")
print("c1_2_36/startswith():")
s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('My')
print(is_start)

print("----------------------------------------")
print("c1_2_37/startswith():")
s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('X')
print(is_start)

print("----------------------------------------")
print("c1_2_38/find():")
s = 'My name is Mike. Hi Mike.'
print(s.find('Mike'))

print("----------------------------------------")
print("c1_2_39/rfind():")
s = 'My name is Mike. Hi Mike.'
print(s.rfind('Mike'))

print("----------------------------------------")
print("c1_2_40/count():")
s = 'My name is Mike. Hi Mike.'
print(s.count('Mike'))

print("----------------------------------------")
print("c1_2_41/capitalize():")
s = 'My name is Mike. Hi Mike.'
print(s.capitalize())

print("----------------------------------------")
print("c1_2_42/title():")
s = 'My name is Mike. Hi Mike.'
print(s.title())

print("----------------------------------------")
print("c1_2_43/upper():")
s = 'My name is Mike. Hi Mike.'
print(s.upper())

print("----------------------------------------")
print("c1_2_44/lower():")
s = 'My name is Mike. Hi Mike.'
print(s.lower())

print("----------------------------------------")
print("c1_2_45/replace():")
s = 'My name is Mike. Hi Mike.'
print(s.replace('Mike', 'Nancy'))

print("----------------------------------------")
print("")

print("| 文字列に他の値を挿入しよう")
print("----------------------------------------")
print("対話型/文字列の挿入:")
print('a is {}'.format('a'))

print("----------------------------------------")
print("対話型/文字列の代入:")
print('a is {}'.format('test'))

print("----------------------------------------")
print("対話型/複数の文字列の挿入:")
print('a is {} {} {}'.format(1, 2, 3))

print("----------------------------------------")
print("対話型/インデックスによる複数の文字列の挿入:")
print('a is {0} {1} {2}'.format(1, 2, 3))

print("----------------------------------------")
print("対話型/インデックスによる複数の文字列の挿入:")
print('a is {2} {1} {0}'.format(1, 2, 3))

print("----------------------------------------")
print("対話型/インデックスによる複数の文字列の挿入:")
print('My name is {0} {1}. Watashi wa {1} {0}.'.format('Jun', 'Sakai'))

print("----------------------------------------")
print("対話型/変数による複数の文字列の挿入:")
print('My name is {name} {family}. Watashi wa {family} {name}.'.format(name='Jun', family='Sakai'))

print("----------------------------------------")
print("")

print("Point/より使いやすいf-strings:")
print("----------------------------------------")
print("c1_2_46/f-strings:")
a = 'a'
print(f'a is {a}')

print("----------------------------------------")
print("c1_2_47/f-strings:")
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

print("----------------------------------------")
print("")

print("Point/数値を文字列に型変換する:")
print("----------------------------------------")
print("対話型/文字列型への型変換:")
print(str(1))

print("----------------------------------------")
print("対話型/文字列型への型変換:")
print(str(3.14))
print(str(True))

print("----------------------------------------")
print("1-2終了")
print("Lesson 1終了")