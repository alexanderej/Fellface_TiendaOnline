from flask import Blueprint

error = Blueprint('error', __name__, template_folder="templates", static_folder='static')
from . import routes