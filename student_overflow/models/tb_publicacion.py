from rxconfig import config
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, VARCHAR, Text, Date
from sqlalchemy.orm import declarative_base, mapped_column, Mapped

Base = declarative_base() 
#Como se veria una tabla en la db
class Publicacion(Base):
    __tablename__ = "publicacion"
    id_publicacion: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(VARCHAR(150), unique=True, nullable=False)
    descripcion: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    fecha: Mapped[str] = mapped_column(Date, nullable=False)
    id_usuario: Mapped[int] = mapped_column(Integer, nullable=False)