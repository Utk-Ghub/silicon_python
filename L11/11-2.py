# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson11 応用編 Webとネットワーク ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("11-2 Pythonで通信してみよう")
print("-------------------------")
print("")

print("| Pythonで通信してみよう")
print("<urllibでREST APIを使ってみよう>")
print("----------------------------------------")
print("コード/ライブラリのimport: No Output")
print("----------------------------------------")
print("")

print("<GET>")
print("コード/GETでアクセスするURL: No Output")

print("----------------------------------------")
print("c11_2_1/GETでアクセス:")
import urllib.request
import json

url = 'http://httpbin.org/get'

with urllib.request.urlopen(url) as f:
    print(f.read())

print("----------------------------------------")
print("c11_2_2/GETで取得したデータをデコード:")
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))

print("----------------------------------------")
print("c11_2_3/GETで取得したデータを辞書型で読み込む:")
with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r)
    print(type(r))

print("----------------------------------------")
print("c11_2_4/GETでパラメータを付加してアクセスするときのURL:")
payload = {"key1": "value1", "key2": "value2"}
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)

print("----------------------------------------")
print("")

print("<POST>")
print("----------------------------------------")
print("コード/POSTでリクエストするためのデータを作成: No Output")
print("c11_2_5/POSTでアクセス:")
payload = {"key1": "value1", "key2": "value2"}
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST'
)

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

print("----------------------------------------")
print("")

print("<PUTとDELETE>")
print("----------------------------------------")
print("c11_2_6/PUTでアクセス:")
payload = {"key1": "value1", "key2": "value2"}
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT'
)
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

print("----------------------------------------")
print("c11_2_7/DELETEでアクセス:")
payload = {"key1": "value1", "key2": "value2"}
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE'
)
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

print("----------------------------------------")
print("")

print("| requestsで簡単にREST APIを使ってみよう")
print("----------------------------------------")
print("c11_2_8/requestsによるGETでのアクセス:")
import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('http://httpbin.org/get', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

print("----------------------------------------")
print("c11_2_9/requestsによるPOSTでのアクセス:")
import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('http://httpbin.org/post', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

print("----------------------------------------")
print("c11_2_10/requestsによるPUTでのアクセス:")
import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.put('http://httpbin.org/put', data=payload)

print(r.status_code)
print(r.text)
print(r.json())

print("----------------------------------------")
print("c11_2_11/requestsによるDELETEでのアクセス:")
import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.delete('http://httpbin.org/delete', data=payload)

print(r.status_code)
print(r.text)
print(r.json())

print("----------------------------------------")
print("c11_2_12/timeoutを指定:")
# import requests
#
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.get('http://httpbin.org/get', params=payload, timeout=0.001)
#
# print(r.status_code)
# print(r.text)
# print(r.json())

print("*** Error Output ***")
err_msg = """\
（詳細省略）
requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='httpbin.org', port=80): Max retries exceeded with url: /get?key1=value1&key2=value2 (Caused by ConnectTimeoutError(<urllib3.connection.HTTPConnection object at 0x000001C1245A6C50>, 'Connection to httpbin.org timed out. (connect timeout=0.001)'))\
"""
print(err_msg)

print("----------------------------------------")
print("11-2終了")