import json
import datetime
import app as manage
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import StringProperty, ObjectProperty
from kivymd.app import StringProperty as sp
from kivy.config import Config
from genereted import (Add_buy, Add_facture, Add_invent, Add_product, Add_provider, Add_report, Edit_product, Edit_provider, Edit_buy, Edit_facture, Edit_invent, Edit_report,View_invent, View_buy, View_report, View_provider, View_facture, View_product, List_buy, List_facture, List_invent, List_product, List_provider, List_report)
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.list import OneLineIconListItem,ThreeLineAvatarIconListItem,TwoLineAvatarIconListItem, IconRightWidget,IconLeftWidget,TwoLineIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '760')
Config.write()
#pos_hint: { "center_x" : 0.5,"top":1}centro
#pos_hint: { "center_x" : 0.5,"center_y": 0.5}merocentro
def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")
            

class Guardar_invent(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_invent_screen"
        campo = self.parent.parent.parent.ids
        if campo.nombre.text !="":
            print()
            fecha=get_date()
            consulta = "SELECT productoid from produtos where nombre = "+campo.nombre.text+";"
            productoid = manage.obtener_registro("./base.db", consulta)
            consulta = "INSERT INTO  inventario(productoid,exitencia, toempresa, fecha_ultima_actual, activo) values("+productoid+","+campo.existencia.text+",'"+app.nombre+"','"+fecha+"')"
            manage.agregar_registro("./base.db",consulta)        
        app.root.remove_widget(self.parent.parent.parent)


class Guardar_buy(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_buy_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        fecha = get_date()
        manage.agregar_registro("./base.db","INSERT INTO buys(Nombre, correo, numero, direccion, nit,comentarios, toempresa, fecha_creacion, imagen, activo)VALUES('"+campo.nombre.text+"', '"+campo.mail.text+"', '"+campo.telefono.text+"', '"+campo.address.text+"', '"+campo.nit.text+"', '"+campo.comentario.text+"', '"+app.nombre+"', '"+fecha+"', NULL, 1)")        
        app.root.remove_widget(self.parent.parent.parent)


class Guardar_provider(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_provider_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        manage.agregar_registro("./base.db","INSERT INTO proveedores(Nombre, correo, numero, direccion, sitio_web,toempresa, empresa, activo)VALUES('"+campo.nombre.text+"', '"+campo.mail.text+"', '"+campo.telefono.text+"', '"+campo.address.text+"', '"+campo.web.text+"', '"+app.name+"', '"+campo.empresa.text+"', 1)")        
        app.root.remove_widget(self.parent.parent.parent)


class Guardar_product(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_product_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        manage.agregar_registro("./base.db","INSERT INTO products(Nombre, correo, numero, direccion, nit,comentarios, toempresa, fecha_creacion, imagen, activo)VALUES('"+campo.nombre.text+"', '"+campo.mail.text+"', '"+campo.telefono.text+"', '"+campo.address.text+"', '"+campo.nit.text+"', '"+campo.comentario.text+"', '"+app.nombre+"', '"+fecha+"', NULL, 1)")        
        app.root.remove_widget(self.parent.parent.parent)


class Guardar_facture(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_facture_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        manage.agregar_registro("./base.db","INSERT INTO factures(Nombre, correo, numero, direccion, nit,comentarios, toempresa, fecha_creacion, imagen, activo)VALUES('"+campo.nombre.text+"', '"+campo.mail.text+"', '"+campo.telefono.text+"', '"+campo.address.text+"', '"+campo.nit.text+"', '"+campo.comentario.text+"', '"+app.nombre+"', '"+fecha+"', NULL, 1)")        
        app.root.remove_widget(self.parent.parent.parent)


class Guardar_report(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_report_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        manage.agregar_registro("./base.db","INSERT INTO reports(Nombre, correo, numero, direccion, nit,comentarios, toempresa, fecha_creacion, imagen, activo)VALUES('"+campo.nombre.text+"', '"+campo.mail.text+"', '"+campo.telefono.text+"', '"+campo.address.text+"', '"+campo.nit.text+"', '"+campo.comentario.text+"', '"+app.nombre+"', '"+fecha+"', NULL, 1)")        
        app.root.remove_widget(self.parent.parent.parent)

class Guardar_cliente(MDRaisedButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_client_screen"
        campo = self.parent.parent.parent.ids
        if campo.nombre.text !="":
            print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
            fecha = datetime.datetime.now().strftime("%Y-%m-%d")
            manage.agregar_registro("./base.db","INSERT INTO Clientes(Nombre, correo, numero, direccion, nit,comentarios, toempresa, fecha_creacion, imagen, activo)VALUES('"+campo.nombre.text+"', '"+campo.mail.text+"', '"+campo.telefono.text+"', '"+campo.address.text+"', '"+campo.nit.text+"', '"+campo.comentario.text+"', '"+app.nombre+"', '"+fecha+"', NULL, 1)")        
        app.root.remove_widget(self.parent.parent.parent)
class Modificar_cliente(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_client_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_cliente("./base.db",campo.search.text, app.nombre, nuevos_datos)
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
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        cliente_id = self.ids.search.text
        if cliente_id is not None:
            client = manage.obtener_cliente("./base.db", cliente_id, app.nombre)
            if client is not None:
                self.ids.nombre.text = client[1]
                self.ids.mail.text = client[2]
                self.ids.telefono.text = client[3]
                self.ids.address.text = client[4]
                self.ids.nit.text = client[5]
                self.ids.comentario.text = client[6]
            else:
                # Si no se encontró el cliente, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_client(MDScreen):
    def eliminar_cliente(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        cliente_id = int(item.secondary_text.split("|")[0])
        manage.eliminar_cliente("./base.db", cliente_id)
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
        print(app.nombre, app.tipo)
        rows = manage.consulta_general("./base.db","SELECT * FROM clientes where toempresa = '"+app.nombre+"' and activo = 1")
        for row in rows:
            self.ids.lista.add_widget(
                ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_cliente(instance)
                    ),
                    radius=[20, 20, 20, 0],
                    bg_color=(0, 0.6, 0.4, 1),
                    text=row[1]+" | "+row[3],
                    secondary_text=row[0].__str__()+" | "+row[6],
                    tertiary_text=row[2],
                    
                    )
                )
            

class View_client(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            client = manage.obtener_cliente("./base.db", myid, app.nombre)
            if client is not None:
                id_ = str(client[0])
                self.ids.cliente_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+client[1]
                self.ids.mail.text ="Correo Electronico:  "+ client[2]
                self.ids.telefono.text = "Telefono:  "+client[3]
                self.ids.address.text = "Direccion:  "+client[4]
                self.ids.nit.text = "NIT:  "+client[5]
                self.ids.comentario.text ="Estado:  "+ client[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(client[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.cliente_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"
class Regresar_invent(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_invent_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Regresar_product(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_product_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Regresar_facture(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_facture_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Regresar_buy(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_buy_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Regresar_provider(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_provider_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Regresar_client(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_client_screen"
        app.root.remove_widget(self.parent.parent.parent)
class Regresar_report(MDIconButton):
    def regresar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_report_screen"
        app.root.remove_widget(self.parent.parent.parent)


class Modificar_invent(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_invent_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_invent("./base.db",campo.search.text, app.nombre, nuevos_datos)
        app.root.remove_widget(self.parent.parent.parent)
class Modificar_buy(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_buy_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_buy("./base.db",campo.search.text, app.nombre, nuevos_datos)
        app.root.remove_widget(self.parent.parent.parent)
class Modificar_provider(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_provider_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_provider("./base.db",campo.search.text, app.nombre, nuevos_datos)
        app.root.remove_widget(self.parent.parent.parent)
class Modificar_product(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_product_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_product("./base.db",campo.search.text, app.nombre, nuevos_datos)
        app.root.remove_widget(self.parent.parent.parent)
class Modificar_facture(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_facture_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_facture("./base.db",campo.search.text, app.nombre, nuevos_datos)
        app.root.remove_widget(self.parent.parent.parent)
class Modificar_report(MDRaisedButton):
    def alterar(self):
        app = MDApp.get_running_app()
        app.root.current = "manage_report_screen"
        campo = self.parent.parent.parent.ids
        print(campo.nombre.text, campo.telefono.text, campo.nit.text, campo.address.text, campo.comentario.text)
        nuevos_datos = {
        'nombre': campo.nombre.text,
        'correo': campo.mail.text,
        'numero': campo.telefono.text,
        'direccion': campo.address.text,
        'nit': campo.nit.text,
        'comentarios': campo.comentario.text,
        }
        manage.modificar_report("./base.db",campo.search.text, app.nombre, nuevos_datos)
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
class Card_invent_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nuevo inventario para: ", app.nombre)
        app.root.add_widget(
            Add_invent(
            )
        )
        app.root.current = "add_invent"

class Card_invent_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nuevo inventario para: ", app.nombre)
        app.root.add_widget(
            Edit_invent(
            )
        )
        app.root.current = "edit_invent"

class Card_invent_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_invent(
            )
        )
        app.root.current = "list_invent"

class Card_invent_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_invent(
            )
        )
        app.root.current = "view_invent"

class Card_buy_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nueva compra para: ", app.nombre)
        app.root.add_widget(
            Add_buy(
            )
        )
        app.root.current = "add_buy"
class Card_facture_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nueva compra para: ", app.nombre)
        app.root.add_widget(
            Add_facture(
            )
        )
        app.root.current = "add_buy"
class Card_report_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nueva compra para: ", app.nombre)
        app.root.add_widget(
            Add_report(
            )
        )
        app.root.current = "add_buy"

class Card_buy_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nueva compra para: ", app.nombre)
        app.root.add_widget(
            Edit_buy(
            )
        )
        app.root.current = "edit_buy"
class Card_facture_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nueva compra para: ", app.nombre)
        app.root.add_widget(
            Edit_facture(
            )
        )
        app.root.current = "edit_facture"
class Card_report_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nueva compra para: ", app.nombre)
        app.root.add_widget(
            Edit_report(
            )
        )
        app.root.current = "edit_report"

class Card_buy_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_buy(
            )
        )
        app.root.current = "list_buy"

class Card_buy_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_buy(
            )
        )
        app.root.current = "view_buy"

class Card_product_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_product(
            )
        )
        app.root.current = "view_product"
class Card_facture_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_facture(
            )
        )
        app.root.current = "view_facture"
class Card_report_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_report(
            )
        )
        app.root.current = "view_report"
class Card_provider_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nuevo proveedor para: ", app.nombre)
        app.root.add_widget(
            Add_provider(
            )
        )
        app.root.current = "add_provider"

class Card_provider_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nuevo proveedor para: ", app.nombre)
        app.root.add_widget(
            Edit_provider(
            )
        )
        app.root.current = "edit_provider"

class Card_provider_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_provider(
            )
        )
        app.root.current = "list_provider"

class Card_facture_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_facture(
            )
        )
        app.root.current = "list_facture"
class Card_provider_view(MDCard):
    def view(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            View_provider(
            )
        )
        app.root.current = "view_provider"

class Card_product_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_product(
            )
        )
        app.root.current = "list_product"

class Card_report_list(MDCard):
    def list(self):
        app = MDApp.get_running_app()
        app.root.add_widget(
            List_report(
            )
        )
        app.root.current = "list_report"
class Card_product_add(MDCard):
    def add(self):
        app = MDApp.get_running_app()
        print("nuevo producto para: ", app.nombre)
        app.root.add_widget(
            Add_product(
            )
        )
        app.root.current = "add_product"
class Card_product_edit(MDCard):
    def edit(self):
        app = MDApp.get_running_app()
        print("nuevo producto para: ", app.nombre)
        app.root.add_widget(
            Edit_product(
            )
        )
        app.root.current = "edit_provider"
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
        manage.eliminar_empresa("./base",item.text)
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