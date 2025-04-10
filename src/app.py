from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html',titulo='Bienvenido a la aplicación de facturación')

@app.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html',titulo='Ver productos')

@app.route('/formulario_producto')
def formulario_producto():
    return render_template('formulario_producto.html',titulo='Crear un producto')


@app.route('/se_guardo')
def se_guardo():
    return render_template('se_guardo.html',titulo='Se guardó!!!')