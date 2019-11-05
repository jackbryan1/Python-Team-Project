from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    lines=[
        {'author':'Oscar', 'content':'This is Team 27'},
        {'author':'John', 'content':'This is Team 34'}
    ]
    return render_template('index.html', lines=lines)

@app.route('/other')
def other():
    return render_template('other.html')

