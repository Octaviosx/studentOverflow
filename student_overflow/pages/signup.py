import reflex as rx
import bcrypt
from ..models.usuario import Usuario
from ..UI.logo import logo

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
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.vstack(
                rx.vstack(
                    logo(),
                    padding_left='170px',
                    width='120%'
                ),
                rx.heading('Registrate', size='8', margin_bottom="10px", margin_top="40px"),
                rx.text('Ingresa tu nombre de usuario'),
                rx.input(
                    placeholder='Usuario',
                    size='3',
                    type='text',
                    required=True,
                    value=EstadoRegistro.usuario, #permite guardar la información
                    on_change=EstadoRegistro.asignarUsuario
                ),
                rx.text('Ingresa tu correo electronico'),
                rx.input(
                    placeholder='Correo elecronico',
                    size='3',
                    required=True,
                    type='email',
                    value=EstadoRegistro.email, #permite guardar la información
                    on_change=EstadoRegistro.asignarCorreo
                ),
                rx.text('Ingresa una contraseña'),
                rx.input(
                    placeholder='Contraseña',
                    size='3',
                    required=True,
                    type='password',
                    value=EstadoRegistro.contrasenia, #permite guardar la información
                    on_change=EstadoRegistro.asignarContrasenia
                ),
                rx.button(
                    "Registrarse",
                    on_click=EstadoRegistro.registrarUsuario,
                    variant='soft',
                    color_scheme='lime',
                    radius='medium',
                    margin_top='15px'
                ),
                align_items='center'
            ),
            height="80vh"
        )
    )