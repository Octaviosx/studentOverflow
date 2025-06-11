import reflex as rx
from ..UI.logo import logo
from ..pages.login import EstadoLogin

class Redirecciones():
    def mandarlogin():
        return rx.redirect('/login')

    def mandarRegistro():
        return rx.redirect('/registro')

class MoverMouse(rx.State):
    variant = "outline"

    @rx.event
    def cambiar_color(self):
        self.variant = "solid"
        
def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", padding_top='5px'), href=url, padding_top='5px'
    )
    

def navbar_searchbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                logo(),
            ),
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    size="3",
                    color_scheme='lime',
                    padding_top='5px',
                ),                
                rx.link(
                    "Contacto",
                    href="#",
                    size="3",
                    padding_top='5px',
                    color_scheme='lime'
                ),                
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Buscar...",
                    type="search",
                    size="2",
                    justify="end",
                    width="600px"
                ),   
                rx.button(
                    "Registrarse",
                    size="2",
                    variant="outline",
                    color_scheme="lime",
                    on_click=Redirecciones.mandarRegistro
                ),
                rx.button(
                    "Iniciar sesión", 
                    size="2",
                    variant="solid",
                    color_scheme="lime",
                    on_click=Redirecciones.mandarlogin
                ),
                rx.color_mode.button(color_scheme="lime", variant="solid"),
                spacing="4",
                justify="end",
                ),
            justify="between",
            align_items="end",
        ),
        width="100%",       # Asegura que el navbar ocupe todo el ancho
        padding="1.3rem",
        position="sticky",
        top="0",
        z_index="1000",       
    )
#####################################    
#### Nav bar con sesión iniciada ####
#####################################

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar_search_user() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                logo(),
                #align_items="left",
            ),
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="/",
                    size="3",
                    padding_top='5px',
                    color_scheme='lime'
                ),                
                rx.link(
                    "Contacto",
                    href="#",
                    size="3",
                    padding_top='5px',
                    color_scheme='lime'
                ),                  
                rx.input(
                    rx.input.slot(rx.icon("search")),
                    placeholder="Buscar...",
                    type="search",
                    size="2",
                    #justify="center",
                    width="600px",
                ),
                rx.text(f"Hola, {EstadoLogin.usuario} 👋", size="3", padding_top='5px'),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                            color='black',
                            bg='#bdee63'
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Ver perfil"),
                        rx.menu.item("Ajustes"),
                        rx.menu.separator(),
                        rx.menu.item("Salir", on_click=EstadoLogin.logout),
                    ),
                rx.color_mode.button(color_scheme="lime", variant="solid"),
                ),
                spacing="4",
                justify="end",
                ),
            justify="between",
            align_items="end",
        ),
        width="100%",       # Asegura que el navbar ocupe todo el ancho
        padding="1.3rem",
        position="sticky",
        top="0",
        z_index="1000",       
    )