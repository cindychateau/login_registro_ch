from flask import render_template, redirect, request, session
from flask_app import app

#Importamos Modelo
from flask_app.models.users import User

#Importación de BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    #Validamos la info que recibimos
    if not User.valida_usuario(request.form):
        return redirect('/')
    
    #Guardar registro
    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptando la contraseña del usuario y guardándola en pwd

    #Creamos un diccionario con todos los datos del request.form
    #request.form['password'] = pwd -> ERROR: request.form NO se puede cambiar

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }

    id = User.save(formulario) #Recibir el identificador del nuevo usuario

    session['user_id'] = id #Guardamos en sesión el identificador del usuario

    return redirect('/dashboard')




@app.route('/dashboard')
def dashboard():
    #PENDIENTE validar que si se haya iniciado sesión o registrado
    return render_template('dashboard.html')