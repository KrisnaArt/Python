#!/usr/bin/env python
import os
import sys

folderName = sys.argv[1]
folderName1 = sys.argv[2]

# define the name of the directory to be created
path = "./images/foto_wajah/"+folderName
path1 = "./images/foto_ktp/"+folderName1

# define the access rights
access_rights = 0o755

check_folder = os.path.exists(path)
check_folder1 = os.path.exists(path1)

if not check_folder and not check_folder1:
    os.mkdir(path, access_rights)
    os.mkdir(path1, access_rights)
    print ("Successfully created the directory %s" % path)
    print ("Successfully created the directory %s" % path1)
else :
    print ("Creation of the directory %s failed" % path)
    print ("Creation of the directory %s failed" % path1)