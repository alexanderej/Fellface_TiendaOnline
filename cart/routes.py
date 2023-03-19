from flask import make_response, render_template

from cart.carrito import Producto, carrito
from . import cart

from datetime import datetime
from flask import redirect, render_template, request, session, url_for
from bd import obtener_conexion
#import pdfkit

@cart.route('/agregar', methods=['POST'])
def agregar():
    if len(carrito)==0:
        tiempo = datetime.now()
        horaActual=tiempo.strftime('%Y%m%d%H%M%S')
        idcarrito="cart"+horaActual
    else:
        idcarrito=carrito.productos[0].id_carrito
    print("id del carrito",idcarrito)
    _id=request.form['txtID']
    _pagina=request.form['pagina']
    _cantidad=int(request.form['cantidad'])

    conexion = obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos` WHERE id=%s",(_id))
    producto=cursor.fetchone()

    nombre=producto[1]
    imagen=producto[2]
    tipo=producto[3]
    disponibles=producto[4]
    descripcion=producto[5]
    precio=producto[6]
    precio_total=precio*_cantidad
    nuevaCantidad=disponibles-_cantidad

    cursor.execute("UPDATE `productos` SET `cantidad` = %s WHERE `productos`.`id` = %s",(nuevaCantidad,_id))
    conexion.commit()

    prod=Producto(_id,nombre,imagen,tipo,_cantidad,descripcion,precio_total,idcarrito)

    print("prod",prod)
    carrito.agregar(prod)
    print("car",carrito)
    return redirect(_pagina+'/1')

@cart.route('/quitar', methods=['POST'])
def quitar():
    _id=request.form['txtID']
    _cantidad=int(request.form['cantidad'])
    posicion=int(request.form['posicion'])


    conexion = obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `productos` WHERE id=%s",(_id))
    producto=cursor.fetchone()

    nombre=producto[1]
    imagen=producto[2]
    tipo=producto[3]
    disponibles=producto[4]
    descripcion=producto[5]
    precio=producto[6]
    precio_total=precio*_cantidad
    nuevaCantidad=disponibles+_cantidad

    cursor.execute("UPDATE `productos` SET `cantidad` = %s WHERE `productos`.`id` = %s",(nuevaCantidad,_id))
    conexion.commit()

    # prod=Producto(_id,nombre,imagen,tipo,_cantidad,descripcion,precio_total)

    print("pos",posicion)
    carrito.quitar(posicion)
    print(carrito)
    return redirect('/mostrarCarrito')




@cart.route('/mostrarCarrito')
def mostrarCarrito():
    num=len(carrito)
    pagar=carrito.total_pagar()
    return render_template('carrito.html', carrito=carrito, num=num, pagar=pagar)

@cart.route('/comprar')
def comprar():
    num=len(carrito)
    return render_template('comprar.html', carrito=carrito, num=num)

@cart.route('/validar_compra', methods=['POST'])
def validar_compra():
    num=len(carrito)
    pagar=carrito.total_pagar()
    idcarrito=carrito.productos[0].id_carrito
    _direccion=request.form['direccion']
    # _password=request.form['pass']
    _cedula=request.form['identificacion']
    _celular=request.form['celular']
    _email=request.form['email']
    _nombres=request.form['nombres']
    _apellidos=request.form['apellidos']
    # _tipoUser="cliente"
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    
    for i in range(0,len(carrito)):
        id_prod=carrito.productos[i].id
        cant=carrito.productos[i].cantidad
        precioT=carrito.productos[i].precio_total
        cursor.execute("SELECT imagen FROM `productos` WHERE id=%s",(id_prod))
        producto=cursor.fetchone()
        imagen=producto[0]

        # print(usuarios)

        cursor.execute("INSERT INTO `compras` (`email`,`direccion`,`cedula`, `nombres`, `apellidos`, `celular`, `id_producto`,`imagen`, `cantidad`, `precio_total`, `id_carrito`) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (_email,_direccion,_cedula, _nombres, _apellidos, _celular, id_prod, imagen, cant, precioT,idcarrito))
        conexion.commit()
    cursor.execute("SELECT productos.nombre, productos.imagen, productos.tipo, compras.cantidad, compras.precio_total, compras.fecha, compras.direccion, compras.cedula, compras.nombres, compras.apellidos, compras.celular FROM `productos`,`compras` WHERE productos.id=compras.id_producto AND email=%s AND id_carrito=%s",(_email, idcarrito))
    compras=cursor.fetchall()
    conexion.commit()
    print(compras)
    fecha=compras[0][5]
    cliente=compras[0][8]+" "+compras[0][9]
    cedula=compras[0][7]
    direccion=compras[0][6]
    celular=compras[0][10]
    carrito.limpiar()
    num=len(carrito)
    
    return render_template('mostrarCompra.html', pagar=pagar, compras=compras, num=num, _email=_email, idcarrito=idcarrito, fecha=fecha, cliente=cliente, cedula=cedula,direccion=direccion,celular=celular)

@cart.route('/generar_pdf', methods=['POST'])
def generar_pdf():
    _email=request.form['email']
    idcarrito=request.form['idcarrito']
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    
    cursor.execute("SELECT productos.nombre, productos.imagen, productos.tipo, compras.cantidad, compras.precio_total, compras.fecha, compras.direccion FROM `productos`,`compras` WHERE productos.id=compras.id_producto AND email=%s AND id_carrito=%s",(_email, idcarrito))
    compras=cursor.fetchall()
    conexion.commit()

    rendered = render_template('pdf.html', compras=compras, idcarrito=idcarrito)
    config = pdfkit.configuration(wkhtmltopdf='wkhtmltox-0.12.6-1.msvc2015-win64.exe')
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    response = make_response(pdf)
    
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=salida.pdf'
    return response     
    # return render_template('comprar.html',)

           

