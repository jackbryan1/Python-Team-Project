from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spec1')
def spec1():
    '''defining spec1, parsing data into html'''
    files = ["./specification-1/README.md"]
    f = open(files[0], 'r')
    lines = []
    lines.append(f.readlines())
    if len(files) == 2:
        f = open(files[1], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec=1)

@app.route('/spec2')
def spec2():
    files = ["./specification-2/README.md", "./specification-2/spec2.py"]
    f = open(files[0], 'r')
    lines = []
    lines.append(f.readlines())
    if len(files) == 2:
        f = open(files[1], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec=2)

@app.route('/spec3')
def spec3():
    files = ["./specification-3/README.md"]
    f = open(files[0], 'r')
    lines = []
    lines.append(f.readlines())
    if len(files) == 2:
        f = open(files[1], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec=3)

@app.route('/spec4')
def spec4():
    files = ["./specification-4/README.md"]
    f = open(files[0], 'r')
    lines = []
    lines.append(f.readlines())
    if len(files) == 2:
        f = open(files[1], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec=4)