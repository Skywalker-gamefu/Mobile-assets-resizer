#resize.py moudel
import os

srcImgList = os.listdir("source") #get list for all files in source directoryne
resultDirs = ["result/XXLarge/" , "result/XLarge/" , "result/Large/" , "result/Normal/" , "result/Small/"]#folder to save resized images
scalRatio = [1 , 960/1440 , 720/1440 , 480/1440 , 360/1440]
size = [50 , 50] #image size [width and height]
supportedFormat = ["png" , "jpeg" , "jpg"]
print("start resizing ...")

def resizeNow():

    scalIndexer = 0


getInfo()
resizeNow()