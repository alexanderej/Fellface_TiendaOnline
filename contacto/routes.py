from flask import render_template
from . import contacto
from cart.carrito import carrito

num=len(carrito)
@contacto.route('/contacto')
def contacto():
    return render_template('contacto.html', carrito=carrito, num=num) 