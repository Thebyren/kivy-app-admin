import sqlite3
def eliminar_cliente(db,id):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        consulta = (f"UPDATE clientes SET activo = 0 WHERE clienteid = '{id}';")
        cursor.execute(consulta)
        con.commit()
        con.close()
    except:
        print("error en borrar la empresa")
def obtener_cliente(db, id, empresa):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        consulta = "SELECT * FROM clientes WHERE activo = 1 AND clienteid = ? AND toempresa = ?;"
        cursor.execute(consulta, (id, empresa))
        cliente = cursor.fetchone()
        con.close()
        
        if cliente is not None:
            return cliente
        else:
            print("No se encontraron resultados para el cliente con nombre:", empresa)
            return None  # o puedes devolver un valor predeterminado, según tus necesidades
    except Exception as e:
        print("Error en obtener_cliente:", str(e))
        return None

        

def eliminar_empresa(db,empresa):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        consultas = []
        for tabla in ["clientes", "compras", "facturas", "inventario", "precios", "productos", "proveedores", "ventas", "empleados"]:
            consultas.append(f"UPDATE {tabla} SET activo = 0 WHERE toempresa = '{empresa}'")
            consultas.append(";")
        cursor.execute(consultas)
        con.commit()
        con.close()
    except:
        print("error en borrar la empresa")
def consulta_general(db,consulta):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute(consulta)
        return cursor.fetchall()
        
    except:
        return "no hay nada"
def agregar_registro(db, consulta):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute(consulta)
        con.commit()
        con.close()
    except:
        print("error en el insert")


def modificar_(db, id, empresa, nuevos_datos):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        campos_a_actualizar = ', '.join([f"{campo} = ?" for campo in nuevos_datos.keys()])
        valores_a_actualizar = tuple(nuevos_datos.values())
        
        consulta = f"UPDATE clientes SET {campos_a_actualizar} WHERE clienteid = ? AND toempresa = ?;"
        valores_a_actualizar += (id, empresa)
        
        cursor.execute(consulta, valores_a_actualizar)
        con.commit()
        con.close()
        
        print("Cliente modificado con éxito")
    except Exception as e:
        print("Error en modificar_cliente:", str(e))
def modificar_cliente(db, id, empresa, nuevos_datos):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        campos_a_actualizar = ', '.join([f"{campo} = ?" for campo in nuevos_datos.keys()])
        valores_a_actualizar = tuple(nuevos_datos.values())
        
        consulta = f"UPDATE clientes SET {campos_a_actualizar} WHERE clienteid = ? AND toempresa = ?;"
        valores_a_actualizar += (id, empresa)
        
        cursor.execute(consulta, valores_a_actualizar)
        con.commit()
        con.close()
        
        print("Cliente modificado con éxito")
    except Exception as e:
        print("Error en modificar_cliente:", str(e))

def obtener_registro(db,consulta ):
    try:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute(consulta)
        con.close()
        return cursor.fetchone()
        
    except:
        return 0
    
