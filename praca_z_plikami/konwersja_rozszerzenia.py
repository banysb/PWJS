from PIL import Image
import os
dir = os.getcwd()
files = []
files.append(dir+"\kot.jpg")
files.append(dir+"\pies.jpg")
files.append(dir+"\malpa.jpg")
files.append(dir+"\panda.jpg")
for item in files:
    image = Image.open(item)
    image.save(item.replace(".jpg", ".png"))
