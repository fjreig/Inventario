from fasthtml import FastHTML
from pathlib import Path
from fasthtml.common import *
from monsterui.all import *
from datetime import datetime

from app.models import new_task, update_task, delete_task
from app.lista import consultar_datos

hdrs = (Theme.green.headers())
app, rt = fast_app(hdrs=hdrs)

@dataclass
class New_Element:
    equipo: str
    categoria: str
    fabricante: str
    modelo: str
    descripcion: str
    habilitado: bool

@dataclass
class Update_Element:
    id: str
    equipo: str
    categoria: str
    fabricante: str
    modelo: str
    descripcion: str
    habilitado: bool

@dataclass
class Delete_Element:
    id: str

@rt('/')
def index():
    return consultar_datos()

@rt("/register")
def post(elemento: New_Element):
    valores = elemento.__dict__
    new_task(valores)
    return Redirect(f"/")

@rt("/update")
def post(elemento: Update_Element):
    valores = elemento.__dict__
    valores.update(fechamodificacion=datetime.now())
    update_task(valores)
    return Redirect(f"/")

@rt("/borrar")
def post(elemento: Delete_Element):
    valores = elemento.__dict__
    delete_task(valores)
    return Redirect(f"/")

serve()