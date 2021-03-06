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

What the code does
-----
Firstly, due to the infancy and development of the project, the 'flask run' command
must be called in the terminal. This runs the Python Module flask, and therefore navigating to
the localhost, port 5000 will run this python program. (http://localhost:5000/)

The HTML form has a drop-down menu that allows you to pick which specification
you would like to see. At the top, specification information will be shown. 
This information outlines a brief description explaining what the code does and how it
meets the objective of the specification.

Below this, is the code for the specification. It is written in simple text
to ensure that the code is readable. Above each file, is the text 'NEW FILE'. 
This is to signify that the code below it is in a new file, and is seperated from the code above.
File names could be here, but this is not necessary to fulfill the specification
and can be added in future iterations.

How this solution meets the specification
-----
This solution sufficiently meets the specification. This can be proven 
by going through each part of the specification, and comparing my solution.

* String manipulation

    The code that was written for other specifications were read with '\n' for new lines. This needed to be manipulated, 
 which I managed to successfully remove using a for statement. 

* File IO
    
    Using the open() method in python completed this objective - It allowed for the reading of files (and writing if
    desired, but not in this specification).

* Templating of HTML files

    I used HTML tags to showcase my code in a clear manner. The solution uses HTML tags, Cascading Style Sheets (CSS)
    elements and Javascript elements to fulfill the specification brief.

* Passing of arguments

    Arguments such as the lines of code, the spec number and specification information (such as this) was using 
    argument passing.

