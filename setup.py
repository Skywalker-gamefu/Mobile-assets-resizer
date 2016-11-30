# setup moudel



def install_and_import(package):

    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        
        pip.main(['install', package])
    finally:
        globals()['PIL'] = importlib.import_module('PIL')
        print("all moudels installed")



if __name__ == "setup":
    pass