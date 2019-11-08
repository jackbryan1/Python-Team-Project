from app import app
from flask import render_template
import glob

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spec1')
def spec1():
    files = glob.glob("./specification-1/*/*/*.py") + glob.glob("./specification-1/*/*.py") + glob.glob(
        "./specification-1/*.py")
    f = open("specification-1/spec1-info.md")
    spec_info = f.readlines()
    length = len(files)
    lines = []
    for i in range(length):
        f = open(files[i], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec_info=spec_info, spec=1)

@app.route('/spec2')
def spec2():
    files = glob.glob("./specification-2/*/*/*.py") + glob.glob("./specification-2/*/*.py") + glob.glob(
        "./specification-2/*.py")
    f = open("specification-2/spec2-info.md")
    spec_info = f.readlines()
    length = len(files)
    lines = []
    for i in range(length):
        f = open(files[i], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', spec_info=spec_info, lines=lines, spec=2)

@app.route('/spec3')
def spec3():
    files = glob.glob("./specification-3/*/*/*.html") + glob.glob("./specification-3/*/*.py") + glob.glob(
        "./specification-3/*.py")
    f = open("specification-3/spec3-info.md")
    spec_info = f.readlines()
    length = len(files)
    lines = []
    for i in range(length):
        f = open(files[i], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec_info=spec_info, spec=3)

@app.route('/spec4')
def spec4():
    files = glob.glob("./specification-4/*/*/*.py") + glob.glob("./specification-4/*/*.py") + glob.glob(
        "./specification-4/*.py")
    f = open("specification-4/spec4-info.md")
    spec_info = f.readlines()
    length = len(files)
    lines = []
    for i in range(length):
        f = open(files[i], 'r')
        lines.append(f.readlines())
    return render_template('spec.html', lines=lines, spec_info=spec_info, spec=4)