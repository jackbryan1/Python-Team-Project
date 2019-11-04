from PIL import Image
import os, sys

pic = "../resources/img/spec2-images/image01.jpg"
thumb = (512, 512)
modf = "../resources/img/spec2-modif"

im = Image.open(pic)

print(im.format, im.size, im.mode)

im.show()

im.convert('RGB')

im.thumbnail(thumb, Image.ANTIALIAS)

im.save(pic + ".thumbnail", "JPEG")

print(os.stat(modf).st_size)

im.show()
