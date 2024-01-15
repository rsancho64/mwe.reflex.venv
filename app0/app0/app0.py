# from rxconfig import config
import reflex as rx


class State(rx.State):

    itemName = ["tomates", "patatas", "cebollas"]
    count = [0,0,0,]

    def incrementItem(self, intemindex):
        self.count[intemindex] += 1

    def incrementItem(self, intemindex):
        self.count[intemindex] -= 1

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
    
    retorno = [] # ???

    # return rx.vstack(
    #     rx.
    #     rx.hstack(
    #         rx.text("patatas", font_size="2em"),
    #         rx.heading(State.countPatatas, font_size="2em"),
    #     ),
    #     rx.hstack(
    #         rx.button(
    #             "--",
    #             bg="#fef2f2",
    #             color="#b91c1c",
    #             border_radius="lg",
    #             on_click=State.decrementPatatas,
    #         ),
    #         rx.button(
    #             "++",
    #             bg="#ecfdf5",
    #             color="#047857",
    #             border_radius="lg",
    #             on_click=State.incrementPatatas,
    #         ),
    #     ),
    #     # spacing="1em",
    #     rx.hstack(
    #         rx.text("tomates", font_size="2em"),
    #         rx.heading(State.countTomates, font_size="2em"),
    #     ),
    #     rx.hstack(
    #         rx.button(
    #             "--",
    #             bg="#fef2f2",
    #             color="#b91c1c",
    #             border_radius="lg",
    #             on_click=State.decrementTomates,
    #         ),
    #         rx.button(
    #             "++",
    #             bg="#ecfdf5",
    #             color="#047857",
    #             border_radius="lg",
    #             on_click=State.incrementTomates,
    #         ),
    #     ),
    #     # # spacing="1em",

    # )


app = rx.App()
app.add_page(index)
# app.compile() deprecated
