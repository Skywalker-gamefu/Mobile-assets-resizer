#crtDirs moudel
import os


def creatinDirs():
    resultDirs = ["result/", "source/", "result/XXLarge/", "result/XLarge/", "result/Large/", "result/Normal/", "result/Small/"]
    for k in resultDirs:
        if os.path.exists(k) == True:
                print("("+k+") folder found\n")
        elif os.path.exists(k) == False:
            print("creating ("+k+") folder...\n")
            os.makedirs(k)
           

creatinDirs()