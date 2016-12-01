# this script use to resize mobile apllication images assets.abs
# developed by skywalker using pillow moudel.
# contact 

#---------------------------------------------------------------

# using pip to install pillow
import setup
import CrtDirs

def main():
        setup.install_and_import('pillow')#install moudels 
        CrtDirs.creatinDirs()#check or create directories

#main function
if __name__ == '__main__':
   main()
   
    
