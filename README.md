TEAM PROJECT (PRACTICAL 3) TEAM 27
=====

Specification 1
=====

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
created in each specification's directory, and 'show' these on a HTML form.

Installation
-----
The Flask Package is used in this project, as is Flaskenv.

Usage
-------
The ```flask run``` command must be called in the terminal. This runs the Python Module flask, and therefore 
navigating to the localhost, port 5000 will display this python program. ```http://localhost:5000/```

The HTML form has a drop-down menu that allows you to pick which specification
you would like to see. At the top, specification information will be shown. 
This information outlines a brief description, explaining what the code does and how it
meets the objective of the specification. Next, a list of all files in each specification's
directory found by my program (using glob module)

Below this, is the code for the specification. It is written in simple text
to ensure that the code is readable. Above each file, is the red text 'NEW FILE'. 
This is to signify that the code below it is in a new file, and is separated from the code above.


Specification 4
=====