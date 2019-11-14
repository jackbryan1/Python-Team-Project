TEAM PROJECT (PRACTICAL 3) TEAM 27
=====

Specification 1
=====

According to the chart letter E, T, A is the letter that appears most frequently in book.txt.

These are the most frequently occurring words in book.txt

Word   | Frequency 
----  | ----  
The|14602
Of|6711
And|6449
a|4697
To|4659
In|4212
That|2955
His|2522
It|2382
i|1943



Run **'python3 main.py'**  in the terminal to run this program. Make 
sure that **book.txt** and **main.py** are in the same directory before running.
If you want to change the name of the output file or the number 
of output words, modify the code in line **76** of **main.py**.

Specification 2
=====

This package allows creating thumbnails with 512x512 sizes and applies the filters: emboss, contour, smooth, black and white.

## Installation

The [Pillow](https://pillow.readthedocs.io/en/stable/) package is used in this project

## Usage

```thumbnail```
creates thumbnails of pictures in "spec2-images" folder

```emboss```
applies the emboss filter on pictures in "spec2-images" folder

```contour```
applies the contour filter on pictures in "spec2-images" folder

```smooth```
applies the smooth filter on pictures in "spec2-images" folder

```bw```
creates black and white versions of pictures in "spec2-images" folder

After using a command you will receive a prompt asking if the program should display the newly created images. 

```yes``` ```y``` ```y``` ``` ``` displays every image

```no``` ```n``` closes the program

Specification 3
=====

Specification 3 is all about showing the team's code in a nice, clean format.
Using Flask, I have created a generalised program that will take all files
created in each specification's directory, and show these on a HTML form.

Installation
-----
The Flask Package is used in this project, as is Flaskenv.

Usage
-------
```flaskenv``` must be installed onto the virtual environment. This is done
through the command ```pip install python-dotenv```. This gives python the capability
to read the .flaskenv file included in this repository. Alternatively, the command
```set  FLASK_APP=specification-3/flask-executable.py``` can be run. Both of these methods 
tell the flask module where to look for the executable file. 

The ```flask run``` command must be called in the terminal. This runs the Python Module flask, and therefore 
navigating to the localhost, port 5000 will display this python program. ```http://localhost:5000/```

The HTML form has a drop-down menu that allows you to pick which specification
you would like to see. 

At the top, specification information will be shown. 
This information outlines a brief description, explaining what the code does and how it
meets the objective of the specification. 

Next, a list of all files in each specification's
directory found by my program (using glob module).

Below this is the code for the specification. It is written in simple text
to ensure that the code is readable. Above each file, is the red text 'NEW FILE'. 
This is to signify that the code below it is in a new file, and is separated from the code above.


Specification 4
=====

Specification 4
=====
About
-----

Specification 4 is a unique specification in that there isnt a particular python library to use, so there is complete creative freedom 

How to Use
-------

example command:

pipenv run python specification-4\start.py test test hash

can also write compare instead of hash \
anything can be written in place of either test

What the code does
-----

The code allows the user to type in a password and have it encrypted and stored. The user can then type in a password to check it against the stored passwords.

How this solution meets the specification
-----

We researched different python libraries and chose Bcrypt to use. We checked that this is not similar to any existing specifications, and then we started working on the code. 
