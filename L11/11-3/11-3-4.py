# -*- coding: utf-8 -*-
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello/<username>')
def hello_world2(username):
    return 'hello world! {}'.format(username)

def main():
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()