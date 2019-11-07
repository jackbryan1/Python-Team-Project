import os
from PIL import Image
from PIL import ImageFilter


pic = "../resources/img/spec2-images"
thumb = (512, 512)

def create_thumbnail():
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.convert('RGB')
        im.thumbnail(thumb)
        im.save(file + "_thumbnail" + ".JPEG")
        im.close()

def apply_emboss():
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.filter(ImageFilter.EMBOSS)
        im.save(file + "_emboss" + ".JPEG")
        im.close()

def apply_contour():
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.filter(ImageFilter.CONTOUR)
        im.save(file + "_contour" + ".JPEG")
        im.close()

def smoothen():
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im.filter(ImageFilter.SMOOTH_MORE)
        im.save(file + "_smooth" + ".JPEG")
        im.close()

def apply_bw():
    for i in os.listdir(pic):
        file, ext = os.path.splitext(i)
        im = Image.open(pic + "/" + i)
        im = im.convert('L')
        im.save(file + "_test" + ".JPEG")
        im.close()

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
