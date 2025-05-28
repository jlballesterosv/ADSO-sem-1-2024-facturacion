from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

engine = create_engine("mysql+pymysql://root@localhost/factura243?charset=utf8mb4")

connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
Base.metadata.bind = engine



@app.route('/')
def index():

    return render_template('index.html',titulo='Bienvenido a la aplicación de facturación')

@app.route('/lista_productos')
def lista_productos():
    try:
        productos = Productos.traer_productos()
        return render_template('lista_productos.html',titulo='Ver productos', productos = productos)
    except:
        return render_template('lista_productos.html',titulo='Error de conexión a la base de datos')
    

@app.route('/formulario_producto', methods=['GET','POST'])
def formulario_producto():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        descripcion = request.form.get('descripcion')
        producto =  session.query(Productos).filter(Productos.descripcion == descripcion).first()
        if producto:
            return render_template('formulario_producto.html',titulo='Error:producto repetido')
        valor_unitario = request.form.get('valor_unitario')
        cantidad_inventario = request.form.get('cantidad_inventario')        
        unidad_medida = request.form.get('unidad_medida')
        categoria = request.form.get('categoria')
        producto = Productos(codigo,descripcion,valor_unitario,unidad_medida,cantidad_inventario,categoria)
        try:
            Productos.crear_producto(producto)
        except:            
            return render_template('formulario_producto.html',titulo='Error al registrar en la base de datos')
 
    categorias = Categorias.traer_categorias() 
    return render_template('formulario_producto.html',titulo='Crear un producto',categorias = categorias)

@app.route('/se_guardo')
def se_guardo():
    return render_template('se_guardo.html',titulo='Se guardó!!!')


class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    codigo = Column(String(9), unique=True, nullable=False)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10,8))
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self,codigo,descripcion,valor_unitario,unidad_medida,cantidad_stock,categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria

    def crear_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto

    def traer_productos():
        productos =  session.query(Productos).all()
        return productos




class Categorias(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)

    
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria

    def traer_categorias():
        categorias = session.query(Categorias).all()
        return categorias
        
    

Base.metadata.create_all(engine)

