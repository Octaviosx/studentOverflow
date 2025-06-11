"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .pages.login import login, EstadoLogin
from .pages.signup import registro
from .pages.publicacion import publicacion
from .UI.navbar import navbar_searchbar, navbar_search_user
from .UI.footer import footer

class State(rx.State):
    """The app state."""

async def getNavbar():
    estadoSesion = await rx.get_state(EstadoLogin)
    print(estadoSesion)
#selecciona el navbar según si se ha iniciado sesión    
def index() -> rx.Component:
    def navbar_condicional():
        return rx.cond(
            EstadoLogin.id_usuario != None,
            navbar_search_user(),
            navbar_searchbar()
        )
    # Welcome Page (Index)
    return rx.vstack(
        navbar_condicional(),
        rx.vstack(
            rx.image(
                src=rx.asset("hybridge_logo.png"),
                width="8%",
                height="auto",
                padding_top='6em'
            ),
            rx.heading("Empoderar al mundo para desarrollar tecnología a través del conocimiento colectivo.", size="9", align='center'),
            rx.text(
                "Comparte tus dudas de desarrollo e informática y la comunidad te dará una mano.",
                size="5",
                padding_bottom='6em'
            ),
            rx.separator(),
            rx.text(rx.text.strong("Podrás encontrar soluciónes para cualquier:"), size="6"),
            rx.vstack(
                rx.text('Lenguaje, framework...', size='4'),
                rx.grid(
                    rx.card(rx.image(src=rx.asset("Java-logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("angular_logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("Csharp_Logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("python-logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("flutter.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("javascript-logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("sql-logo.png")), width="100%"),
                columns="7",
                spacing="4",
                width="100%",
                ),
                align='center'
            ),
            rx.vstack(
                rx.text('Nube', size='4'),
                rx.grid(
                    rx.card(rx.image(src=rx.asset("Azure-logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("aws-logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("gcp-logo.png")), width="100%"),
                    rx.card(rx.image(src=rx.asset("alibaba-logo.png")), width="100%"),
                columns="4",
                spacing="9",
                width="100%",
                ),
                align='center'
            ),
            direction="column",
            width="100%",
            spacing="6",
            align='center',
            justify="center",
            min_height="70vh",
            padding_left='17em',
            padding_right='17em',
        ),
        footer()
    )


style = {
    "font_family": "Arial",
}

app = rx.App(style=style)
#rutas
app.add_page(index)
app.add_page(login)
app.add_page(registro)
app.add_page(publicacion)
