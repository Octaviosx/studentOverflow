#Este archivo de va a encargar de controlar toda la informacion 
#que viaje entre la aplicacion y la base de datos correspondiente a la
#tabla usuarios
from rxconfig import config
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, VARCHAR, Text
from sqlalchemy.orm import declarative_base, mapped_column, Mapped

Base = declarative_base() 
#Como se veria una tabla en la db
class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(VARCHAR(60), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    contrasenia: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)