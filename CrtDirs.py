#crtDirs moudel
import os


def creatinDirs():
    print("* * * CREATING FOLDERS IF NOT EXISTS. * * *\n")
    resultDirs = ["result/", "source/", "result/XXLarge/", "result/XLarge/", "result/Large/", "result/Normal/", "result/Small/"]
    for k in resultDirs:
        if os.path.exists(k) == True:
                print("("+k+") folder found")
        elif os.path.exists(k) == False:
            print("creating ("+k+") folder...")
            os.makedirs(k)
           



if __name__ == "CrtDirs":
    pass