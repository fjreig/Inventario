from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import Date, cast, extract, func
from datetime import datetime
from fasthtml.common import *
import pprint
from bson.json_util import dumps

from app.database import db

@dataclass
class Inventario():
    equipo: str
    categoria: str
    fabricante: str
    modelo: str
    descripcion: str
    habilitado: bool

def get_all_tasks():
    cursor = db.inventario.find() 
    valores = list(cursor)
    return(valores)

def get_count_category():
    valores = []
    valores.append({'categoria': 1, 'count': 1 })
    return(valores)

def get_count_habilitado():
    valores = []
    valores.append({'habilitado': 1, 'count': 1 })
    return(valores)

def get_count_rows():
    return(1)

def new_task(valores):
    valores.update({'fechacreacion': datetime.now(), 'fechaactualizacion': datetime.now()})
    post_id = db.inventario.insert_one(valores).inserted_id
    print(post_id)

def update_task(valores):
    a=1

def delete_task(valores):
    a=1