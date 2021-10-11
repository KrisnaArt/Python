from flask import Flask, request, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc, create_engine,Column,Integer,String,Text,select,text
from sqlalchemy.sql.elements import Null
from makeFolder import make_dir
from decodeImage import decode, decode1
from makeFile import writeFile,writeFile1
from getFilePath import filePath, filePath1
from faceRecog import detect_user_face, learn_user_face
import time

app = Flask(__name__)  

engine = create_engine("mysql+mysqldb://root@localhost:3306/skripsi")
Base = declarative_base()
Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()

class fotoUser(Base):
    __tablename__ = 'foto_user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    foto_wajah = Column(Text)
    foto_baru = Column(Text)
    alamat = Column(Text)
    alamat_login = Column(Text)

@app.route('/')
def hello_world():
    return 'Selamat datang di tutorial Flask'

@app.route('/input',methods=['POST'])
def input_user():
    a = ""
    b = 0
    if request.method == 'POST':
        us = fotoUser()
        us.username = request.form['username']
        us.password = request.form['password']
        us.email = request.form['email']
        us.foto_wajah = request.form['foto_wajah']
        us.alamat = request.form['alamat']

        try:
            sql_query = text("SELECT COUNT(username) FROM foto_user WHERE username = '"+us.username+"'")
            result = session.execute(sql_query)
            result_as_list = result.fetchall()

            for row in result_as_list:
                print(row[0])

            if row[0] == 0 :
                if make_dir(us.username, "learn") == "oke":
                    a = "oke1"
                    b = 100
                    print ("---1")
                    if writeFile(us.username,us.foto_wajah) == "oke":
                        a = "oke2"
                        b = 200
                        print ("----2")
                        if decode(us.username) == "oke":
                            a = "oke3"
                            b = 300
                            print ("----3")
                            if learn_user_face() == "oke":
                                print ("----4")
                                milliseconds = int(round(time.time() * 1000))
                                print("learn : "+str(milliseconds))
                                us.foto_wajah = filePath(us.username)
                                session.add(us)
                                session.commit()
                                milliseconds = int(round(time.time() * 1000))
                                print("submit : "+str(milliseconds))
                                a = "oke4"
                                b = 400
                            else:
                                a = "gagal"
                                b = 500
                        else:
                            a = "gagal"
                            b = 600
                    else:
                        a = "gagal"
                        b = 700
                else:
                    a = "gagal"
                    b = 800
            else:
                a = "Username sudah ada"
                b = 900
            return jsonify(status = b, message = a)
        except exc.SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

@app.route('/login',methods=['POST'])
def login_user():
    a = ""
    b = 0
    if request.method == 'POST':
        us = fotoUser()
        us.username = request.form['username']
        us.password = request.form['password']

        try:
            sql_query = text("SELECT COUNT(*) FROM foto_user WHERE username = '"+us.username+"' AND password = '"+us.password+"'")
            result = session.execute(sql_query)
            result_as_list = result.fetchall()

            for row in result_as_list:
                print(row[0])

            if row[0] == 1 :
                milliseconds = int(round(time.time() * 1000))
                print("detect user : "+str(milliseconds))
                a = "oke"
                b = 200
            else:
                a = "gagal"
                b = 300
            return jsonify(status = b, message = a)
        except exc.SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

@app.route('/recog',methods=['POST'])
def recog_user():
    a = ""
    b = 0
    if request.method == 'POST':
        us = fotoUser()
        us.username = request.form['username']
        us.foto_baru = request.form['foto_baru']
        us.alamat_login = request.form['alamat_login']

        try:
            if make_dir(us.username, "detect") == "oke":
                a = "oke1"
                b = 100
                print ("---1")
                if writeFile1(us.username,us.foto_baru) == "oke":
                    a = "oke2"
                    b = 200
                    print ("----2")
                    if decode1(us.username) == "oke":
                        a = "oke3"
                        b = 300
                        print ("----3")
                        us.foto_baru = filePath1(us.username)
                        print("user : "+us.foto_baru)
                        if detect_user_face(filePath1(us.username)) == us.username:
                            print ("----4")
                            milliseconds = int(round(time.time() * 1000))
                            print("detect face : "+str(milliseconds))
                            data=session.query(fotoUser).filter_by(username=us.username).first()
                            data.foto_baru = filePath1(us.username)
                            data.alamat_login = us.alamat_login
                            session.commit()
                            sql_query1 = text("SELECT COUNT(foto_baru) FROM foto_user WHERE username = '"+us.username+"'")
                            result1 = session.execute(sql_query1)
                            result_as_list = result1.fetchall()

                            for row in result_as_list:
                                print(row[0])

                            if row[0] == 1:
                                milliseconds = int(round(time.time() * 1000))
                                print("get face data : "+str(milliseconds))
                                a = "oke4"
                                b = 400
                            else:
                                a = "gagal"
                                b = 500
                        else:
                            a = "gagal"
                            b = 600
                    else:
                        a = "gagal"
                        b = 700
                else:
                    a = "gagal"
                    b = 800
            else:
                a = "gagal"
                b = 900
            return jsonify(status = b, message = a)
        except exc.SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

@app.route('/logout',methods=['POST'])
def logout():
    a = ""
    b = 0
    if request.method == 'POST':
        us = fotoUser()
        us.username = request.form['username']

        try:
            data=session.query(fotoUser).filter_by(username=us.username).first()
            data.foto_baru = None
            data.alamat_login = None
            session.commit()
            sql_query = text("SELECT foto_baru FROM foto_user WHERE username = '"+us.username+"'")
            result = session.execute(sql_query)
            result_as_list = result.fetchall()
            for row in result_as_list:
                print (row[0])
            if row[0] == None :
                a = "oke"
                b = "200"
            else:
                a = "gagal"
                b = "100"
            return jsonify(status = b, message = a)
        except exc.SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error            