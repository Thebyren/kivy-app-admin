import json
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import StringProperty, ObjectProperty
from kivymd.app import StringProperty as sp
from kivy.config import Config
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.list import OneLineIconListItem,TwoLineAvatarIconListItem, IconRightWidget,IconLeftWidget,TwoLineIconListItem, IRightBodyTouch
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '760')
Config.write()
class Guardar_cliente(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_client_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Add_client(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class Edit_client(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class List_client(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class View_client(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo

class Regresar_client(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_client_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Card_client_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nuevo cliente para: ", app.nombre)
        app.root.add_widget(
            Add_client(
            )
        )
        app.root.current ="add_client"
class Card_client_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nuevo cliente para: ", app.nombre)
        app.root.add_widget(
            Edit_client(
            )
        )
        app.root.current ="edit_client"
class Card_client_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_client(
            )
        )
        app.root.current ="list_client"
class Card_client_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_client(
            )
        )
        app.root.current ="view_client"

class manage_client_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class manage_invent_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class manage_buy_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class manage_provider_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class manage_product_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class manage_facture_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
class manage_report_screen(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo

class Card_type(MDCard):
    tipo = sp()
    img = sp()
    def manage_client(self):
        app = MDApp.get_running_app()
        print("manejo de clientes",app.nombre, app.tipo)
        app.root.add_widget(
            manage_client_screen(
                
            )
        )
        app.root.current ="manage_client_screen"
    def manage_invent(self):
        app = MDApp.get_running_app()
        print("manejo de inventario",app.nombre, app.tipo)
        app.root.add_widget(
            manage_invent_screen(
                
            )
        )
        app.root.current ="manage_invent_screen"
    def manage_buy(self):
        app = MDApp.get_running_app()
        print("manejo de compras",app.nombre, app.tipo)
        app.root.add_widget(
            manage_buy_screen(
                
            )
        )
        app.root.current ="manage_buy_screen"
    def manage_provider(self):
        app = MDApp.get_running_app()
        print("manejo de proveedores",app.nombre, app.tipo)
        app.root.add_widget(
            manage_provider_screen(
                
            )
        )
        app.root.current ="manage_provider_screen"
    def manage_product(self):
        app = MDApp.get_running_app()
        print("manejo de productos",app.nombre, app.tipo)
        app.root.add_widget(
            manage_product_screen(
                
            )
        )
        app.root.current ="manage_product_screen"
    def manage_facture(self):
        app = MDApp.get_running_app()
        print("manejo de facturas",app.nombre, app.tipo)
        app.root.add_widget(
            manage_facture_screen(
                
            )
        )
        app.root.current ="manage_facture_screen"
    def manage_report(self):
        app = MDApp.get_running_app()
        print("manejo de reportes",app.nombre, app.tipo)
        app.root.add_widget(
            manage_report_screen(
                
            )
        )
        app.root.current ="manage_report_screen"

class Main(MDApp):
    nombre=""
    tipo=""
    def build(self):
        Builder.load_file("layout.kv")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Purple"
        return main_screen_manager(transition=FadeTransition())
class Tipos_menu(MDScreenManager):
    pass
class Menu_empresa(MDScreen):
    nombre = StringProperty("")
    descripcion = StringProperty("")
    def __init__(self, nombre, descripcion, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.descripcion = descripcion
    
    def change(self):
        print("depurador xd")
        app = MDApp.get_running_app()
        app.root.current = "main_screen"
        app.root.remove_widget(self)
        print(app.root.current)

class DialogContent(MDBoxLayout):
    pass
class Regresar_menu_empresa(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "menu_empresa"
        app.root.remove_widget(self.parent.parent.parent)
class DashBoard(MDScreen):
    empresas=[{}]
    def __init__(self, **kwargs):
        super(DashBoard, self).__init__(**kwargs)
        self.empresas=[]
    def on_enter(self):
        #
        # self.cargar_empresas()
        pass
    def presionado(self):
        self.cargar_empresas()
    def guardar_empresas(self):
        with open("empresas.json", "w") as json_file:
            json.dump(self.empresas, json_file)
            json_file.close()

    def cargar_empresas(self):
        try:
            with open("empresas.json", "r") as json_file:
                self.empresas = json.load(json_file)
                for empresa in self.empresas:
                    nombre = empresa.get("nombre", "")
                    tipo = empresa.get("tipo", "")
                    print(nombre, tipo)
                    tipo_empresa = tipo.lower()
                    icono = "google-my-business"
                    iconos_por_tipo = {
                        "farmacia": "pill",
                        "super": "shopping",
                        "ferreteria": "hammer",
                        "libreria": "book",
                        "almacen": "store",
                        "agencia": "briefcase",
                        "restaurante": "silverware",
                        "software":"application-brackets",
                        "frutas":"food-apple",
                        "nube":"cloud",
                        "publicidad":"human-male-board-poll",
                        "universidad":"book-education",
                        "cerveceria":"beer",
                        "embotelladora":"bottle-soda",
                        "gasolinera":"gas-station"

                    }
                    for palabra_clave in reversed(iconos_por_tipo.keys()):
                        if palabra_clave in tipo_empresa:
                            icono = iconos_por_tipo[palabra_clave]
                            break
                    self.ids.lista_empresa.add_widget(
                    TwoLineAvatarIconListItem(
                        IconLeftWidget(
                            icon=icono
                        ),
                        IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_empresa(instance)
                        ),  
                        radius=[25, 0, 25, 0],
                        bg_color=(0, 0.6, 0.4, 1),
                        id="texto",
                        secondary_text=tipo,
                        text=nombre,
                        on_release=lambda instance: self.imprimir(instance),
                    ),
                )
        except FileNotFoundError:
            self.empresas = []

    def nueva_empresa(self, nombre_empresa, tipo_empresa):
        icono = "google-my-business"
        tipo_empresa = tipo_empresa.lower()
        iconos_por_tipo = {
            "farmacia": "pill",
            "super": "shopping",
            "ferreteria": "hammer",
            "libreria": "book",
            "almacen": "store",
            "agencia": "briefcase",
            "restaurante": "silverware",
            "software":"application-brackets",
            "frutas":"food-apple",
            "nube":"cloud",
            "publicidad":"human-male-board-poll",
            "universidad":"book-education",
            "cerveceria":"beer",
            "embotelladora":"bottle-soda",
            "gasolinera":"gas-station"

        }
        for palabra_clave in reversed(iconos_por_tipo.keys()):
            if palabra_clave in tipo_empresa:
                icono = iconos_por_tipo[palabra_clave]
                break
        empresa = {"nombre": nombre_empresa, "tipo": tipo_empresa}
        self.empresas.append(empresa)
        self.guardar_empresas()
        print(nombre_empresa, tipo_empresa)
        self.ids.lista_empresa.add_widget(
            TwoLineAvatarIconListItem(
                IconLeftWidget(
                    icon=icono
                ),
                IconRightWidget(
                    icon="delete",
                    on_release=lambda instance: self.eliminar_empresa(instance)
                ),
                radius=[25, 0, 25, 0],
                bg_color=(0, 0.6, 0.4, 1),
                id="texto",
                secondary_text=tipo_empresa,
                text=nombre_empresa,
                on_release=lambda instance: self.imprimir(instance),
            ),
        )
    def eliminar_empresa(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista_empresa.remove_widget(item)
        empresa_a_eliminar = next(
            e for e in self.empresas if e["nombre"] == item.text and e["tipo"] == item.secondary_text
        )
        self.empresas.pop(self.empresas.index(empresa_a_eliminar))
        self.guardar_empresas()
 
    def imprimir(self, instance):
        Main.nombre=instance.text
        Main.tipo = instance.secondary_text
        app = MDApp.get_running_app()
        print(app.root.ids)
        # app.root.clear_widgets()
        app.root.add_widget(Menu_empresa(instance.text, instance.secondary_text))
        app.root.current = "menu_empresa"
        print(app.root.current)

    def show_dialog(self):
        self.dialog = MDDialog(
            title="Datos de la nueva empresa",
            type="custom",
            content_cls=DialogContent(),
            buttons=[
                MDRaisedButton(
                    text="Cancelar",
                    on_release=self.cerrar,
                ),
                MDRaisedButton(
                    text="OK",
                    on_release=self.obtener_texto,
                ),
            ],
        )
        self.dialog.open()

    def cerrar(self, *args):
        self.dialog.dismiss()

    def obtener_texto(self, *args):
        nombre_empresa = self.dialog.content_cls.ids.nombre_empresa.text
        tipo_empresa = self.dialog.content_cls.ids.tipo_empresa.text
        print("Nombre de la empresa:", nombre_empresa)
        print("Tipo de empresa:", tipo_empresa)
        DashBoard.nueva_empresa(self, nombre_empresa, tipo_empresa)
        self.dialog.dismiss()


class IntegranteInfo(TwoLineIconListItem):
    name = StringProperty()
    carnet = StringProperty()
    img = StringProperty()

class ItemListMenu(OneLineIconListItem):
    name = StringProperty()
    id = StringProperty()
    icon = StringProperty()

class InfoScreen(MDBoxLayout):
    texto= StringProperty()
class TemplateScreen(MDScreen):
    texto= StringProperty()
class CardType(MDCard):
    img = StringProperty()
    title = StringProperty()

class main_screen_manager(ScreenManager):
    pass
class cuestionario_empresa():
    pass
class MsgNewCard():
    pass



Main().run()