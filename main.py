from pydoc import cli
from flask import Flask, render_template
from ChatMojiBot import *
import asyncio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/textToEmoji')
# async
def textToEmoji():
    # await send_receive()
    # asyncio.run(send_receive())
    # print("click")
    return(runner())
    # return "done"






@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
