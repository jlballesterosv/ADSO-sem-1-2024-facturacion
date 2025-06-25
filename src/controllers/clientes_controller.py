from flask import render_template, request
from flask_controller import FlaskController
from src.models.clientes import Clientes
from src.app import app


class ClientesController(FlaskController):
    @app.route('/lista_clientes')
    def lista_clientes():
        try:
            clientes = Clientes.traer_clientes()
            return render_template('lista_clientes.html',titulo='Ver clientes', clientes = clientes)
        except:
            return render_template('lista_clientes.html',titulo='Error de conexión a la base de datos')    

    @app.route('/consultar_cliente_numero_identificacion/<numero_identificacion>')
    def consultar_cliente_numero_identificacion(numero_identificacion):
        cliente = Clientes.obtener_cliente_por_numero_identificacion(numero_identificacion)
        return cliente
    