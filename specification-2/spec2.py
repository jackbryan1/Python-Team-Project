import os
from PIL import Image
from PIL import ImageFilter

# Path to folder with pictures
pic = "../resources/img/spec2-images"

# Thumbnail size
thumb = (512, 512)


def create_thumbnail():
    """Creates thumbnails of all pictures in pic path."""
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.convert('RGB')
        im.thumbnail(thumb)
        im.save(file + "_thumbnail" + ".JPEG")
        im.close()


def apply_emboss():
    """Applies the emboss filter to all pictures in pic path."""
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.filter(ImageFilter.EMBOSS)
        im.save(file + "_emboss" + ".JPEG")
        im.close()


def apply_contour():
    """Applies the contour filter to all pictures in pic path."""
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.filter(ImageFilter.CONTOUR)
        im.save(file + "_contour" + ".JPEG")
        im.close()


def smoothen():
    """Smoothens all pictures in pic path."""
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.filter(ImageFilter.SMOOTH_MORE)
        im.save(file + "_smooth" + ".JPEG")
        im.close()


def apply_bw():
    """Changes the RGB values to black and white for all pictures in pic path."""
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im = im.convert('L')
        im.save(file + "_test" + ".JPEG")
        im.close()


# Input acts like a command line
ask_user = input("What would you like to do?")

if ask_user == "thumbnail":
    print("Creating thumbnails...")
    create_thumbnail()

elif ask_user == "emboss":
    print("Applying emboss...")
    apply_emboss()

elif ask_user == "contour":
    print("Applying contour...")
    apply_contour()

elif ask_user == "smooth":
    print("Smoothening...")
    smoothen()

elif ask_user == "bw":
    print("Applying black and white filter...")
    apply_bw()

else:
    print("Invalid command")

# Strings for yes or no commands
yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n'}

# Path to newly created images
newpic = "../specification-2"

choice = input("Would you like to see the created images?").lower()

if choice in yes:
    print("Opening pictures...")
    for j in os.listdir(newpic):
        newim = Image.open(newpic + "/" + j)
        newim.show()
        newim.close

elif choice in no:
    print("Closing program.")

else:
    print("Please respond with 'yes' or 'no'")