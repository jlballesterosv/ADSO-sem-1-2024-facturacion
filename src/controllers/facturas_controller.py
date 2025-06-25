from flask import render_template
from flask_controller import FlaskController

from src.app import app


class FacturasController(FlaskController):
  

    @app.route('/formulario_factura', methods=['GET','POST'])
    def formulario_factura():     
      
        return render_template('formulario_factura.html',titulo='Nueva Factura')

