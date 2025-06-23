import reflex as rx
from rxconfig import config
from typing import Optional
from typing import List, Dict, Any
from sqlalchemy import text, select
from ..pages.login import EstadoLogin
from ..models.usuario import Usuario
from ..models.tb_publicacion import Publicacion
from ..UI.navbar import navbar_searchbar, navbar_search_user
from ..UI.logo import logo
from ..UI.footer import footer

class EstadoPublicaciones(rx.State):
    publicacionSeleccionada: dict = {}
        
    @rx.event
    def cargar_publicacion_por_id(self, id_publicacion: int):
        with rx.session() as session:
            stmt = text("""
                SELECT 
                    p.id_publicacion, p.titulo, p.descripcion, p.fecha, 
                    u.username AS nombre_usuario
                FROM publicacion p
                JOIN usuario u ON p.id_usuario = u.id_usuario
                WHERE p.id_publicacion = :id_pub
                LIMIT 1;
            """)
            resultado = session.exec(stmt, {"id_pub": id_publicacion}).first()
            if resultado:
                self.publicacionSeleccionada = dict(resultado._mapping)
            else:
                self.publicacionSeleccionada = {}

        print(f"Publicación cargada para id {id_publicacion}:", self.publicacionSeleccionada)


@rx.page(route="/publicacion/[id_publicacion]", title="Publicacion")
def publicacion(id_publicacion: Optional[int] = None) -> rx.Component:
    if id_publicacion is None:
        return rx.text("No se proporcionó id de publicación.")
    print("id_publicacion recibido:", id_publicacion)
    
    EstadoPublicaciones.cargar_publicacion_por_id(id_publicacion)
    
    pub = EstadoPublicaciones.publicacionSeleccionada
    if not pub:
        return rx.text("Publicación no encontrada")
    
    def navbar_condicional():
        return rx.cond(
            EstadoLogin.id_usuario != 0,
            navbar_search_user(),
            navbar_searchbar()
        )

    # Obtenemos la publicación desde la base de datos
    with rx.session() as session:
        pub = session.exec(
            select(Publicacion).where(Publicacion.id_publicacion == id_publicacion)
        ).first()
        print("Resultado de la consulta publicacion:", pub)

    if not pub:
        print('No encontré ninguna publicación')
        return rx.text("Publicación no encontrada")
    
    return rx.vstack(
        navbar_condicional(),
        rx.box(height="6em", z_index="1000", padding_bottom='5em'),
        rx.center(
            rx.box(
                rx.hstack(
                    rx.heading(pub.titulo, size='9'),
                    rx.button(
                        "Haznos saber tu duda",
                        size="3",
                        width="100%",
                        color_scheme='lime',
                        on_click=rx.redirect('/publicar'),
                        align='right',
                    ),
                    justify="between",
                    align_items="end",
                    padding_bottom='2em'
                ),
                rx.separator(),
                rx.text(pub.descripcion, padding_bottom='1em'),
                rx.text(f'Fecha: {pub.fecha}  Autor: {pub.usuario.username}', size="2", color="gray", align='right'),
                padding="1rem",
                margin_bottom="1rem",
            ),
            max_width="1200px",
            width="100%",
            margin="auto",
        ),
        footer(),
    )


