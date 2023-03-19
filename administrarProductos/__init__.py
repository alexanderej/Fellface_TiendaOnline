from flask import Blueprint

administrarProductos = Blueprint('administrarProductos',__name__,template_folder='templates', static_folder='static')

from . import routes