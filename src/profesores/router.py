import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.profesores import schemas, services

# Creamos un logger para este módulo específico. Más info.: https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/profesores", tags=["profesores"])

# Rutas para Profesores

@router.post("/", response_model=schemas.Profesor)
def create_profesor(profesor: schemas.ProfesorCreate, db: Session = Depends(get_db)):
    logger.info("Creando profesor desde endpoint...")  # <- este mensaje se verá por la terminal
    return services.crear_profesor(db, profesor)

@router.get("/", response_model=list[schemas.Profesor])
def read_profesor(db: Session = Depends(get_db)):
    logger.info("Consultando la lista de profesores desde endpoint...")  # <- este mensaje se verá por la terminal
    return services.listar_profesores(db)