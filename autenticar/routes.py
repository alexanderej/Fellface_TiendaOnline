from flask import redirect, render_template, url_for, request, session, flash
from . import autenticar
from bd import obtener_conexion
from cart.carrito import carrito

@autenticar.route('/login')
def login():
    num=len(carrito)
    return render_template('login.html', carrito=carrito, num=num)

@autenticar.route('/validar_login', methods=['POST'])
def validar_login():
    
    _usuario=request.form['usrname']
    _password=request.form['pass']

    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `usuarios` WHERE usuario=%s AND password=%s",(_usuario,_password))
    usuarios=cursor.fetchone()
    conexion.commit()
    print(_usuario, _password)

    print(usuarios)
    if usuarios:
        session["login"]=True
        session["id"]=usuarios[0]
        session["cedula"]=usuarios[1]
        session["nombre"]=usuarios[2]
        session["apellido"]=usuarios[3]
        session["celular"]=usuarios[4]
        session["email"]=usuarios[5]
        session["user"]=usuarios[6]
        session["pass"]=usuarios[7]
        session["tipoUser"]=usuarios[8]

        if session["tipoUser"]=="admin":
            print("Administrador")
            return redirect(url_for('administrarProductos.cat_ad'))
        else:

            print("Cliente")
            # cursor.execute("SELECT * FROM `carrito` WHERE usuario=%s",(_usuario))
            # carrito=cursor.fetchall()
            # print(carrito)
            return redirect(url_for('catalogo.cat'))

    else:
        # print("No esta registrado")   
        flash('El usuario ingresado no está registrado, o verifique su contraseña') 
        return redirect("/login")


@autenticar.route('/registrarse')
def registrarse():
    num=len(carrito)
    return render_template('registrarse.html', carrito=carrito, num=num)


@autenticar.route('/validar_registro', methods=['POST'])
def validar_registro():
    _usuario=request.form['usrname']
    _password=request.form['pass']
    _cedula=request.form['identificacion']
    _celular=request.form['celular']
    _email=request.form['email']
    _nombres=request.form['nombres']
    _apellidos=request.form['apellidos']
    _tipoUser="cliente"
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `usuarios` WHERE usuario=%s",(_usuario))
    usuarios=cursor.fetchone()
    conexion.commit()

    print(usuarios)
    if not usuarios: ##No existe el usuario ingresado
        cursor.execute("INSERT INTO `usuarios` (`cedula`, `nombres`, `apellidos`, `celular`, `correo`, `usuario`, `password`, `tipoUsuario`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (_cedula, _nombres, _apellidos, _celular, _email, _usuario, _password, _tipoUser))
        conexion.commit()
        cursor.execute("SELECT * FROM `usuarios` WHERE usuario=%s AND password=%s",(_usuario,_password))
        usuarios=cursor.fetchone()
        conexion.commit()
        session["login"]=True
        session["id"]=usuarios[0]
        session["cedula"]=usuarios[1]
        session["nombre"]=usuarios[2]
        session["apellido"]=usuarios[3]
        session["celular"]=usuarios[4]
        session["email"]=usuarios[5]
        session["user"]=usuarios[6]
        session["pass"]=usuarios[7]
        session["tipoUser"]=usuarios[8]

        return redirect(url_for('catalogo.cat'))
        
    else:
        # print("Ya esta registrado") 
        flash('El usuario ingresado ya se encuentra registrado. Por favor ingrese uno nuevo')
        return redirect("/registrarse",)
    # return render_template('admin/login.html')

@autenticar.route('/logout')
def logout():
    session.clear()
    return redirect('/')
