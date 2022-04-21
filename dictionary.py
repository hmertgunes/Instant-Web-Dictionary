import justpy as jp
from definition import Definiton


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        list = jp.QList(a=scroller)
        jp.A(a=list, text="Home", href="/", classes="p-2 m-2 text-lg text-gray-600 hover:text-blue")
        jp.Br(a=list)
        jp.A(a=list, text="About", href="/about", classes="text-lg text-gray-600 hover:text-blue p-2 m-2")
        jp.Br(a=list)
        jp.A(a=list, text="Dictionary", href="/dictionary", classes="text-lg text-gray-600 hover:text-blue p-2 m-2")
        jp.Br(a=list)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                icon="menu", click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")
        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="INSTANT ENGLISH DICTIONARY",
               classes="text-4xl m-2 text-center py-2 px-4 m-2")
        jp.Div(a=div, text="Get the definition of any word that you type in below.",
               classes="text-lg text-left py-2 px-4 m-2 ")
        div2 = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg bg-gray-100 border-2 border-gray-500 h-1/2")
        input_div = jp.Input(a=div2, placeholder="Type a word here...", outputdiv=output_div,
                             classes="text-lg m-2 bg-gray-100 border-2 border-gray-500 rounded w-100 focus:bg-white "
                                     "focus:outline-none focus:border-red-500 py-2 px-4")
        input_div.on("input", cls.get_definition)
        # jp.Button(a=div2, text="Click", classes="text-lg bg-gray-100 border-2 border-gray-500 m-2 py-2 px-4 rounded "
        #                                       "text-gray-600 hover:bg-red-500 hover:text-white w-100",
        #         click=cls.get_definition, outputdiv=output_div, inputdiv=input_div)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = Definiton(widget.value).get()
        widget.outputdiv.text = " ".join(defined)

    @staticmethod
    def move_drawer(widget, msg):
        if not widget.drawer.value:
            widget.drawer.value = True
        else:
            widget.drawer.value = False
