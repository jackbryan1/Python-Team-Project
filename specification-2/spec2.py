import os
from PIL import Image

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

ask_user = input("What would you like to do?")
if ask_user == "thumb":
    print("Creating thumbnails...")
    create_thumbnail()
else:
    print("Invalid command")
