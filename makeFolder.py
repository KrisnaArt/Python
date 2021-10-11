import os

def make_dir(a, b):

    # define the name of the directory to be created
    if(b == "learn"):
        path = "Fotowajah/learn/"+a
    else:
        path = "Fotowajah/detect/"+a    

    # define the access rights
    access_rights = 0o755

    check_folder = os.path.exists(path)

    if not check_folder : #and not check_folder1:
        os.mkdir(path, access_rights)
        print ("Successfully created the directory %s" % path)
        return "oke"
    else :
        print ("Creation of the directory %s failed" % path)
        return "oke"