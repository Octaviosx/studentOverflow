import reflex as rx

def logo():
    return rx.hstack(
        rx.image(
            src=rx.asset("hybridge_logo.png"),
            width="11%",
            height="auto",
        ),
        rx.text(
            "Student",
            rx.text.strong("Overflow"),
            size="7",
            padding_top='5px'
        ),
    )