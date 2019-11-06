from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spec1')
def spec1():
    '''defining spec1, parsing data into html'''
    f = open("./specification-1/README.md", 'r')
    lines = (f.readlines())
    return render_template('spec.html', lines=lines, spec=1)

@app.route('/spec2')
def spec2():
    f = open("./specification-2/spec2.py", 'r')
    lines = (f.readlines())
    return render_template('spec.html', lines=lines, spec=2)

@app.route('/spec3')
def spec3():
    f = open("./specification-3/README.md", 'r')
    lines = (f.readlines())
    return render_template('spec.html', lines=lines, spec=3)

@app.route('/spec4')
def spec4():
    f = open("./specification-4/README.md", 'r')
    lines = (f.readlines())
    return render_template('spec.html', lines=lines, spec=4)