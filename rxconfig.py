import reflex as rx

config = rx.Config(
    app_name="student_overflow",
    plugins=[rx.plugins.TailwindV3Plugin()],
    db_url = "postgresql://<usuario>:<contraseña>@localhost:5432/db"
)