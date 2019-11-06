import os
from PIL import Image

pic = "../resources/img/spec2-images"
thumb = (512, 512)

for i in os.listdir(pic):
    file, ext = os.path.splitext(i)
    im = Image.open(pic + "/" + i)
    im.convert('RGB')
    im.thumbnail(thumb)
    im.save(file + "_thumbnail" + ".JPEG")
    im.close()

