import reflex as rx
from rxconfig import config
import bcrypt
import sqlalchemy
from ..models.usuario import Usuario
from ..UI.logo import logo
from ..UI.footer import footer
from ..UI.estados import AppState
from ..pages.loading import loading_view

class EstadoLogin(rx.State):
    usuario: str = ''
    contrasenia: str = ''
    error_msg: str = ''
    id_usuario: int = None
    

    @rx.event
    def asignarUsuario(self, usuario_ingresado):
        self.usuario = usuario_ingresado
    
    @rx.event       
    def asignarContrasenia(self, contrasenia_ingresada):
        self.contrasenia = contrasenia_ingresada
    
    @rx.event
    def onlogin(self):
        if not self.usuario or not self.contrasenia:
            self.error_msg = "Por favor, ingresa usuario y contraseña"
            return
    
        try:
            with rx.session() as session:
                stmt = sqlalchemy.text(
                    "SELECT id_usuario, contrasenia FROM usuario WHERE username = :username").bindparams(username=self.usuario)
                
                result = session.exec(stmt)
                usuario = result.one_or_none()

                if usuario:
                    id_usuario = usuario[0] 
                    hashed_password = usuario[1]
                    #debuggear que usario detecta
                    #print(f"[DEBUG] user = {usuario}")
                    if bcrypt.checkpw(self.contrasenia.encode(), hashed_password.encode()):
                        self.id_usuario = id_usuario
                        self.error_msg = ''
                        self.usuario = ''
                        self.contrasenia = ''
                        AppState.cargar_datos,
                        loading_view(),
                        return rx.redirect('/#')
                    else:
                        self.error_msg = "Contraseña incorrecta"
                        self.usuario = ''
                        self.contrasenia = ''
                else:
                    self.error_msg = "Usuario no encontrado"
                    self.usuario = ''
                    self.contrasenia = ''
        except Exception as e:
            self.error_msg = f"Error en login: {str(e)}"
            self.error_msg = ''
            
    def logout(self):
        self.id_usuario = None  # Limpiar sesión
        rx.spinner
        AppState.cargar_datos()
        return rx.redirect("/#")  # Redirigir a login      

           

@rx.page(route='/login', title='Iniciar sesión')
def login() -> rx.Component:
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
                            "Iniciar sesión",
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
                            placeholder="Juan.dev7427",
                            type="user",
                            size="3",
                            width="100%",
                            value=EstadoLogin.usuario, #permite guardar la información
                            on_change=EstadoLogin.asignarUsuario
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Contraseña",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Ingresa tu contraseña",
                            type="password",
                            size="3",
                            width="100%",
                            value=EstadoLogin.contrasenia, #permite guardar la información
                            on_change=EstadoLogin.asignarContrasenia
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Iniciar sesión",
                        size="3", 
                        width="100%", 
                        color_scheme='lime',
                        on_click=EstadoLogin.onlogin,
                    ),
                    rx.cond(
                        EstadoLogin.error_msg,
                        rx.text(EstadoLogin.error_msg, color="red"),
                        rx.box()
                    ),
                    rx.center(
                        rx.text("¿Aún no tienes cuenta?", size="3"),
                        rx.link("Registrate", href="/registro", size="3"),
                        opacity="0.8",
                        spacing="2",
                        direction="row",
                    ),
                    spacing="6",
                    width="100%",
                ),
                size="4",
                max_width="28em",
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
    """return rx.container(
        rx.center(
            rx.vstack(
                rx.vstack(
                  logo(),
                  padding_left='75px'                  
                ),
                rx.heading('Inicio de sesión', size='8', margin_bottom="10px"),
                rx.input(
                    placeholder='Correo electronico',
                    type='email',
                    size='3',
                    value=EstadoLogin.email, #permite guardar la información
                    on_change=EstadoLogin.asignarCorreo
                ),
                rx.input(
                    placeholder='Contraseña',
                    type='password',
                    size='3',
                    value=EstadoLogin.contrasenia,
                    on_change=EstadoLogin.asignarContrasenia
                ),
                rx.button(
                    "Iniciar sesión",
                    on_click=EstadoLogin.mostrar_info,
                    variant='soft',
                    color_scheme='lime',
                    radius='medium',
                    margin_top='15px'
                ),
                align='center'
            ),
            height="60vh"
        )
    )"""