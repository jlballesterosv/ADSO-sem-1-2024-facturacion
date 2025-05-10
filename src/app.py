from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html',titulo='Bienvenido a la aplicación de facturación')

@app.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html',titulo='Ver productos')

@app.route('/formulario_producto', methods=['GET','POST'])
def formulario_producto():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        print ("Entró por POST")
        print(codigo)    
    return render_template('formulario_producto.html',titulo='Crear un producto')

@app.route('/se_guardo')
def se_guardo():
    return render_template('se_guardo.html',titulo='Se guardó!!!')


class Productos():
    id = Column(Integer, primary_key=True)
    codigo = Column(String(9), unique=True, nullable=False)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10,8))
    unidad_medida = Column(String(3), unique=True, nullable=False)
    cantidad_stock = Column(Float(10,8))
    categoria = Column(Integer, nullable=False)
