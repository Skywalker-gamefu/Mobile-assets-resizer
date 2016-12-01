# setup moudel



def install_and_import(package):
    print("* * * INSTALL DEPENDENCIES. * * *\n")
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        
        pip.main(['install', package])
    finally:
        globals()['PIL'] = importlib.import_module('PIL')
        print("All modules installed.\n")



if __name__ == "setup":
    pass