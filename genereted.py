from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconRightWidget,IconLeftWidget

import app as manage
class Add_invent(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    
class Edit_invent(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        invent_id = self.ids.search.text
        if invent_id is not None:
            invent = manage.obtener_invent("./base.db", invent_id, app.nombre)
            if invent is not None:
                self.ids.nombre.text = invent[1]
                self.ids.mail.text = invent[2]
                self.ids.telefono.text = invent[3]
                self.ids.address.text = invent[4]
                self.ids.nit.text = invent[5]
                self.ids.comentario.text = invent[6]
            else:
                # Si no se encontró el invent, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_invent(MDScreen):
    def eliminar_invent(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        invent_id = int(item.text.split(":")[0])
        print(invent_id)
        manage.eliminar_invent("./base.db", invent_id)
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
        print(app.nombre, app.tipo)
        consulta = """ SELECT DISTINCT
        i.productoid,
        i.existencia,
        i.fecha_ultima_actualizacion,
        p.nombre,
        p.Categoría
    FROM inventario AS i
    INNER JOIN productos AS p ON i.productoid = p.productoid
    WHERE i.activo = 1
      AND p.activo = 1"""
        
        rows = manage.consulta_general("./base.db",consulta)
        print(rows)
        print(len(rows)) 
        for row in rows:
            self.ids.lista.add_widget(
                ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_invent(instance)
                    ),
                    radius=[20, 20, 20, 0],
                    bg_color=(0, 0.6, 0.4, 1),
                    text="ID:"+str(row[0])+"  Nombre:"+str(row[3]),
                    secondary_text="Categoria"+str(row[4])+"  existencia:"+str(row[1]),
                    tertiary_text="Actualizacio en:"+str(row[2]),          
                    )
                )
            

class View_invent(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            invent = manage.obtener_invent("./base.db", myid, app.nombre)
            if invent is not None:
                id_ = str(invent[0])
                self.ids.invent_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+invent[1]
                self.ids.mail.text ="Correo Electronico:  "+ invent[2]
                self.ids.telefono.text = "Telefono:  "+invent[3]
                self.ids.address.text = "Direccion:  "+invent[4]
                self.ids.nit.text = "NIT:  "+invent[5]
                self.ids.comentario.text ="Estado:  "+ invent[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(invent[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.invent_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"



class Add_buy(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    
class Edit_buy(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        buy_id = self.ids.search.text
        if buy_id is not None:
            buy = manage.obtener_buy("./base.db", buy_id, app.nombre)
            if buy is not None:
                self.ids.nombre.text = buy[1]
                self.ids.mail.text = buy[2]
                self.ids.telefono.text = buy[3]
                self.ids.address.text = buy[4]
                self.ids.nit.text = buy[5]
                self.ids.comentario.text = buy[6]
            else:
                # Si no se encontró el buy, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_buy(MDScreen):
    def eliminar_buy(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        buy_id = int(item.secondary_text.split("|")[0])
        manage.eliminar_buy("./base.db", buy_id)
    


    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
        print(app.nombre, app.tipo)
        rows = manage.consulta_general("./base.db","SELECT * FROM compras where toempresa = '"+app.nombre+"' and activo = 1")
        for row in rows:
            self.ids.lista.add_widget(
                ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_buy(instance)
                    ),
                    radius=[20, 20, 20, 0],
                    bg_color=(0, 0.6, 0.4, 1),
                    text=row[1]+" | "+row[3],
                    secondary_text=row[0].__str__()+" | "+row[6],
                    tertiary_text=row[2],
                    
                    )
                )
            

class View_buy(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            buy = manage.obtener_buy("./base.db", myid, app.nombre)
            if buy is not None:
                id_ = str(buy[0])
                self.ids.buy_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+buy[1]
                self.ids.mail.text ="Correo Electronico:  "+ buy[2]
                self.ids.telefono.text = "Telefono:  "+buy[3]
                self.ids.address.text = "Direccion:  "+buy[4]
                self.ids.nit.text = "NIT:  "+buy[5]
                self.ids.comentario.text ="Estado:  "+ buy[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(buy[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.buy_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"



class Add_provider(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    
class Edit_provider(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        provider_id = self.ids.search.text
        if provider_id is not None:
            provider = manage.obtener_provider("./base.db", provider_id, app.nombre)
            if provider is not None:
                self.ids.nombre.text = provider[1]
                self.ids.mail.text = provider[2]
                self.ids.telefono.text = provider[3]
                self.ids.address.text = provider[4]
                self.ids.nit.text = provider[5]
                self.ids.comentario.text = provider[6]
            else:
                # Si no se encontró el provider, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_provider(MDScreen):
    def eliminar_provider(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        provider_id = int(item.secondary_text.split("|")[0])
        manage.eliminar_provider("./base.db", provider_id)
    


    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
        print(app.nombre, app.tipo)
        rows = manage.consulta_general("./base.db","SELECT * FROM proveedores where toempresa = '"+app.nombre+"' and activo = 1")
        for row in rows:
            self.ids.lista.add_widget(
                ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_provider(instance)
                    ),
                    radius=[20, 20, 20, 0],
                    bg_color=(0, 0.6, 0.4, 1),
                    text=row[1]+" | "+row[3],
                    secondary_text=row[0].__str__()+" | "+row[6],
                    tertiary_text=row[2],
                    
                    )
                )
            

class View_provider(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            provider = manage.obtener_provider("./base.db", myid, app.nombre)
            if provider is not None:
                id_ = str(provider[0])
                self.ids.provider_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+provider[1]
                self.ids.mail.text ="Correo Electronico:  "+ provider[2]
                self.ids.telefono.text = "Telefono:  "+provider[3]
                self.ids.address.text = "Direccion:  "+provider[4]
                self.ids.nit.text = "NIT:  "+provider[5]
                self.ids.comentario.text ="Estado:  "+ provider[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(provider[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.provider_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"



class Add_product(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    
class Edit_product(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        product_id = self.ids.search.text
        if product_id is not None:
            product = manage.obtener_product("./base.db", product_id, app.nombre)
            if product is not None:
                self.ids.nombre.text = product[1]
                self.ids.mail.text = product[2]
                self.ids.telefono.text = product[3]
                self.ids.address.text = product[4]
                self.ids.nit.text = product[5]
                self.ids.comentario.text = product[6]
            else:
                # Si no se encontró el product, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_product(MDScreen):
    def eliminar_product(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        product_id = int(item.secondary_text.split("|")[0])
        manage.eliminar_product("./base.db", product_id)
    


    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
        print(app.nombre, app.tipo)
        rows = manage.consulta_general("./base.db","SELECT * FROM productos where toempresa = '"+app.nombre+"' and activo = 1")
        for row in rows:
            self.ids.lista.add_widget(
                ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_product(instance)
                    ),
                    radius=[20, 20, 20, 0],
                    bg_color=(0, 0.6, 0.4, 1),
                    text=row[1]+" | "+row[3],
                    secondary_text=row[0].__str__()+" | "+row[6],
                    tertiary_text=row[2],
                    
                    )
                )
            

class View_product(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            product = manage.obtener_product("./base.db", myid, app.nombre)
            if product is not None:
                id_ = str(product[0])
                self.ids.product_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+product[1]
                self.ids.mail.text ="Correo Electronico:  "+ product[2]
                self.ids.telefono.text = "Telefono:  "+product[3]
                self.ids.address.text = "Direccion:  "+product[4]
                self.ids.nit.text = "NIT:  "+product[5]
                self.ids.comentario.text ="Estado:  "+ product[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(product[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.product_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"



class Add_facture(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    
class Edit_facture(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        facture_id = self.ids.search.text
        if facture_id is not None:
            facture = manage.obtener_facture("./base.db", facture_id, app.nombre)
            if facture is not None:
                self.ids.nombre.text = facture[1]
                self.ids.mail.text = facture[2]
                self.ids.telefono.text = facture[3]
                self.ids.address.text = facture[4]
                self.ids.nit.text = facture[5]
                self.ids.comentario.text = facture[6]
            else:
                # Si no se encontró el facture, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_facture(MDScreen):
    def eliminar_facture(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        facture_id = int(item.secondary_text.split("|")[0])
        manage.eliminar_facture("./base.db", facture_id)
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
        print(app.nombre, app.tipo)
        rows = manage.consulta_general("./base.db","SELECT * FROM facturas where toempresa = '"+app.nombre+"' and activo = 1")
        for row in rows:
            self.ids.lista.add_widget(
                ThreeLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="account"
                    ),
                    IconRightWidget(
                        icon="delete",
                        on_release=lambda instance: self.eliminar_facture(instance)
                    ),
                    radius=[20, 20, 20, 0],
                    bg_color=(0, 0.6, 0.4, 1),
                    text=row[1]+" | "+row[3],
                    secondary_text=row[0].__str__()+" | "+row[6],
                    tertiary_text=row[2],
                    
                    )
                )
            

class View_facture(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            facture = manage.obtener_facture("./base.db", myid, app.nombre)
            if facture is not None:
                id_ = str(facture[0])
                self.ids.facture_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+facture[1]
                self.ids.mail.text ="Correo Electronico:  "+ facture[2]
                self.ids.telefono.text = "Telefono:  "+facture[3]
                self.ids.address.text = "Direccion:  "+facture[4]
                self.ids.nit.text = "NIT:  "+facture[5]
                self.ids.comentario.text ="Estado:  "+ facture[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(facture[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.facture_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"



class Add_report(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    
class Edit_report(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        report_id = self.ids.search.text
        if report_id is not None:
            report = manage.obtener_report("./base.db", report_id, app.nombre)
            if report is not None:
                self.ids.nombre.text = report[1]
                self.ids.mail.text = report[2]
                self.ids.telefono.text = report[3]
                self.ids.address.text = report[4]
                self.ids.nit.text = report[5]
                self.ids.comentario.text = report[6]
            else:
                # Si no se encontró el report, asigna "No se encontró" a todos los campos
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"

        
class List_report(MDScreen):
    def eliminar_report(self, instance):
        print("borrando ")
        item = instance.parent.parent
        self.ids.lista.remove_widget(item)
        report_id = int(item.secondary_text.split("|")[0])
        manage.eliminar_report("./base.db", report_id)
    
class View_report(MDScreen):
    def on_enter(self):
        app = MDApp.get_running_app()
        self.ids.label1.text = app.nombre
        self.ids.label2.text = app.tipo
    def buscar(self):
        app = MDApp.get_running_app()
        app.nombre
        myid = self.ids.myid.text
        if myid is not None:
            report = manage.obtener_report("./base.db", myid, app.nombre)
            if report is not None:
                id_ = str(report[0])
                self.ids.report_id_.text="Id:  "+ id_
                self.ids.nombre.text = "Nombre:  "+report[1]
                self.ids.mail.text ="Correo Electronico:  "+ report[2]
                self.ids.telefono.text = "Telefono:  "+report[3]
                self.ids.address.text = "Direccion:  "+report[4]
                self.ids.nit.text = "NIT:  "+report[5]
                self.ids.comentario.text ="Estado:  "+ report[6]
                self.ids.fecha_creacion.text ="fecha ingreso:  "+ str(report[8])
                self.ids.myid.text = ""
            else:
                self.ids.myid.text =""
                self.ids.report_id_.text = "no se encontró"
                self.ids.nombre.text = "No se encontró"
                self.ids.mail.text = "No se encontró"
                self.ids.telefono.text = "No se encontró"
                self.ids.address.text = "No se encontró"
                self.ids.nit.text = "No se encontró"
                self.ids.comentario.text = "No se encontró"
                self.ids.fecha_creacion.text= "no se encontró"
