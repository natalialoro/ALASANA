from flask import Flask, render_template, request, redirect, url_for, session

import pymongo

app = Flask(__name__)
app.secret_key = "nataliaroldan123"

myClient = pymongo.MongoClient("mongodb://localhost:27017")
myDb = myClient["userapp"]
myCollection = myDb ["users"]

myUser = {"fullname": "Natalia Londoño", "identification": 1039459769, "city": "Medellin", "country": "Colombia", "password": 1234}

result = myCollection.insert_one(myUser)
print(result)



@app.route('/')
def index():
    return render_template ('login.html')




  

@app.route('/login', methods= ["POST"])
def login():
    if request.method == "POST":
        email = request.form ['email']
        rol = request.form ['rol']
        password = request.form ['password']
        session ['user'] = email
        session ['rol'] = rol
        return redirect(url_for('properties'))
    else:
        return redirect(url_for('register'))

@app.route('/properties')
def properties():
    if 'user' in session and session['rol'] == "Anfi":
        return render_template ('properties.html')
    else:
        return render_template ('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



@app.route('/register', methods= ["POST"])
def register():
      if request.method == "POST":
        Nombre = request.form ['fullname']
        Identificacion = request.form ['identification']
        Ciudad = request.form ['city']
        Pais = request.form ['country']
        Contraseña = request.form ['password']
        session ['user'] = Nombre
        session ['Identificacion'] = Identificacion
        session ['Ciudad'] = Ciudad
        session ['Pais'] = Pais
        session ['Contraseña'] = Contraseña
        return redirect(url_for('properties'))
      else:
        return redirect(url_for('login'))
       





    
    

 

if __name__ == '__main__':
    app.run(debug=True)

    