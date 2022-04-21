import justpy as jp


class About:
    path = "/about"

    @classmethod
    def serve(cls):
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
        jp.Div(a=div, text="This is the about page!",
               classes="text-4xl m-2 text-center")
        jp.Div(a=div, text="""
        Cristoforo Colombo nasce vicino a Genova nel 1451 e già da giovane comincia ad appassionarsi al mare e alla navigazione. All'età di 14 anni diventa marinaio e inizia a viaggiare in numerosi Paesi europei. Cristoforo Colombo, appassionato di geografia ed astronomia, sostiene fermamente che la Terra è rotonda. Per dimostrarlo a tutti, alla fine del XV secolo decide di viaggiare verso l'India navigando in direzione ovest. La spedizione è molto costosa e Cristoforo Colombo decide di chiedere un aiuto economico ai sovrani del Portogallo. Il re del Portogallo gli nega l'appoggio economico, quindi si rivolge alla regina Isabella di Castiglia.

Ottenuti soldi e navi, salpa da Palos de la Frontera il 3 agosto del 1492 e, dopo mesi di navigazione, tocca terra il 12 ottobre. Tuttavia, non si tratta dell'India ma di un nuovo continente: l'America, che viene denominata Nuovo Mondo. Da quel momento prende inizio la grande colonizzazione spagnola del continente americano.

Lo stesso Cristoforo Colombo organizza altri tre viaggi verso l'America, ma continui problemi e le grosse difficoltà 
nel trovare l'oro lo rendono poco amato dai re di Spagna. Muore a Valladolid nel 1506, povero e dimenticato da tutti. 
""", classes="text m-2")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if not widget.drawer.value:
            widget.drawer.value = True
        else:
            widget.drawer.value = False
