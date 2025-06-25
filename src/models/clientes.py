from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
import json


class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    documento_identidad = Column(String(20), unique=True, nullable=False)
    nombre_completo = Column(String(100), nullable=False)
    direccion = Column(String(300), nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(200))

    def __init__(self,documento_identidad,nombre_completo,direccion,telefono,email):
        self.documento_identidad = documento_identidad
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def crear_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente
    
    def traer_clientes():
        clientes =  session.query(Clientes).all()
        return clientes
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def obtener_cliente_por_numero_identificacion(numero_identificacion):
        cliente = session.query(Clientes).filter(Clientes.documento_identidad == numero_identificacion).first()
        print(cliente)
        return json.dumps(cliente.as_dict())