from flask import render_template
from . import error

@error.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Pagina no encontrada"), 404
