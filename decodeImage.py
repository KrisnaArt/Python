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
    i = 0
    while os.path.exists(f"fotoWajah/detect/"+filename+"/face_{i}.txt"):
        while os.path.exists(f"fotoWajah/detect/"+filename+"/face_{i}.jpg"):
            i += 1

    file = open(f"fotoWajah/detect/"+filename+"/face_{i}.txt", "r")

    if(os.path.exists(f"fotoWajah/detect/"+filename+"/face_{i}.jpg")):
        with open(f"fotoWajah/detect/"+filename+"/face_{i}.jpg", "wb") as fh:
            fh.write(base64.decodebytes(file.read().encode()))
            test = Image.open(f"fotoWajah/detect/"+filename+"/face_{i}.jpg").rotate(90)
            test.save(f"fotoWajah/detect/"+filename+"/face_{i}.jpg")
        if(os.path.exists(f"fotoWajah/detect/"+filename+"/face_{i}.jpg")):
            print ("----decode")
            file.close()
            os.remove(f"fotoWajah/detect/"+filename+"/face_{i}.txt")
            return "oke"
        else:
            print ("----gagal decode")
            return "gagal"