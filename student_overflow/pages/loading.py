import reflex as rx
from ..UI.logo import logo
from ..UI.footer import footer


def loading_view() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.vstack(
                logo(),
                align='center',
                padding_left='3%',
                padding_bottom='3%',
            ),
            rx.spinner(size="3", color="#bdee63", height="10vh"),
            align="center",
            width="100%",
            height="91vh",
            justify='center',
        ),
        footer(),
    )