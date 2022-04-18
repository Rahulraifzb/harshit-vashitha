# Installation of pillow library
# change the image extension
# resize image files
# resize multiple images using for loop
# Sharpness
# Brightness
# Color
# Contrast
# Image blur,GaussianBlur

from PIL import Image,ImageEnhance,ImageFilter
import os

# img1 = Image.open("dog.jpg")
# img1.save("dog1.png")
# img1.show()

# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save("dog1small.jpg")

# for item in os.listdir():
#     if item.endswith(".jpg"):
#         img2 = Image.open("dog.jpg")
#         filename,extension = os.path.splitext(item)
#         img2.save(f'{filename}.png')

# img1 = Image.open("dog.jpg")
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(10).save("dogsharp.jpg")
# 0 : Blurry
# 1 : Original Image
# 2 : Image with increased sharpness


###### Color ######
# img2 = Image.open("dog.jpg")
# enhencer = ImageEnhance.Color(img2)
# enhencer.enhance(0).save("dogbw.jpg")


###### -------- Brightness -------- ######

# img2 = Image.open("dog.jpg")
# enhencer = ImageEnhance.Brightness(img2)
# enhencer.enhance(0).save("dogbw.jpg")


###### -------- Contrast -------- ######
# img2 = Image.open("dog.jpg")
# enhencer = ImageEnhance.Contrast(img2)
# enhencer.enhance(1.5).save("dogbw.jpg")

###### -------- Image Filter -------- ######

img2 = Image.open("dog.jpg")
img2.filter(ImageFilter.GaussianBlur(radius=5)).save("dogblur.jpg")