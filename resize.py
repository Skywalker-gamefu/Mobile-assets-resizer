#resize.py moudel
import os
from PIL import Image

srcImgList = os.listdir("source") #get list for all files in source directoryne
resultDirs = ["result/XXLarge/" , "result/XLarge/" , "result/Large/" , "result/Normal/" , "result/Small/"]#folder to save resized images
scalRatio = [1 , 960/1440 , 720/1440 , 480/1440 , 360/1440]
size = [50 , 50] #image size [width and height]
supportedFormat = ["png" , "jpeg" , "jpg"]
scalIndexer = 0


def resizeNow(folderToSave):
    for x in srcImgList:
        if  x[-3:] in supportedFormat:#if x is image file end with supportedFormat[]
            img = Image.open("source/"+x) # read single image every time
            size[0] = img.width * scalRatio[scalIndexer]
            size[1] = img.height * scalRatio[scalIndexer]
            img.thumbnail(size, Image.ANTIALIAS)
            img.save(folderToSave+x , "png")
        else:
            print("\033[93m WARNING "+ x + " is not image file." )
            continue

def startRes():
    print("\n* * * START RESIZING IMAGES * * *.\n")
    global scalIndexer
    for i in resultDirs:
        print(i+" folder is fill.")
        resizeNow(i)
        scalIndexer+= 1
