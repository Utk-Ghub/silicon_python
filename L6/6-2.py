print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson6 入門編 オブジェクトとクラス ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("6-2 クラスをもっと活用してみよう")
print("-------------------------")
print("")

print("| プロパティの使い方を知ろう")
print("<プロパティ>")
print("----------------------------------------")
print("c6_2_1/オブジェクトの変数を書き換える:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

advanced_car = AdvancedCar('SUV')
advanced_car.enable_auto_run = True
print(advanced_car.enable_auto_run)

print("----------------------------------------")
print("c6_2_2/オブジェクトの変数に_をつける:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

advanced_car = AdvancedCar('SUV')
advanced_car._enable_auto_run = True
print(advanced_car._enable_auto_run)

print("----------------------------------------")
print("c6_2_3/@propertyを使う:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

advanced_car = AdvancedCar('SUV')
print(advanced_car._enable_auto_run)

print("----------------------------------------")
print("c6_2_4/プロパティに値を設定する:")
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#
# class AdvancedCar(Car):
#     def __init__(self, model='SUV', enable_auto_run=False):
#         super().__init__(model)
#         self._enable_auto_run = enable_auto_run
#
#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
#
# advanced_car = AdvancedCar('SUV')
# advanced_car.enable_auto_run = True
# print(advanced_car._enable_auto_run)

print("*** Error Output ***")
err_msg = """\
    advanced_car.enable_auto_run = True
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: property 'enable_auto_run' of 'AdvancedCar' object has no setter\
"""
print(err_msg)

print("----------------------------------------")
print("c6_2_5/セッターの使用:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

advanced_car = AdvancedCar('SUV')
advanced_car.enable_auto_run = True
print(advanced_car.enable_auto_run)

print("----------------------------------------")
print("c6_2_6/セッターの使い方:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

advanced_car = AdvancedCar('SUV', passwd='456')
advanced_car.enable_auto_run = True
print(advanced_car.enable_auto_run)

print("----------------------------------------")
print("")

print("<変数にアンダースコアをつける>")
print("----------------------------------------")
print("c6_2_7/_をつけた変数にアクセスする:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

advanced_car = AdvancedCar('SUV')
print(advanced_car._enable_auto_run)

print("----------------------------------------")
print("c6_2_8/__をつけた変数にアクセスする:")
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#
# class AdvancedCar(Car):
#     def __init__(self, model='SUV', enable_auto_run=False):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run
#
#     @property
#     def enable_auto_run(self):
#         return self.__enable_auto_run
#
# advanced_car = AdvancedCar('SUV')
# print(advanced_car.__enable_auto_run)

print("*** Error Output ***")
err_msg = """\
    print(advanced_car.__enable_auto_run)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'AdvancedCar' object has no attribute '__enable_auto_run'. Did you mean: 'enable_auto_run'?\
# """
print(err_msg)

print("----------------------------------------")
print("c6_2_9/__をつけた変数にクラス内からアクセスする:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')

advanced_car = AdvancedCar('SUV')
advanced_car.run()

print("----------------------------------------")
print("")

print("Point/アンダースコアつきの変数を使うときの注意点:")
print("----------------------------------------")
print("c6_2_10/オブジェクトにあとから変数を追加する:")
class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

print("----------------------------------------")
print("c6_2_11/__をつけた変数に値を入れる:")
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    # 下記関数は、私の理解の為に私自身が追加した
    def run(self):
        print(self.__enable_auto_run)

advanced_car = AdvancedCar('SUV')
advanced_car.__enable_auto_run = 'XXXXXXXXXX'
print(advanced_car.__enable_auto_run)

print("")
print("下記1行は私の理解の為に私自身が追加した")
advanced_car.run()

print("----------------------------------------")
print("")

print("| 例外処理とダックタイピング")
print("----------------------------------------")
print("c6_2_12/babyを渡したdriveメソッド:")
class  Car(object):
    def ride(self, person):
        person.drive()

class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
print("----------------------------------------")
# baby = Baby()
# car = Car()
# car.ride(baby)

print("*** Error Output ***")
err_msg = """\
Traceback (most recent call last):
  File "<パス省略>6-2.py", line 275, in <module>
    car.ride(baby)
  File "<パス省略>6-2.py", line 244, in ride
    person.drive()
  File "<パス省略>6-2.py", line 255, in drive
    raise Exception('No drive')
Exception: No drive\
"""
print(err_msg)

print("----------------------------------------")
print("c6_2_13/adultを渡したdriveメソッド:")
adult = Adult()
car = Car()
car.ride(adult)

print("----------------------------------------")
print("")

print("| 抽象クラスの使い方を学ぼう")
print("----------------------------------------")
print("c6_2_14/adultでdriveメソッドを実行:")
class Person(object):
    def __init__(self, age=1):
        self.age = age

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')

adult = Adult()
adult.drive()

print("----------------------------------------")
print("c6_2_15/babyでdriveメソッドを実行:")
# baby = Baby()
# baby.drive()
print("*** Error Output ***")
err_msg = """\
  File "<パス省略>6-2-14_15.py", line 35, in <module>
    baby.drive()
  File "<パス省略>6-2-14_15.py", line 17, in drive
    raise Exception('No drive')
Exception: No drive\
"""
print(err_msg)

print("----------------------------------------")
print("c6_2_16/メソッドがないとエラーになる:")
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age
#
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# adult = Adult()
# adult.drive()

print("*** Error Output ***")
err_msg = """\
    adult.drive()
    ^^^^^^^^^^^
AttributeError: 'Adult' object has no attribute 'drive'\
"""
print(err_msg)

print("----------------------------------------")
print("c6_2_17/継承先のクラスで抽象メソッドをオーバーライドしないとエラー:")
# import abc
#
# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age=1):
#         self.age = age
#
#     @abc.abstractmethod
#     def drive(self):
#         pass
#
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# adult = Adult()

print("*** Error Output ***")
err_msg = """\
    adult = Adult()
            ^^^^^^^
TypeError: Can't instantiate abstract class Adult with abstract method drive\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("| 多重継承で複数の機能を持ったクラスを作ろう")
print("----------------------------------------")
print("c6_2_18/多重継承:")
class Person(object):
    def talk(self):
        print('talk')

class Car(object):
    def run(self):
        print('run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

print("----------------------------------------")
print("c6_2_19/多重継承の順番:")
class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.run()

print("----------------------------------------")
print("c6_2_20/多重継承の順番:")
class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Car, Person):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.run()

print("----------------------------------------")
print("")

print("| クラス変数で値を共有しよう")
print("----------------------------------------")
print("c6_2_21/オブジェクト間で共通するインスタンス変数:")
class Person(object):
    def __init__(self, name):
        self.kind = 'human'
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

print("----------------------------------------")
print("c6_2_22/クラス変数:")
class Person(object):
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

print("----------------------------------------")
print("c6_2_23/リストのクラス変数:")
class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')

print(c.words)

print("----------------------------------------")
print("c6_2_24/クラス変数の初期化:")
class T(object):
    words = []

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add 1')
c.add_word('add 2')

print(c.words)

d = T()
d.add_word('add 3')
d.add_word('add 4')

print(d.words)

print("----------------------------------------")
print("")

print("| クラスメソッドとスタティックメソッドを使おう")
print("<クラスメソッド>")
print("----------------------------------------")
print("c6_2_25/クラスの定義と利用:")
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

a = Person()
print(a)
b = Person
print(b)

print("----------------------------------------")
print("c6_2_26/インスタンス変数の呼び出し:")
a = Person()
print(a.x)

print("----------------------------------------")
print("c6_2_27/インスタンス変数の呼び出し:")
# b = Person
# print(b.x)

print("*** Error Output ***")
err_msg = """\
    print(b.x)
          ^^^
AttributeError: type object 'Person' has no attribute 'x'\
"""
print(err_msg)

print("----------------------------------------")
print("c6_2_28/クラス変数の呼び出し:")
a = Person()
print(a.kind)
b = Person
print(b.kind)

print("----------------------------------------")
print("コード/クラスの定義:")
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind

print("----------------------------------------")
print("c6_2_29/オブジェクトからメソッドを実行:")
a = Person()
print(a.what_is_your_kind())

print("----------------------------------------")
print("c6_2_30/クラスからメソッドを実行:")
# b = Person
# print(b.what_is_your_kind())

print("*** Error Output ***")
err_msg = """\
    print(b.what_is_your_kind())
          ^^^^^^^^^^^^^^^^^^^^^
TypeError: Person.what_is_your_kind() missing 1 required positional argument: 'self'\
"""
print(err_msg)

print("----------------------------------------")
print("c6_2_31/クラスメソッド:")
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
a = Person()
print(a.what_is_your_kind())

b = Person
print(b.what_is_your_kind())

print("----------------------------------------")
print("")

print("Point/クラスメソッドの実行方法:")
print("----------------------------------------")
print("c6_2_32/クラスメソッド:")
print(Person.kind)
print(Person.what_is_your_kind())

print("----------------------------------------")
print("")

print("<スタティックメソッド>")
print("----------------------------------------")
print("c6_2_33/スタティックメソッド:")
class Person(object):

    @staticmethod
    def about():
        print('about human')

Person.about()

print("----------------------------------------")
print("c6_2_34/引数を取るスタティックメソッド:")
class Person(object):

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

Person.about(1999)

print("----------------------------------------")
print("")

print("Point/スタティックメソッドの使い方:")
print("----------------------------------------")
print("c6_2_35/関数として定義:")
def about(year):
    print('about human {}'.format(year))

class human(object):
    pass

about(1999)

print("----------------------------------------")
print("")

print("| 特殊メソッドを使おう")
print("----------------------------------------")
print("c6_2_36/__str__:")
class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'word!!!!!!'

w = Word('test')
print(w)

print("----------------------------------------")
print("c6_2_37/__len__:")
class Word(object):
    def __init__(self, text):
        self.text = text

    def __len__(self):
        return len(self.text)

w = Word('test')
print(len(w))

print("----------------------------------------")
print("c6_2_38/__add__:")
class Word(object):
    def __init__(self, text):
        self.text = text

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

w = Word('test')
w2 = Word('##########')
print(w + w2)

print("----------------------------------------")
print("c6_2_39/オブジェクトの比較:")
class Word(object):
    def __init__(self, text):
        self.text = text

w = Word('test')
w2 = Word('test')
print(w == w2)
print(id(w))
print(id(w2))

print("----------------------------------------")
print("c6_2_40/__eq__:")
class Word(object):
    def __init__(self, text):
        self.text = text

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('test')
w2 = Word('test')
print(w == w2)

print("----------------------------------------")
print("6-2終了")
print("Lesson6終了")