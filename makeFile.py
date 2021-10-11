import os

def writeFile(filename,file):
    f= open('fotoWajah/learn/'+filename+'/'+filename+".txt","w+")
    f.write(file)
    if(os.path.exists('fotoWajah/learn/'+filename+'/'+filename+'.txt')):
        print ("----createFile")
        f.close()
        return "oke"
    else:
        print ("----gagal createFile")
        return "gagal"

def writeFile1(filename,file):
    f= open('fotoWajah/detect/'+filename+'/'+filename+"_1"+".txt","w+")
    f.write(file)
    if(os.path.exists('fotoWajah/detect/'+filename+'/'+filename+'_1.txt')):
        print ("----createFile")
        f.close()
        return "oke"
    else:
        print ("----gagal createFile")
        return "gagal"
