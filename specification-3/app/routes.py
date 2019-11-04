from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user={'username': 'John'}
    lines=[
        {'author':'Oscar', 'content':'This is Team 27'},
        {'author':'John', 'content':'This is Team 34'}
    ]
    return render_template('index.html', user=user, lines=lines)
