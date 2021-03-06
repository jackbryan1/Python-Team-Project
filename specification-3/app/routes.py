from app import app
from flask import render_template
import glob

@app.route('/')
@app.route('/home')
def home():
    '''render home web-page'''
    return render_template('home.html')

@app.route('/spec1')
def spec1():
    '''render specification 1, parse in code, information and specification number'''
    files = glob.glob("./specification-1/*/*/*.py") + glob.glob("./specification-1/*/*.py") + glob.glob(
        "./specification-1/*.py") #search for python files in directory up to 3 levels
    f = open("specification-1/README.md", 'r')
    spec_info = f.readlines()
    f.close()
    length = len(files)
    lines = []
    for i in range(length): #for each file in directory
        f = open(files[i], 'r')
        lines.append(f.readlines())
        f.close()
    return render_template('spec.html', lines=lines, spec_info=spec_info, spec=1, files=files)

@app.route('/spec2')
def spec2():
    '''render specification 2, parse in code, information and specification number'''
    files = glob.glob("./specification-2/*/*/*.py") + glob.glob("./specification-2/*/*.py") + glob.glob(
        "./specification-2/*.py") #search for python files in directory up to 3 levels
    f = open("specification-2/README.md", 'r')
    spec_info = f.readlines()
    f.close()
    length = len(files)
    lines = []
    for i in range(length): #for each file in directory
        f = open(files[i], 'r')
        lines.append(f.readlines())
        f.close()
    return render_template('spec.html', spec_info=spec_info, lines=lines, spec=2, files=files)

@app.route('/spec3')
def spec3():
    '''render specification 3, parse in code, information and specification number'''
    files = glob.glob("./specification-3/*/*/*.html") + glob.glob("./specification-3/*/*.py") + glob.glob(
        "./specification-3/*.py") #search for python files in directory up to 2 levels, html in third
    f = open("specification-3/README.md", 'r')
    spec_info = f.readlines()
    f.close()
    length = len(files)
    lines = []
    for i in range(length): #for each file in directory
        f = open(files[i], 'r')
        lines.append(f.readlines())
        f.close()
    return render_template('spec.html', lines=lines, spec_info=spec_info, spec=3, files=files)

@app.route('/spec4')
def spec4():
    '''render specification 4, parse in code, information and specification number'''
    files = glob.glob("./specification-4/*/*/*.py") + glob.glob("./specification-4/*/*.py") + glob.glob(
        "./specification-4/*.py") #search for python files in directory up to 3 levels
    f = open("specification-4/README.md", 'r')
    spec_info = f.readlines()
    f.close()
    length = len(files)
    lines = []
    for i in range(length): #for each file in directory
        f = open(files[i], 'r')
        lines.append(f.readlines())
        f.close()
    return render_template('spec.html', lines=lines, spec_info=spec_info, spec=4, files=files)