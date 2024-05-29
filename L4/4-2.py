print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson4 入門編 関数と例外処理 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("4-2 関数の応用をマスターしよう")
print("-------------------------")
print("")

print("| 関数内関数の書き方を知ろう")
print("----------------------------------------")
print("c4_2_1/関数内関数:")
def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)

outer(1, 2)

print("----------------------------------------")
print("")

print("<関数内関数とクロージャー>")
print("----------------------------------------")
print("c4_2_2/クロージャー:")
def outer(a, b):
    def inner():
        return a + b

    return inner

print(outer(1, 2))

print("----------------------------------------")
print("c4_2_3/クロージャー:")
def outer(a, b):
    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)

print("----------------------------------------")
print("/円の面積を求める-クロージャーの定義:No Output")
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

print("----------------------------------------")
print("/円の面積を求める-クロージャーを格納する:No Output")
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159)

print("----------------------------------------")
print("c4_2_4/円の面積を求める-クロージャーを格納する:")
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.14159)

print(ca1(10))
print(ca2(10))

print("----------------------------------------")
print("")

print("| デコレーターで関数の前後に処理を加える")
print("----------------------------------------")
print("c4_2_5/関数の実行前と実行後に処理を行う:")
def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')
print(r)

print("----------------------------------------")
print("c4_2_6/デコレーターの実行:")
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b


f = print_info(add_num)
r = f(10, 20)
print(r)

print("----------------------------------------")
print("c4_2_7/デコレーターの簡単な指定:")
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

print("----------------------------------------")
print("c4_2_8/デコレーター:")
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

print("----------------------------------------")
print("c4_2_9/複数のデコレーター:")
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
print("----------------------------------------")
print("c4_2_10/複数のデコレーターの順番:")
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_more
@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
print("----------------------------------------")
print("")

print("Point/@を使わないデコレーターの書き方:")
print("----------------------------------------")
print("c4_2_11/@を使わないデコレーターの書き方:")
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(print_more(add_num))
r = f(10, 20)
print(r)

print("----------------------------------------")
print("")

print("| lambdaを使って関数を引数にする")
print("----------------------------------------")
print("c4_2_12/リストの要素に関数を適用する:")
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

print("----------------------------------------")
print("c4_2_13/lambda:")
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

sample_func = lambda word: word.capitalize()

change_words(l, sample_func)

print("----------------------------------------")
print("c4_2_14/lambda:")
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

change_words(l, lambda word: word.capitalize())

print("----------------------------------------")
print("c4_2_15/複数の簡単な関数を定義する:")
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

def sample_func2(word):
    return word.lower()

change_words(l, sample_func)
change_words(l, sample_func2)

print("----------------------------------------")
print("c4_2_16/lambdaで簡潔に書く:")
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

print("----------------------------------------")
print("")

print("| ジェネレーターで反復可能な要素を生成する")
print("----------------------------------------")
print("c4_2_17/イテレーター:")
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("----------------------------------------")
print("c4_2_18/ジェネレーター:")
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for g in greeting():
    print(g)

print("----------------------------------------")
print("c4_2_19/ジェネレーター:")
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print('@@@@@')
print(next(g))
print('@@@@@')
print(next(g))
print('@@@@@')
print("----------------------------------------")
print("c4_2_20/ジェネレーター:")
# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'
#
# g = greeting()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

print("*** Error Output ***")
err_msg = """\
    print(next(g))
          ^^^^^^^
StopIteration\
"""
print(err_msg)

print("----------------------------------------")
print("c4_2_21/ジェネレーター:")
def counter(num=10):
    for _ in range(num):
        yield 'run'
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print("----------------------------------------")
print("")

print("Point/ジェネレーターによって重たい処理を小分けにする:")
print("----------------------------------------")
print("c4_2_/ジェネレーター:No Output")
def greeting():
    yield 'Good morning'
    for i in range(1000000):
        print(i)
    yield 'Good afternoon'
    for i in range(1000000):
        print(i)
    yield 'Good night'

print("----------------------------------------")
print("4-2終了")