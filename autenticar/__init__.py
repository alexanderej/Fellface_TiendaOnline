from flask import Blueprint

autenticar = Blueprint('autenticar',__name__,template_folder='templates')

from . import routes