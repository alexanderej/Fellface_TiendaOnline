from flask import render_template, session
from . import catalogo
from bd import obtener_conexion
from cart.carrito import carrito, num, Producto




@catalogo.route('/catalogo')
def cat():
    num=len(carrito)
    # print(session)
    # carrito.agregar(Producto(6,5))
    print(carrito.productos)
    print(num)
    return render_template('catalogo.html', carrito=carrito, num=num)

@catalogo.route('/faciales/<number_page>')
def faciales(number_page):
    number_page=int(number_page)
    num=len(carrito)
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("select count(*) from `productos` WHERE tipo='productos faciales'")
    num_prod=cursor.fetchone()[0]
    # print(num_prod,type(num_prod))
    ######Controlar cuantos se muestran en cada pagina
    productos_por_pagina=4
    num_paginas=int(num_prod/productos_por_pagina) ##Mostraremos de 10 productos
    resultado=num_prod/productos_por_pagina
    if resultado>num_paginas:
        num_paginas+=1
    # print(num_paginas)
    # print(number_page)
    a_partir=0
    
    for num_p in range(1,num_paginas+1):
        if num_p == number_page:
            cursor.execute("SELECT * FROM `productos` WHERE tipo='productos faciales' LIMIT %s,%s",(a_partir,productos_por_pagina))
            
        a_partir+=productos_por_pagina

    productos=cursor.fetchall()
    conexion.commit()
    # print(productos)    

    return render_template('faciales.html', productos=productos, carrito=carrito, num=num, num_paginas=num_paginas)

@catalogo.route('/cabello/<number_page>')
def cabello(number_page):
    number_page=int(number_page)
    num=len(carrito)
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("select count(*) from `productos` WHERE tipo='productos cabello'")
    num_prod=cursor.fetchone()[0]
    # print(num_prod,type(num_prod))
    ######Controlar cuantos se muestran en cada pagina
    productos_por_pagina=4
    num_paginas=int(num_prod/productos_por_pagina) ##Mostraremos de 10 productos
    resultado=num_prod/productos_por_pagina
    if resultado>num_paginas:
        num_paginas+=1
    # print(num_paginas)
    # print(number_page)
    a_partir=0
    
    for num_p in range(1,num_paginas+1):
        if num_p == number_page:
            cursor.execute("SELECT * FROM `productos` WHERE tipo='productos cabello' LIMIT %s,%s",(a_partir,productos_por_pagina))
            
        a_partir+=productos_por_pagina

    productos=cursor.fetchall()
    conexion.commit()
    # print(productos)    

    return render_template('cabello.html', productos=productos, carrito=carrito, num=num, num_paginas=num_paginas)

@catalogo.route('/perfumes/<number_page>')
def perfumes(number_page):
    number_page=int(number_page)
    num=len(carrito)
    conexion=obtener_conexion()
    cursor=conexion.cursor()
    cursor.execute("select count(*) from `productos` WHERE tipo='perfumes'")
    num_prod=cursor.fetchone()[0]
    # print(num_prod,type(num_prod))
    ######Controlar cuantos se muestran en cada pagina
    productos_por_pagina=4
    num_paginas=int(num_prod/productos_por_pagina) ##Mostraremos de 10 productos
    resultado=num_prod/productos_por_pagina
    if resultado>num_paginas:
        num_paginas+=1
    # print(num_paginas)
    # print(number_page)
    a_partir=0
    
    for num_p in range(1,num_paginas+1):
        if num_p == number_page:
            cursor.execute("SELECT * FROM `productos` WHERE tipo='perfumes' LIMIT %s,%s",(a_partir,productos_por_pagina))
            
        a_partir+=productos_por_pagina

    productos=cursor.fetchall()
    conexion.commit()
    # print(productos)    

    return render_template('perfumes.html', productos=productos, carrito=carrito, num=num, num_paginas=num_paginas)