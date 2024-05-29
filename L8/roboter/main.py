# -*- coding: utf-8 -*-
from copy import deepcopy
import csv
import os
import string

##############################
# 処理開始
##############################

# 変数宣言と設定
robot = 'Roboko'
ranking_csv = 'ranking.csv'
recommend = ''
yn_answer = ''
fieldnames = ['NAME', 'COUNT']
restauraunt_dic = {}
recommend_dic = {}
tmp_name = ''
max_name = ''
tmp_count = 0
max_count = 0


##############################
# ユーザーに名前を聞く
##############################
with open('msg_dir/greeting_msg.txt') as f:
    g = string.Template(f.read())

display_msg = g.substitute(robot_name=robot)
user = input(display_msg)

##############################
# CSVファイルにデータありなしを確認する
#
# CSVファイルにデータがあれば
# 最多票のレストランをお勧めする
#
# CSVファイルにデータがなければ
# 好きなレストランを質問する、まで飛ぶ
##############################

# CSVファイルが存在するか確認
if os.path.isfile(ranking_csv):

    with open(ranking_csv, 'r', newline='') as f:
        reader = csv.DictReader(f)

        # レストランDictionaryを作成する
        for row in reader:
            restauraunt_dic.update({row['NAME']: int(row['COUNT'])})

        ##############################
        # １度紹介したオススメのレストランを表示させないために
        # １度紹介したレストランを消していくための
        # オススメ専用辞書を作成
        ##############################
        recommend_dic = deepcopy(restauraunt_dic)

        ##############################
        # レストラン情報があればオススメレストランを表示する
        ##############################
        while len(recommend_dic) > 0:

            # 変数初期化
            tmp_name = ''
            max_name = ''
            tmp_count = 0
            max_count = 0

            ##############################
            # 最多票のレストラン名を取得
            ##############################
            for tmp_name, tmp_count in recommend_dic.items():

                #############################
                # 最多票のレストランに何も入っていない（ループ1回目）もしくは読み込んだ票数が最多票より多い場合
                # かつ
                # 読み込んだレストラン名が既にオススメしたリストではない場合
                # 最多票レストラン名と票数を取得する
                #############################
                if (max_name == '') | (tmp_count > max_count):
                    max_name = tmp_name
                    max_count = tmp_count

            ##############################
            # オススメのレストラン名を設定して
            # レストランDictionaryから既にオススメしたレストラン名を削除する
            ##############################
            recommend = max_name
            del recommend_dic[recommend]

            #############################
            # 最多票のレストランが好きかどうか聞く
            #############################
            with open('msg_dir/recommend_msg.txt') as f:
                r = string.Template(f.read())

            display_msg = r.substitute(recommend_restaurant=recommend)
            yn_answer = input(display_msg)

            # ##############################
            # オススメしたレストランが好きではない（no）の場合
            # 他にオススメのレストランがレストランDictionaryにあれば
            # ループしてレストランDictionaryから次点のレストラン名を取得する
            #
            # 全てのレストランを表示して全て好きでない（no）となった場合
            # ループを抜けて好きなレストランを質問する
            #
            # オススメしたレストランが好き（yes）の場合
            # 対象のレストランの票数を1追加して
            # ループを抜けて好きなレストランを質問する
            # ##############################
            if yn_answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
                restauraunt_dic[recommend] += 1
                break

# ##############################
# # 好きなレストランを質問する
# ##############################
with open('msg_dir/question_msg.txt') as f:
    q = string.Template(f.read())

display_msg = q.substitute(user_name=user)
recommend = (input(display_msg)).title()

##############################
# CSVファイルに好きなレストランを書き込む
##############################

with open(ranking_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()

    ##############################
    # レストランDictionaryにデータがあれば更新してCSVに上書き
    ##############################
    if len(restauraunt_dic) > 0:

        ##############################
        # オススメ質問に全てNoでこたえたが
        # 既にレストランDictionaryに存在しているレストランを入力した場合
        # レストランDictionary内のレストランに1票追加する
        # ※yesでこたえた場合は、既にWhileループの中で1票追加しているので、ここでの処理は不要
        ##############################
        if (recommend in restauraunt_dic) & (
                yn_answer in ['n', 'N', 'no', 'No', 'NO']):
            restauraunt_dic[recommend] += 1

        ##############################
        # レストランDictionaryをCSVに上書き
        ##############################
        for key, value in restauraunt_dic.items():
            writer.writerow({'NAME': key, 'COUNT': value})

    ##############################
    # 入力したレストランがレストランDictionaryに存在しない場合、
    # そのレストランをCSVに追記する
    ##############################
    if recommend not in restauraunt_dic:
        writer.writerow({'NAME': recommend, 'COUNT': 1})

##############################
# 処理の終了
##############################
# 締めの挨拶
with open('msg_dir/closing_msg.txt') as f:
    c = string.Template(f.read())

display_msg = c.substitute(robot_name=robot, user_name=user)
print(display_msg)