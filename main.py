# this script use to resize mobile apllication images assets.abs
# developed by skywalker using pillow moudel.
# contact 

#---------------------------------------------------------------

# using pip to install pillow
import setup
import CrtDirs
import resize
import os

def main():
        setup.install_and_import('pillow')#install moudels 
        CrtDirs.creatinDirs()#check or create directories
        resize.startRes()
        print("\033[92m * * * SUCCESSFULLY DONE. * * *")
        os.system('pause')

#main function
if __name__ == '__main__':
   main()

    
