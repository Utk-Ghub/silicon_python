# -*- coding: utf-8 -*-
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("■ Lesson10 応用編 コンフィグとロギング ■")
print("■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
print("")
print("10-1 設定ファイルのさまざまな形式")
print("-------------------------")
print("")

print("| configparserを使って設定ファイルを読み書きしよう")
print("----------------------------------------")
print("c10_1_1/configparserで書き込む: No Output")
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}
with open('config.ini', 'w') as config_file:
    config.write(config_file)

print("----------------------------------------")
print("c10_1_2/configparserで読み込む:")
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])

print(config['DEFAULT']['debug'])

print("----------------------------------------")
print("")

print("| yaml形式で書かれた設定ファイルを読み書きしよう")
print("----------------------------------------")
print("c10_1_3/yamlファイルに書き込む: No Output")
import yaml
with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file)

print("----------------------------------------")
print("c10_1_4/yamlファイルを読み込む:")
import yaml

with open('config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(data)
    print(type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])

print("----------------------------------------")
print("")

print("Point/yamlのスタイル:")
print("----------------------------------------")
print("c10_1_5/ブロックスタイルで書き込む: No Output")
import yaml
with open('config2.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)

print("----------------------------------------")
print("10-1終了")

import os

while True:
    file_remover = input('作成したファイル/ディレクトリを削除しますか（y/n）：')
    if file_remover == 'y':
        os.remove('config.ini')
        os.remove('config.yml')
        os.remove('config2.yml')
        break
    elif file_remover == 'n':
        break
    else:
        print("yかnを入力してください")