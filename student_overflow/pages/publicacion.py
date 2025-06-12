import reflex as rx
from rxconfig import config
import sqlalchemy
from ..pages.login import EstadoLogin
from ..UI.navbar import navbar_searchbar, navbar_search_user
from ..UI.footer import footer
from ..models.tb_publicacion import Publicacion
import datetime as dt


class EstadoPublicacion(rx.State):
    titulo: str = ''
    descripcion: str = ''

    @rx.event
    def asignarTitulo(self, titulo_ingresado):
        self.titulo = titulo_ingresado
    
    @rx.event       
    def asignarDescripcion(self, descripcion_ingresada):
        self.descripcion = descripcion_ingresada
       
    @rx.event    
    async def publicar(self):
        estado_login = await self.get_state(EstadoLogin)
        # Si estado_login no es None, entonces usa estado_login.id_usuario.
        # Si estado_login es None (por ejemplo, no hay estado de sesión cargado), entonces asigna 0.
        id_usuario = estado_login.id_usuario if estado_login else 0

        if not id_usuario:
            EstadoLogin.error_msg = "No estás logueado"
            return
        with rx.session() as canal:
            canal.add(
            Publicacion(
                titulo=self.titulo,
                descripcion=self.descripcion,
                fecha=dt.date.today(),
                id_usuario = id_usuario,
                )
            )
            canal.commit()
            self.titulo = ''
            self.descripcion = ''
        return rx.redirect('/')

@rx.page(route='/publicacion', title='Publicacion')
def publicacion() -> rx.Component:
    def navbar_condicional():
        return rx.cond(
            EstadoLogin.id_usuario != 0,
            navbar_search_user(),
            navbar_searchbar()
    )
    return rx.vstack(
        navbar_condicional(),
        rx.vstack(
            rx.center(
                rx.card(
                    rx.vstack(
                        rx.center(
                            rx.heading(
                                "Formula una pregunta",
                                size="6",
                                as_="h2",
                                text_align="left",
                                width="100%",
                            ),
                            direction="column",
                            spacing="5",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Titulo",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                placeholder="Error en cadena de conexión...",
                                type="text",
                                size="3",
                                width="100%",
                                value=EstadoPublicacion.titulo,
                                on_change=EstadoPublicacion.asignarTitulo
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    "Descripción",
                                    size="3",
                                    weight="medium",
                                ),
                                justify="between",
                                width="100%",
                            ),
                            rx.text_area(
                                placeholder="Escribe tu duda o error para ayudarte",
                                type="text",
                                size="3",
                                width="100%",
                                value=EstadoPublicacion.descripcion,
                                on_change=EstadoPublicacion.asignarDescripcion
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button("Publicar", size="3", width="100%", color_scheme='lime', on_click=EstadoPublicacion.publicar),
                        spacing="6",
                        width="100%",
                    ),
                size="5",
                max_width="50em",
                width="1000px",
                ),
            
            padding_top='18vh',
            padding_bottom='18vh',
            padding_left='50vh',
            align_items='center'
            ),        
        ),
        footer()      
    )