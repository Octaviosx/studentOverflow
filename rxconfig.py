import reflex as rx

config = rx.Config(
    app_name="student_overflow",
    plugins=[rx.plugins.TailwindV3Plugin()],
    db_url = "postgresql://postgres:Tanj1ro.postgres@localhost:5432/dbstudentoverflow"
)