from flask import render_template, url_for
from . import inicio
from cart.carrito import carrito


@inicio.route('/')
def inicio():
    print(carrito)
    num=len(carrito)
    print(num)
    return render_template('index.html', carrito=carrito, num=num)


