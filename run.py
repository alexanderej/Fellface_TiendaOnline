from flask import Flask, render_template
from catalogo import catalogo
from administrarProductos import administrarProductos
from contacto import contacto
from inicio import inicio
from autenticar import autenticar
from cart import cart
from error import error
from flaskext.mysql import MySQL
from datetime import datetime
from cart.carrito import carrito

miApp = Flask(__name__)
miApp.secret_key='secretKey1234'


miApp.register_blueprint(catalogo)
miApp.register_blueprint(administrarProductos)
miApp.register_blueprint(inicio)
miApp.register_blueprint(autenticar)
miApp.register_blueprint(contacto)
miApp.register_blueprint(cart)
miApp.register_blueprint(error)

# #Configurar la base de datos
# mysql=MySQL()

# miApp.config['MYSQL_DATABASE_HOST']='localhost'
# miApp.config['MYSQL_DATABASE_USER']='root'
# miApp.config['MYSQL_DATABASE_PASSWORD']=''
# miApp.config['MYSQL_DATABASE_DB']='tienda'
# mysql.init_app(miApp)
# conexion=mysql.connect()

@miApp.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada"), 404


if __name__ == '__main__':
    miApp.run(debug=True)