import reflex as rx

class AppState(rx.State):
    cargando: bool = True

    async def cargar_datos(self):
        self.cargando = True
        await self.sleep(2)  # Simula una carga (como si fuera de red)
        self.cargando = False