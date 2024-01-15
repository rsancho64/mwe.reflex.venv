# from rxconfig import config
import reflex as rx


class State(rx.State):
    countTomates: int = 0
    countPatatas: int = 0

    def incrementTomates(self):
        self.countTomates += 1

    def decrementTomates(self):
        self.countTomates -= 1

    def incrementPatatas(self):
        self.countPatatas += 1

    def decrementPatatas(self):
        self.countPatatas -= 1


# def newCustomized_rx_hstack():
#     return rx.hstack(
#         rx.button(
#             "--",
#             bg="#fef2f2",
#             color="#b91c1c",
#             border_radius="lg",
#             on_click=State.decrement,
#         ),
#         rx.button(
#             "++",
#             bg="#ecfdf5",
#             color="#047857",
#             border_radius="lg",
#             on_click=State.increment,
#         ),
#     )

def index():
    return rx.vstack(
        rx.hstack(
            rx.text("patatas", font_size="2em"),
            rx.heading(State.countPatatas, font_size="2em"),
        ),
        rx.hstack(
            rx.button(
                "--",
                bg="#fef2f2",
                color="#b91c1c",
                border_radius="lg",
                on_click=State.decrementPatatas,
            ),
            rx.button(
                "++",
                bg="#ecfdf5",
                color="#047857",
                border_radius="lg",
                on_click=State.incrementPatatas,
            ),
        ),
        # spacing="1em",
        rx.hstack(
            rx.text("tomates", font_size="2em"),
            rx.heading(State.countTomates, font_size="2em"),
        ),
        rx.hstack(
            rx.button(
                "--",
                bg="#fef2f2",
                color="#b91c1c",
                border_radius="lg",
                on_click=State.decrementTomates,
            ),
            rx.button(
                "++",
                bg="#ecfdf5",
                color="#047857",
                border_radius="lg",
                on_click=State.incrementTomates,
            ),
        ),
        # # spacing="1em",
                
    )

app = rx.App()
app.add_page(index)
# app.compile() deprecated
