import pyrebase 
from flask import Flask, render_template, request

config={
    "apiKey": "AIzaSyBJLcng2_OwEKGF209mkGzs-PQzDyVxFM8",
    "authDomain": "drugai.firebaseapp.com",
    "projectId": "drugai",
    "storageBucket": "drugai.appspot.com",
    "messagingSenderId": "895269842002",
    "appId": "1:895269842002:web:11eeb1939724b86006038b",
    "measurementId": "G-2TB21YF0ZK",
    "databaseURL": "https://drugai.firebaseio.com",

  }
 
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

app=Flask(__name__, static_folder='static',
            template_folder='templates')
#inicio
@app.route("/")
def home():
    return render_template('Inicio.html')
#inicio de sesion
@app.route("/iniciar")
def iniciar():
    return render_template('iniciar.html')
#Base de datos inicio de sesion
@app.route('/iniciar',methods=['GET','POST'])
def basic():
    unsuccessful='Verifique los datos ingresados'
    if request.method=='POST':
        email=request.form['name']
        password=request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('homeu.html')
        except:
            render_template('homeu.html', us= unsuccessful)

    return render_template("iniciar.html")
#Informacion
@app.route("/informacion")
def informacion():
    return render_template('informacion.html')

#Home usuario
@app.route("/homeu")
def homeu():
    return render_template('homeu.html')

#Prediccion
@app.route("/prediccion")
def prediccion():
    return render_template('prediccion.html')

if __name__=="__main__":
    app.run(debug=True)