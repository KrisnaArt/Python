import base64
import os
from PIL import Image

def decode(filename):
    f =  open('fotoWajah/learn/'+filename+'/'+filename+'.txt',"r")

    with open('fotoWajah/learn/'+filename+'/'+filename+'.jpg', "wb") as fh:
        fh.write(base64.decodebytes(f.read().encode()))
        test = Image.open('fotoWajah/learn/'+filename+'/'+filename+'.jpg').rotate(90)
        test.save('fotoWajah/learn/'+filename+'/'+filename+'.jpg')
    if(os.path.exists('fotoWajah/learn/'+filename+'/'+filename+'.jpg')):
        print ("----decode")
        f.close()
        os.remove('fotoWajah/learn/'+filename+'/'+filename+".txt")          
        return "oke"
    else:
        print ("----gagal decode")
        return "gagal"
    
def decode1(filename):
    f =  open('fotoWajah/detect/'+filename+'/'+filename+'_1.txt',"r")

    with open('fotoWajah/detect/'+filename+'/'+filename+'_1.jpg', "wb") as fh:
        fh.write(base64.decodebytes(f.read().encode()))
        test = Image.open('fotoWajah/detect/'+filename+'/'+filename+'_1.jpg').rotate(90)
        test.save('fotoWajah/detect/'+filename+'/'+filename+'_1.jpg')
    if(os.path.exists('fotoWajah/detect/'+filename+'/'+filename+'_1.jpg')):
        print ("----decode")
        f.close()
        os.remove('fotoWajah/detect/'+filename+'/'+filename+"_1"+".txt")
        return "oke"
    else:
        print ("----gagal decode")
        return "gagal"