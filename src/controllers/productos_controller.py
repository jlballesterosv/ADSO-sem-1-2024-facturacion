from flask import render_template, request
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.categorias import Categorias
from src.app import app


class ProductosController(FlaskController):
    @app.route('/lista_productos')
    def lista_productos():
        try:
            productos = Productos.traer_productos()
            return render_template('lista_productos.html',titulo='Ver productos', productos = productos)
        except:
            return render_template('lista_productos.html',titulo='Error de conexión a la base de datos')    

    @app.route('/formulario_producto', methods=['GET','POST'])
    def formulario_producto():
        categorias = Categorias.traer_categorias() 
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            descripcion = request.form.get('descripcion')
            valor_unitario = request.form.get('valor_unitario')
            cantidad_inventario = request.form.get('cantidad_inventario') 
            unidad_medida = request.form.get('unidad_medida')
            categoria = request.form.get('categoria')
            producto_almacenar = Productos(codigo,descripcion,valor_unitario,unidad_medida,cantidad_inventario,categoria)        
            producto_repetido =  Productos.traer_producto_por_descripcion(descripcion)
            if producto_repetido:
                return render_template('formulario_producto.html'
                                    ,titulo='Crear un producto'
                                    ,errorProducto = "La descripción no se puede repetir"
                                    ,categorias = categorias
                                    ,producto_almacenar = producto_almacenar)
            try:
                Productos.crear_producto(producto_almacenar)
            except:            
                return render_template('formulario_producto.html',titulo='Error al registrar en la base de datos',categorias = categorias) 
        return render_template('formulario_producto.html',titulo='Crear un producto',categorias = categorias)

