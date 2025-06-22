import reflex as rx
from ..UI.logo import logo


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon, color='#bdee63'), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("linkedin", "https://www.linkedin.com/in/octavio-solis-203238245/"),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="auto",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src=rx.asset("hybridge_logo.png"),
                            width="8%",
                            height="auto",
                        ),
                        rx.text(
                            "© Octavio Solis",
                            size="3",
                            white_space="nowrap",
                            weight="medium",
                            padding_top='2px'
                        ),
                    ),
                    spacing="2",
                    align="center",
                    width="100%",
                ),
                socials(),
                spacing="4",
                width="100%",
                padding='1em'
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
        background_color="var(--gray-2)",
        position="fixed",
        bottom="0",
        left="0",  
        z_index="1000", 
    )