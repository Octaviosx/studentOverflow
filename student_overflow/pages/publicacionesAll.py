import reflex as rx
from rxconfig import config
import bcrypt
from typing import List, Dict, Any
from sqlalchemy import text
from ..pages.login import EstadoLogin
from ..models.usuario import Usuario
from ..models.tb_publicacion import Publicacion
from ..UI.navbar import navbar_searchbar, navbar_search_user
from ..UI.logo import logo
from ..UI.footer import footer


class EstadoPublicaciones(rx.State):
    publicacionesList: List[dict] = []
    @rx.event
    def cargar_publicaciones(self):
        with rx.session() as session:
            stmt = text("""
            SELECT 
                p.id_publicacion, 
                p.titulo, 
                p.descripcion, 
                p.fecha, 
                u.id_usuario,
                u.username AS nombre_usuario
            FROM 
                publicacion p
            JOIN 
                usuario u ON p.id_usuario = u.id_usuario
            ORDER BY 
                p.fecha DESC
            LIMIT 5;
        """)
            resultado = session.exec(stmt)
            self.publicacionesList = [dict(r._mapping) for r in resultado]
        
        #print("Datos cargados:", EstadoPublicaciones.publicacionesList)

    

@rx.page(route='/publicaciones', title='publicaciones', on_load=EstadoPublicaciones.cargar_publicaciones)
def publicaciones() -> rx.Component:
    def navbar_condicional():
        return rx.cond(
            EstadoLogin.id_usuario != 0,
            navbar_search_user(),
            navbar_searchbar()
        )
    return rx.vstack(
        navbar_condicional(),
        rx.box(height="6em", z_index="1000",padding_bottom='5em'),
        rx.center(
            rx.box(
                rx.hstack(
                    rx.hstack(
                        rx.heading(
                            'Publicaciones',
                            size='9',
                            #padding_bottom='20px',
                        ),
                    ),
                    rx.hstack(
                        rx.button(
                            "Haznos saber tu duda",
                            size="3", 
                            idth="100%", 
                            color_scheme='lime',
                            align='right',
                            on_click=rx.redirect('/publicar')
                        ),
                        justify="end",
                        spacing="9",
                    ),
                    justify="between",
                    align_items="end",
                    padding_bottom='2em'
                ),            
                rx.separator(),
                rx.flex(
                    rx.foreach(
                        EstadoPublicaciones.publicacionesList,  # sin paréntesis ✅
                        lambda pub: rx.card(
                            rx.heading(pub["titulo"], size="4", on_click=rx.redirect(f'/publicacion/{pub["id_publicacion"]}'),cursor="pointer", ),
                            rx.text(pub["descripcion"], padding_bottom='1em'),
                            rx.text(f'Fecha: {pub["fecha"]}  Autor: {pub["nombre_usuario"]}', size="2", color="gray", align='right'),
                            #rx.text(f'Autor: {pub["nombre_usuario"]}', size="1", color="lime"),
                            padding="1rem",
                            margin_bottom="1rem"
                        )
                    ),
                    padding="2em",
                    background_color="var(--gray-2)",
                    width='1200px',
                    direction="column",
                    spacing="3"
                ),
                position="sticky",
                #top="0",
                left="0",
                width="100%",
                box_shadow="md",
            ),
            max_width="1200px",
            width="100%",
            margin="auto",
        ),
        footer(),
    )