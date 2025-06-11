import reflex as rx
import bcrypt
from ..models.usuario import Usuario
from ..UI.logo import logo
from ..UI.footer import footer

class EstadoRegistro(rx.State):
    usuario: str = ''
    email: str = ''
    contrasenia: str = ''
    
    @rx.event
    def asignarUsuario(self, usuario_ingresado):
        self.usuario = usuario_ingresado
        
    @rx.event
    def asignarCorreo(self, correo_ingresado):
        self.email = correo_ingresado
    
    @rx.event       
    def asignarContrasenia(self, contrasenia_ingresada):
        self.contrasenia = contrasenia_ingresada
    
    @rx.event    
    def mostrar_info(self):
        print(self.usuario)
        print(self.email)
        print(self.contrasenia)
    
    @rx.event    
    def registrarUsuario(self):
        try:
        # Hashear la contraseña antes de guardarla
            hashed_password = bcrypt.hashpw(self.contrasenia.encode(), bcrypt.gensalt()).decode()
            with rx.session() as canal:
                canal.add(
                Usuario(
                    username=self.usuario, 
                    email=self.email,
                    contrasenia=hashed_password
                    )
                )
                canal.commit()
                self.usuario = ''
                self.email = ''
                self.contrasenia = ''
            return rx.redirect('/login')

        except Exception as e:
            self.error_msg = f"Error al registrar: {str(e)}"
            
            
@rx.page(route='/registro', title='Registro')
def registro() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.card(
                rx.vstack(
                    rx.center(
                        rx.vstack(
                            logo(),
                            padding_left='4em'
                        ),
                        rx.heading(
                            "Registrate",
                            size="6",
                            as_="h2",
                            text_align="center",
                            width="100%",
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Usuario",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="user.dev",
                            type="user",
                            size="3",
                            width="100%",
                            required=True,
                            value=EstadoRegistro.usuario, #permite guardar la información
                            on_change=EstadoRegistro.asignarUsuario
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Correo Electronico",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("at-sign")),
                            placeholder="user@correo.dev",
                            type="email",
                            size="3",
                            width="100%",
                            value=EstadoRegistro.email, #permite guardar la información
                            on_change=EstadoRegistro.asignarCorreo
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Contraseña",
                                size="3",
                                weight="medium",
                            ),
                            justify="start",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Ingresa tu contraseña",
                            type="password",
                            size="3",
                            width="100%",
                            value=EstadoRegistro.contrasenia, #permite guardar la información
                            on_change=EstadoRegistro.asignarContrasenia
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.button(
                        "Registrarse",
                        on_click=EstadoRegistro.registrarUsuario,
                        variant='soft',
                        color_scheme='lime',
                        radius='medium',
                        margin_top='15px',
                        width='100%'
                    ),
                    spacing="6",
                    width="100%",
                ),
                max_width="28em",
                size="4",
                width="100%",
            ),
            justify="center",
            align='center',
            height="92vh",
            #width='100vh'
            padding_left='38%'
        ),
        footer(),
    )