print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson6 入門編 オブジェクトとクラス ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("6-1 クラスとメソッド")
print("-------------------------")
print("")

print("| クラスを作成しよう")
print("----------------------------------------")
print("c6_1_1/文字列のクラスとメソッドの確認:")
s = 'fadsalkfjsa'
print(s.capitalize())

print("----------------------------------------")
print("c6_1_2/メソッドの実行:")
class Person(object):
    def say_something(self):
        print('hello')

person = Person()
person.say_something()

print("----------------------------------------")
print("")

print("| クラスが初期化されるときの処理を作成しよう")
print("----------------------------------------")
print("c6_1_3/初期化処理:")
class Person(object):
    def __init__(self):
        print('First')

person = Person()

print("----------------------------------------")
print("c6_1_4/初期化処理:")
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

person = Person('Mike')

print("----------------------------------------")
print("c6_1_5/初期化時に引数を渡す:")
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#
# person = Person()
print("*** Error Output ***")
err_msg = """\
    person = Person()
             ^^^^^^^^
TypeError: Person.__init__() missing 1 required positional argument: 'name'\
"""
print(err_msg)

print("----------------------------------------")
print("c6_1_6/初期化処理にデフォルト引数を設定する:")
class Person(object):
    def __init__(self, name='Default'):
        self.name = name
        print(self.name)

person = Person()

print("----------------------------------------")
print("c6_1_7/オブジェクトの変数を呼び出す:")
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))

person = Person('Mike')
person.say_something()

print("----------------------------------------")
print("c6_1_8/自分自身のメソッドを呼び出す:")
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

person = Person('Mike')
person.say_something()

print("----------------------------------------")
print("")

print("| オブジェクトの最後に実行される処理を作成しよう")
print("----------------------------------------")
print("c6_1_9/デストラクタ: No Output")
print("c6_1_9.pyファイル単独で実行しないと全てのコードを実行した後にデストラクタが実行されるため、別途6-1-9.pyファイルを準備した")

print("----------------------------------------")
print("")

print("Point/明示的にデストラクタを呼び出す:")
print("----------------------------------------")
print("c6_1_10/明示的にデストラクタを呼び出す:")
class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('good bye')

person = Person('Mike')
del person
print('##########')

print("----------------------------------------")
print("")

print("| クラスを継承しよう")
print("----------------------------------------")
print("c6_1_11/クラスの継承: No Output")
class Car(object):
    pass

class MyCar(Car):
    pass

print("----------------------------------------")
print("c6_1_12/継承したメソッドの実行:")
class Car(object):
    def run(self):
        print('run')

class MyCar(Car):
    pass

car = Car()
car.run()
my_car = MyCar()
my_car.run()

print("----------------------------------------")
print("c6_1_13/クラスの継承:")
class Car(object):
    def run(self):
        print('run')

class AdvancedCar(Car):
    def auto_run(self):
        print('auto run')

advanced_car = AdvancedCar()
advanced_car.run()
advanced_car.auto_run()

print("----------------------------------------")
print("")

print("| 継承元のメソッドを上書きして実行しよう")
print("<メソッドのオーバーライド>")
print("----------------------------------------")
print("c6_1_14/メソッドのオーバーライド:")
class Car(object):
    def run(self):
        print('run')

class MyCar(Car):
    def run(self):
        print('fast')

class AdvancedCar(Car):
    def run(self):
        print('super fast')

car = Car()
car.run()
print('##########')
my_car = MyCar()
my_car.run()
print('##########')
advanced_car = AdvancedCar()
advanced_car.run()
print("----------------------------------------")
print("c6_1_15/親クラスで__init__を定義する:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class MyCar(Car):
    pass

class AdvancedCar(Car):
    pass

my_car = MyCar('sedan')
print(my_car.model)
advanced_car = AdvancedCar('SUV')
print(advanced_car.model)
print("----------------------------------------")
print("c6_1_16/__init__のオーバーライド:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class MyCar(Car):
    pass

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        self.model = model
        self.enable_auto_run = enable_auto_run

my_car = MyCar('sedan')
print(my_car.model)
advanced_car = AdvancedCar('SUV')
print(advanced_car.model)
print("----------------------------------------")
print("c6_1_17/superを使った継承元クラスのメソッドの実行:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class MyCar(Car):
    pass

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

my_car = MyCar('sedan')
print(my_car.model)
advanced_car = AdvancedCar('SUV')
print(advanced_car.model)

print("----------------------------------------")
print("6-1終了")