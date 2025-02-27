from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime
from fasthtml.common import *

from app.database import Base, session, engine

@dataclass
class Inventario(Base):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, index=True)
    fechacreacion = Column(DateTime, default=datetime.utcnow)
    fechamodificacion = Column(DateTime, default=datetime.utcnow)
    equipo = Column(String)
    categoria = Column(String)
    fabricante = Column(String)
    modelo = Column(String)
    descripcion = Column(String)
    habilitado = Column(Boolean)

def get_all_tasks():
    result = session.query(Inventario).with_entities(
        Inventario.id.label('id'),
        Inventario.equipo.label('equipo'),
        Inventario.categoria.label('categoria'),
        Inventario.fabricante.label('fabricante'),
        Inventario.modelo.label('modelo'),
        Inventario.descripcion.label('descripcion'),
        Inventario.habilitado.label('habilitado'),
        Inventario.fechacreacion.label('fechacreacion'),
        Inventario.fechamodificacion.label('fechamodificacion')
        ).order_by(Inventario.id.asc()).all()
    valores = []
    for i in range(len(result)):
        valores.append({
            'id': result[i][0], 
            'equipo': result[i][1], 
            'categoria': result[i][2], 
            'fabricante': result[i][3],
            'modelo': result[i][4],
            'descripcion': result[i][5],
            'habilitado': result[i][6],
            'fechacreacion': result[i][7],
            'fechamodificacion': result[i][8],
            })
    return(valores)

def get_count_category():
    result = session.query(Inventario.categoria, 
        func.count(Inventario.categoria)).group_by(Inventario.categoria).all()
    valores = []
    for i in result:
        valores.append({'categoria': i[0], 'count': i[1] })
    return(valores)

def get_count_habilitado():
    result = session.query(Inventario.habilitado, 
        func.count(Inventario.habilitado)).group_by(Inventario.habilitado).all()
    valores = []
    for i in result:
        valores.append({'habilitado': i[0], 'count': i[1] })
    return(valores)

def get_count_rows():
    result = session.query(func.count(Inventario.id)).all()
    return(result[0][0])

def new_task(valores):
    ticket = Inventario(
        equipo = valores['equipo'],
        categoria = valores['categoria'],
        fabricante = valores['fabricante'],
        modelo = valores['modelo'],
        descripcion = valores['descripcion'],
        habilitado = valores['habilitado'],
        ) 
    session.add(ticket)
    session.commit()

def update_task(valores):
    inventario = session.query(Inventario).filter(Inventario.id == valores['id']).one()
    inventario.equipo = valores['equipo']
    inventario.categoria = valores['categoria']
    inventario.fabricante = valores['fabricante']
    inventario.modelo = valores['modelo']
    inventario.descripcion = valores['descripcion']
    inventario.habilitado = valores['habilitado']
    inventario.fechamodificacion = valores['fechamodificacion']
    session.commit()

def delete_task(valores):
    inventario = session.query(Inventario).filter(Inventario.id == valores['id']).one()
    session.delete(inventario)
    session.commit()