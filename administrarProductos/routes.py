import os
from datetime import datetime
from flask import redirect, render_template, request, session, url_for
from . import administrarProductos
from bd import obtener_conexion
from werkzeug.utils import secure_filename


@administrarProductos.route('/catalogo_ad')
def cat_ad():
    if not 'tipoUser' in session: 
        return redirect("/")
    elif session['tipoUser']!='admin':
        return redirect("/")
    print(session)
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos` ORDER BY `tipo`")
    productos=cursor.fetchall()
    #####
    for i in range(len(productos)):
        print(i)
        print(productos[i])
    return render_template('catalogo_ad.html',productos=productos)

@administrarProductos.route('/guardar', methods=['POST'])
def admin_productos_guardar():
    if not 'tipoUser' in session: 
        return redirect("/")
    elif session['tipoUser']!='admin':
        return redirect("/")
    _nombre=request.form['txtNombre']
    _descripcion=request.form['txtdes']
    _tipo=request.form['btnTipo']
    _cantidad=request.form['txtCan']
    _precio=request.form['txtPre']
    _archivo=request.files['txtImagen']
    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%m%d%H%M%S')
    print(_tipo)

    if _archivo.filename!="":
        # filename = secure_filename(_archivo.filename)
        nuevoNombre=_tipo+"_"+horaActual+".png"
        # print(url_for('static', filename='assets/img_p'))
        ruta='static/assets/img_p'
        _archivo.save(os.path.join(ruta, nuevoNombre))
    sql="INSERT INTO `productos` (`nombre`, `descripcion`, `tipo`, `cantidad`,`precio`,`imagen`) VALUES (%s, %s, %s, %s, %s, %s)" 
    datos=(_nombre,_descripcion,_tipo,_cantidad,_precio,nuevoNombre)
    conexion= obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

    print(_nombre)
    print(_descripcion)
    print(_archivo)
    print(nuevoNombre)
    
    return redirect('/catalogo_ad')

@administrarProductos.route('/modificar_catalogo', methods=['POST'])
def cat_mod():
    if not 'tipoUser' in session: 
        return redirect("/")
    elif session['tipoUser']!='admin':
        return redirect("/")
    _id=request.form['txtID']
    print(_id)    
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos` WHERE id=%s",(_id))
    producto=cursor.fetchone()

    print(producto)

    return render_template('modificar_catalogo.html',producto=producto)

@administrarProductos.route('/actualizar', methods=['POST'])
def admin_productos_actualizar():
    if not 'tipoUser' in session: 
        return redirect("/")
    elif session['tipoUser']!='admin':
        return redirect("/")
    _id=request.form['txtID']
    _nombre=request.form['txtNombre']
    _descripcion=request.form['txtdes']
    _tipo=request.form['btnTipo']
    _cantidad=request.form['txtCan']
    _precio=request.form['txtPre']
    _archivo=request.files['txtImagen']
    tiempo = datetime.now()
    horaActual=tiempo.strftime('%Y%H%M%S')
    print(_tipo)
    conexion= obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `productos` WHERE id=%s",(_id))
    producto=cursor.fetchone()
    nuevoNombre=producto[0]
    if _archivo.filename!="" and _archivo.filename!=nuevoNombre:
        # filename = secure_filename(_archivo.filename)
        nuevoNombre=_tipo+"_"+horaActual+".png"
        # print(url_for('static', filename='assets/img_p'))
        ruta='static/assets/img_p'
        _archivo.save(os.path.join(ruta, nuevoNombre))

        if os.path.exists("static/assets/img_p/"+str(producto[0])):
            print("existe")
            os.remove("static/assets/img_p/"+str(producto[0]))
        
    cursor.execute("UPDATE `productos` SET `nombre` = %s, `descripcion` = %s, `tipo` = %s, `cantidad` = %s,`precio` = %s,`imagen` = %s WHERE `productos`.`id` = %s",(_nombre,_descripcion,_tipo,_cantidad,_precio,nuevoNombre,_id))
    conexion.commit()
    
    # sql="INSERT INTO `productos` (`nombre`, `descripcion`, `tipo`, `cantidad`,`precio`,`imagen`) VALUES (%s, %s, %s, %s, %s, %s)" 
    # datos=(_nombre,_descripcion,_tipo,_cantidad,_precio,nuevoNombre)
    # conexion= obtener_conexion()
    # cursor=conexion.cursor()
    # cursor.execute(sql,datos)
    # conexion.commit()

    print(_nombre)
    print(_descripcion)
    print(_archivo)
    print(f"nuevoNombre:{nuevoNombre}")
    
    return redirect('/catalogo_ad')

@administrarProductos.route('/borrar', methods=['POST'])
def admin_productos_borrar():
    if not 'tipoUser' in session: 
        return redirect("/")
    elif session['tipoUser']!='admin':
        return redirect("/")
    _id=request.form['txtID']
    print(_id)

    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `productos` WHERE id=%s",(_id))
    productos=cursor.fetchall()
    conexion.commit()
    print(productos)

    if os.path.exists("static/assets/img_p/"+str(productos[0][0])):
        print("existe")
        os.remove("static/assets/img_p/"+str(productos[0][0]))

    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM `productos` WHERE id=%s",(_id))
    conexion.commit()
    return redirect('/catalogo_ad')