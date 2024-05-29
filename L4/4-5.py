print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson4 入門編 関数と例外処理 ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("4-5 例外処理（エラーハンドリング）")
print("-------------------------")
print("")

print("| 例外処理をしてみよう")
print("<例外処理>")
print("----------------------------------------")
print("c4_5_1/IndexError:")
# l = [1, 2, 3]
# i = 5
# l[i]
print("*** Error Output ***")
err_msg = """\
    l[i]
    ~^^^
IndexError: list index out of range\
"""
print(err_msg)

print("----------------------------------------")
print("c4_5_2/エラーハンドリング:")
l = [1, 2, 3]
i = 5
try:
    l[i]
except:
    print("Don't worry")
print("last")

print("----------------------------------------")
print("c4_5_3/特定のエラーの処理:")
l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError:
    print("Don't worry")

print("----------------------------------------")
print("c4_5_4/エラーの内容を表示:")
l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))

print("----------------------------------------")
print("c4_5_5/異なるエラーの発生:")
# l = [1, 2, 3]
# i = 5
# del l
# try:
#     l[i]
# except IndexError as ex:
#     print("Don't worry: {}".format(ex))
print("*** Error Output ***")
err_msg = """\
    l[i]
    ^
NameError: name 'l' is not defined\
"""
print(err_msg)

print("----------------------------------------")
print("c4_5_7/Exception:")
l = [1, 2, 3]
i = 5
try:
    () + l
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other:{}".format(ex))

print("----------------------------------------")
print("")

print("<finally>")
print("----------------------------------------")
print("c4_5_8/finally:")
l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
finally:
    print("clean up")

print("----------------------------------------")
print("c4_5_9/finally:")
# l = [1, 2, 3]
# i = 5
# try:
#     l[i]
# finally:
#     print("clean up")

print("*** Error Output ***")
err_msg = """\
    l[i]
    ~^^^
IndexError: list index out of range\
"""
print(err_msg)

print("----------------------------------------")
print("")

print("<else>")
print("----------------------------------------")
print("c4_5_10/else:")
l = [1, 2, 3]
i = 5

try:
    l[0]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
else:
    print("done")
finally:
    print("clean up")

print("----------------------------------------")
print("")

print("| 独自例外を作成してみよう")
print("----------------------------------------")
print("c4_5_11/raise:")
# raise IndexError('test error')
print("*** Error Output ***")
err_msg = """\
    raise IndexError('test error')
IndexError: test error\
"""
print(err_msg)

print("----------------------------------------")
print("c4_5_12/独自例外を発生させる:")
# class UppercaseError(Exception):
#     pass
#
# def check():
#     words = ['APPLE', 'orange', 'banana']
#     for word in words:
#         if word.isupper():
#             raise UppercaseError(word)
#
# check()

print("*** Error Output ***")
err_msg = """\
    raise UppercaseError(word)
UppercaseError: APPLE\
"""
print(err_msg)

print("----------------------------------------")
print("c4_5_13/独自例外を発生させる:")
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

print("----------------------------------------")
print("")

print("Point/既存の例外を発生させる:")
print("----------------------------------------")
print("c4_5_14/既存の例外を発生させる:")
def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise ValueError(word)

try:
    check()
except ValueError as exc:
    print('This is my fault. Go next')

print("----------------------------------------")
print("4-5終了")
prnit("Lesson4終了")