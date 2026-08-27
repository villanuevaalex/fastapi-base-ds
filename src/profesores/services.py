import logging
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.profesores.models import Profesor
from src.profesores import schemas


# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

# operaciones CRUD para Profesores

def crear_profesor(db: Session, profesor: schemas.Profesor) -> schemas.Profesor:
    _profesor = Profesor(**profesor.model_dump())
    db.add(_profesor)
    db.commit()
    db.refresh(_profesor)
    return _profesor

def listar_profesores(db: Session) -> List[schemas.Persona]:
    logger.info("Listando profesores desde services")  # <- este mensaje se verá por la terminal
    return db.scalars(select(Profesor)).all()