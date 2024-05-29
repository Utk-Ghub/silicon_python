print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson4 入門編 関数と例外処理 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("4-1 何度も実行する処理の関数を作ろう")
print("-------------------------")
print("")

print("| 関数を定義する方法を知ろう")
print("<関数>")
print("----------------------------------------")
print("c4_1_1/関数定義:")
def say_something():
    print('hi')

say_something()

print("----------------------------------------")
print("")

print("Point/関数は呼び出しより先に定義する:")
print("----------------------------------------")
print("c4_1_2/関数定義の順番:")
# say_something()
# def say_something():
#     print('hi')
print("*** Error Output ***")
err_msg = """\
    say_something()
    ^^^^^^^^^^^^^
NameError: name 'say_something' is not defined\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("----------------------------------------")
print("c4_1_3/関数の呼び出し方:No Output")
def say_something():
    print('hi')

say_something

print("----------------------------------------")
print("c4_1_4/関数の型:")
def say_something():
    print('hi')

print(type(say_something))

print("----------------------------------------")
print("c4_1_5/関数を変数に入れて呼び出す:")
def say_something():
    print('hi')

f = say_something
f()

print("----------------------------------------")
print("")

print("<返り値>")
print("----------------------------------------")
print("c4_1_6/返り値:")
def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

print("----------------------------------------")
print("")

print("<引数>")
print("----------------------------------------")
print("c4_1_7/引数:")
def what_is_this(color):
    print(color)

what_is_this('red')

print("----------------------------------------")
print("c4_1_8/引数:")
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)

print("----------------------------------------")
print("")

print("Point/引数と返り値の型宣言:")
print("----------------------------------------")
print("c4_1_9/引数の型の宣言: No Output")
def add_num(a: int, b: int):
    return a + b

print("----------------------------------------")
print("c4_1_10/返り値の型の宣言: No Output")
def add_num(a: int, b: int) -> int:
    return a + b

print("----------------------------------------")
print("c4_1_11/型が宣言された関数の呼び出し:")
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)

print("----------------------------------------")
print("c4_1_11/型が宣言された関数の呼び出し:")
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a', 'b')
print(r)

print("----------------------------------------")
print("")

print("| 位置引数、キーワード引数、デフォルト引数の違いは？")
print("<位置引数>")
print("----------------------------------------")
print("c4_1_13/位置引数:")
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('beef', 'beer', 'ice')

print("----------------------------------------")
print("c4_1_14/位置引数の順番:")
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('beef', 'ice', 'beer')

print("----------------------------------------")
print("")

print("<キーワード引数>")
print("----------------------------------------")
print("c4_1_15/キーワード引数:")
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu(entree='beef', dessert='ice', drink='beer')

print("----------------------------------------")
print("c4_1_15/キーワード引数:")
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('beef', dessert='ice', drink='beer')

print("----------------------------------------")
print("c4_1_16/位置引数とキーワード引数を混ぜて使う:")
# def menu(entree, drink, dessert):
#     print('entree = ', entree)
#     print('drink = ', drink)
#     print('dessert = ', dessert)
#
# menu(dessert='ice', 'beef', drink='beer')
#
print("*** Error Output ***")
err_msg = """\
    menu(dessert='ice', 'beef', drink='beer')
                                            ^
SyntaxError: positional argument follows keyword argument\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("<デフォルト引数>")
print("----------------------------------------")
print("c4_1_18/デフォルト引数:")
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu()

print("----------------------------------------")
print("c4_1_19/デフォルト引数を上書きする:")
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu(entree='chicken', drink='beer')

print("----------------------------------------")
print("c4_1_20/位置引数とキーワード引数とデフォルト引数を混ぜて使う:")
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('chicken', drink='beer')

print("----------------------------------------")
print("")

print("| デフォルト引数でリストや辞書型を使う際の注意")
print("----------------------------------------")
print("c4_1_21/デフォルト引数に空のリストを使う:")
def sample_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = sample_func(100, y)
print(r)

y = [1, 2, 3]
r = sample_func(200, y)
print(r)

print("----------------------------------------")
print("c4_1_22/デフォルト引数に空のリストを使う:")
def sample_func(x, l=[]):
    l.append(x)
    return l

r = sample_func(100)
print(r)

print("----------------------------------------")
print("c4_1_23/デフォルト引数に空のリストを使う:")
def sample_func(x, l=[]):
    l.append(x)
    return l

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)

print("----------------------------------------")
print("")

print("Point/デフォルト引数に空のリストを使いたい場合:")
print("----------------------------------------")
print("c4_1_24/デフォルト引数に空のリストではなくNoneを使う:")
def sample_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)

print("----------------------------------------")
print("")

print("| 位置引数をタプル化してまとめよう")
print("----------------------------------------")
print("c4_1_25/複数の引数:")
def say_something(word, word2, word3):
    print(word)
    print(word2)
    print(word3)

say_something('Hi!', 'Mike', 'Nancy')

print("----------------------------------------")
print("c4_1_26/位置引数のタプル化:")
def say_something(*args):
    print(args)

say_something('Hi!', 'Mike', 'Nancy')

print("----------------------------------------")
print("c4_1_27/位置引数のタプル化:")
def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')

print("----------------------------------------")
print("c4_1_28/位置引数のタプル化:")
def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')

print("----------------------------------------")
print("")

print("Point/引数を渡す際にアンパッキングする:")
print("----------------------------------------")
print("c4_1_29/タプルの引数をタプル化する:")
def say_something(word, *args):
    print('word =',word)
    for arg in args:
        print(arg)

t = ('Mike', 'Nancy')
say_something('Hi!', *t)

print("----------------------------------------")
print("")

print("| キーワード引数を辞書化してまとめよう")
print("----------------------------------------")
print("c4_1_30/キーワード引数:")
def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffee')

print("----------------------------------------")
print("c4_1_31/キーワード引数の辞書化:")
def menu(**kwargs):
    print(kwargs)

menu(entree='beef', drink='coffee')

print("----------------------------------------")
print("c4_1_32/キーワード引数の辞書化:")
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

print("----------------------------------------")
print("")

print("Point/キーワード引数を辞書にして渡す:")
print("----------------------------------------")
print("c4_1_33/キーワード引数の辞書化:")
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)

print("----------------------------------------")
print("")

print("----------------------------------------")
print("c4_1_34/位置引数とタプル化と辞書化:")
def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu(
    'banana',
     'apple', 'orange',
     entree='beef', drink='coffee'
)

print("----------------------------------------")
print("c4_1_35/位置引数とタプル化と辞書化:")
# def menu(food, **kwargs, *args):
#     print(food)
#     print(args)
#     print(kwargs)
#
# menu(
#     'banana',
#      'apple', 'orange',
#      entree='beef', drink='coffee'
# )
print("*** Error Output ***")
err_msg = """\
    def menu(food, **kwargs, *args):
                             ^
SyntaxError: arguments cannot follow var-keyword argument\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("| docstringって何？")
print("----------------------------------------")
print("/関数の説明の記述: No Output")
def example_func(param1, param2):
    """Docstring example for describing overall explanation of function.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    print(param1)
    print(param2)
    return True

print("----------------------------------------")
print("c4_1_36/関数の説明の出力:")
def example_func(param1, param2):
    """Docstring example for describing overall explanation of function.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    print(param1)
    print(param2)
    return True

print(example_func.__doc__)

print("----------------------------------------")
print("c4_1_37/関数の説明の出力:")
def example_func(param1, param2):
    """Docstring example for describing overall explanation of function.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    print(param1)
    print(param2)
    return True

help(example_func)

print("----------------------------------------")
print("4-1終了")