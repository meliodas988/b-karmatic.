from flask import Flask
import time
from threading import Thread

app=Flask('')

@app.route('/')




def home():
    return f'im kinda alive, also ()'

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t=Thread(target=run)
    t.start()