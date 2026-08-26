from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Profesor(ModeloBase):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    # fecha_ingreso: Mapped[datetime] = mapped_column(DateTime)
    # departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))
    # departamento: Mapped["Departamento"] = relationship(back_populates="profesores")
    # cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")