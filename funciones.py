from conexion import *

import sqlite3
import re
import os
import sys


conn = sqlite3.connect('base.sqlite')

cursor = conn.cursor()
from time import sleep
from rich.console import Console
from rich.table import Table
console = Console()

#tabla de listado rich lybrary listado clientes


# table.add_row(
#     "May 25, 2018",
#     "[red]Solo[/red]: A Star Wars Story",
#     "$275,000,000",
#     "$393,151,347",
# )
# table.add_row(
#     "Dec 15, 2017",
#     "Star Wars Ep. VIII: The Last Jedi",
#     "$262,000,000",
#     "[bold]$1,332,539,889[/bold]",
# )

def borrar_pantalla():
  
    os.system('cls')
    sys.stdout.flush()

def limpiarString(ejemploString):
    for char in ejemploString:
        if char in "(')":
            ejemploString.replace(char,'')
    return ejemploString
    



def funcionMenu( diccionario ):
    print("""Seleccione una de las siguientes opciones: """)
    for k , v in diccionario.items():
        print('[',k,']',v )
    opcion= input("Ingrese número de la opción deseada  ")

        
        

   


    res = opcion if opcion.capitalize() in diccionario.keys() else "la opción ingresada es inexistente"

    return res.capitalize()
    
    
def listarClientes():
    
   
    table = generarTabla()
    cursor.execute('SELECT * from clientes')
    conn.commit()
    todosLosClientes = cursor.fetchall()
    
    for item in todosLosClientes:
        tupla_a_lista = list(item)
        id = str(tupla_a_lista[0])
        nombre = str(tupla_a_lista[1])
        apellido = str(tupla_a_lista[2])
        dni = str(tupla_a_lista[3])
        telefono = str(tupla_a_lista[4])
        direccion = str(tupla_a_lista[5])
 
        
        table.add_row(
        id,
        nombre,
        apellido,
        dni,
        telefono,
        direccion)
    console.print(table)    
    sleep(2) 
    
      
    
def insertarClientes():
    
    try: 
            sql = """INSERT INTO CLIENTES (nombre, apellido , dni , telefono , direccion) VALUES (?, ?, ?, ?, ?)""" 
            nombre = input('Ingresar nombre ')
            apellido = input('Ingresar apellido ')
            dni = input('Ingresar dni ')
            telefono = input('Ingresar telefono ')
            direccion = input('Ingresar direccion ')
            val = (nombre, apellido , dni , telefono , direccion)
        
            cursor.execute(sql, val)
            conn.commit()
            listarClientes()
            print("""
                        ####################################
                        
                        El usuario fue insertado correctamente
                        
                        ####################################
                    
                        """)
       
           
    
    except sqlite3.Error as error:
        print("Falló al insertar cliente en la base de datos", error)
        
        
def borrarCliente():
    try:
        listarClientes()
        id_usuario = input('Ingresar id del usuario que desea borrar ')
        sql = 'DELETE FROM CLIENTES WHERE id_cliente=?'
        cursor.execute(sql,(id_usuario,))
        conn.commit()
       
        
        print("""
                        ####################################
                        
                        El usuario fue borrado correctamente
                        
                        ####################################
                    
                        """)
       
    except sqlite3.Error as error:
        print("Falló al eliminar cliente en la base de datos", error)
    
    
def editarCliente():
   
    try:
        listarClientes()
        id_cliente = input('Ingresar id del usuario que desea editar ')
        #traer datos del ususario
        sqlSelect = 'SELECT * FROM CLIENTES WHERE id_cliente=?'
        cursor.execute(sqlSelect,(int(id_cliente),))
        datosOriginales =  cursor.fetchone()
        lista=[]
        
        campos = {
            'nombre':datosOriginales[1],
            'apellido':datosOriginales[2],
            'dni': datosOriginales[3],
            'telefono': datosOriginales[4],
            'direccion':datosOriginales[5]
        }
        sql = """UPDATE CLIENTES SET nombre = ? , apellido = ? , dni = ? , telefono = ? , direccion = ? WHERE id_cliente = ?"""
        
        for k,v in campos.items():
            respuesta = input("Desea modificar campo {} ( si o no ) ".format(k)  ) 
        
            if respuesta.lower() == 'si':
                respTemp= None
                # print(k)
                respTemp = input("ingresar nuevo {} ".format(k) ) 
                campos[k] = respTemp
            
        
        str = ""
        for k,v in campos.items():      
        
            # tupla = (v)
            # print(v)
            lista.append(v)
    
        # try:
            
        # except:
        lista.append(int(id_cliente))
        valores = tuple(lista)
       
        cursor.execute(sql, valores)
        conn.commit()
        listarClientes()
        
        print("""
                        ####################################
                        
                        Cliente fue editado correctamente
                        
                        ####################################
                    
                        """)
        
    
    except sqlite3.Error as error:
            print("Falló al actualizar cliente en la base de datos", error)

    
def buscarClientePorDni():
        try:
           
            listarClientes()
            dni_cliente = input('Ingresar dni del cliente que desea a buscar ')
            sqlSelect = 'SELECT * FROM CLIENTES WHERE dni = ?'
            cursor.execute(sqlSelect,(dni_cliente,))
            clientesDniResultado =  cursor.fetchall()
            conn.commit()
            if len(clientesDniResultado):
                # for item in clientesDniResultado:
        
                #     print(item)
                tablaBuscarPorDni = generarTabla()
                for item in clientesDniResultado:
                    tupla_a_lista = list(item)
                    id = str(tupla_a_lista[0])
                    nombre = str(tupla_a_lista[1])
                    apellido = str(tupla_a_lista[2])
                    dni = str(tupla_a_lista[3])
                    telefono = str(tupla_a_lista[4])
                    direccion = str(tupla_a_lista[5])
            
                    
                    tablaBuscarPorDni.add_row(
                    id,
                    nombre,
                    apellido,
                    dni,
                    telefono,
                    direccion)
                console.print(tablaBuscarPorDni)    
                sleep(2) 
                
            else:
                    print("""
                        ####################################
                        
                        no se encontraron resultados para su búsqueda
                        
                        ####################################
                    
                        """)
            
        except sqlite3.Error as error:
            print("Falló al actualizar cliente en la base de datos", error)
            
            
def buscarReservaPorCliente():
    
    
        try:
            listarClientes()
            id_cliente = input('Ingresar id del cliente cuyas reservas desea buscar ')
            # sqlSelect = 'SELECT * FROM CLIENTES WHERE dni = ?'
            lista = [int(id_cliente),int(id_cliente)]
        
            valores = tuple(lista)
            # print(lista)
            sqlSelect = 'Select id_reserva , fecha_reserva , cantidad_dias , nombre , apellido , dni ,telefono, direccion from reserva ,clientes   where id_reserva in ( select id_reserva  from Clientes_reserva_alquiler where  id_cliente = ?) AND id_cliente = ?';
            # sqlSelect = 'Select id_reserva , fecha_reserva , cantidad_dias from reserva    where id_reserva in ( select id_reserva  from Clientes_reserva_alquiler where  id_cliente = ?) ';
            cursor.execute(sqlSelect,valores)
            clientesReservasResultado =  cursor.fetchall()
            conn.commit()
            
         
            
            
            
            if len(clientesReservasResultado):
                table =generarTablaBusquedaReserva()
                for item in clientesReservasResultado :
                    tupla_a_lista = list(item)
                    id_reserva= str(tupla_a_lista[0])
                    fecha_reserva = str(tupla_a_lista[1])
                    cantidad_dias = str(tupla_a_lista[2])
                    nombre = str(tupla_a_lista[3])
                    apellido = str(tupla_a_lista[4])
                    dni = str(tupla_a_lista[5])
                    telefono = str(tupla_a_lista[6])
                    direccion = str(tupla_a_lista[7])
                
                        
                    table.add_row(
                        id_reserva,
                        fecha_reserva,
                        cantidad_dias,
                        nombre,
                        apellido,
                        dni,
                        telefono,
                        direccion
                        
                        )
                console.print(table)    
                
                sleep(2) 
                    
                    
            
            
            
            else:
                    print("""
                        ####################################
                        
                        no se encontraron resultados para su búsqueda
                        
                        ####################################
                    
                        """)
            
        except sqlite3.Error as error:
            print("Falló la busqueda de la reserva", error)
    
def buscarClienteRegistroAlquiler():
        try:
            listarClientes()
            id_cliente = input('Ingresar id del cliente cuyos registros de alquiler desea buscar ')
            # sqlSelect = 'SELECT * FROM CLIENTES WHERE dni = ?'
            lista = [int(id_cliente),int(id_cliente)]
        
            valores = tuple(lista)
            # print(lista)
            sqlSelect = 'Select R.id_registro , R.id_auto , A.modelo , R.fecha_entrega , R.fecha_devolucion , R.importe_alquiler , R.observaciones , C.nombre , C.apellido , C.dni ,C.telefono, C.direccion from registro_alquiler R ,clientes C   inner join auto A on R.id_registro = A.id_Auto where id_registro in ( select id_registro  from Clientes_reserva_alquiler where   id_cliente = ?) AND id_cliente = ?';
            # sqlSelect = 'Select id_reserva , fecha_reserva , cantidad_dias from reserva    where id_reserva in ( select id_reserva  from Clientes_reserva_alquiler where  id_cliente = ?) ';
            cursor.execute(sqlSelect,valores)
            clientesRegistrosResultado =  cursor.fetchall()
            conn.commit()
            
         
            
            
            
            if len(clientesRegistrosResultado):
                table =generarTablaBusquedaRegistroAlquiler()
                for item in clientesRegistrosResultado :
                    tupla_a_lista = list(item)
                    id_registro= str(tupla_a_lista[0])
                    id_auto = str(tupla_a_lista[1])
                    auto = str(tupla_a_lista[2])
                    
                    fecha_entrega = str(tupla_a_lista[3])
                    fecha_devolucion= str(tupla_a_lista[4])
                    importe_alquiler = str(tupla_a_lista[5])
                    observaciones = str(tupla_a_lista[6])
                    nombre = str(tupla_a_lista[7])
                    apellido = str(tupla_a_lista[8])
                    dni = str(tupla_a_lista[9])
                    telefono = str(tupla_a_lista[10])
                    direccion = str(tupla_a_lista[11])
                
                        
                    table.add_row(
                        id_registro,
                        id_auto,
                          auto,
                       
                        fecha_entrega,
                        fecha_devolucion,
                        importe_alquiler,
                        observaciones,
                        nombre,
                        apellido,
                 
                        telefono,
                       
                        )
                console.print(table)    
                
                sleep(2) 
                    
                    
            
            
            
            else:
                
                          print("""
                        ####################################
                        
                        no se encontraron resultados para su búsqueda
                        
                        ####################################
                    
                        """)
               
            
        except sqlite3.Error as error:
            print("Falló la busqueda del registro de alquiler", error)
#      Select id_registro , id_auto , fecha_entrega , fecha_devolucion , importe_alquiler , observaciones , nombre , apellido , dni ,telefono, direccion from registro_alquiler ,clientes   
#  where id_registro in ( select id_registro  from Clientes_reserva_alquiler where   id_cliente = 2) AND id_cliente = 2;  
    
    

# Select R.id_registro , R.id_auto , A.modelo , R.fecha_entrega , R.fecha_devolucion , R.importe_alquiler , R.observaciones , C.nombre , C.apellido 
# , C.dni ,C.telefono, C.direccion from registro_alquiler R ,clientes C   inner join auto A on R.id_registro = A.id_Auto
#  where id_registro in ( select id_registro  from Clientes_reserva_alquiler where   id_cliente = 2) AND id_cliente = 2;  
def generarTabla() :
        table = Table(title="Tabla clientes")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Id", style="dim", width=12)
        table.add_column("Nombre")
        table.add_column("Apellido", justify="right")
        table.add_column("Dni", justify="right")
        table.add_column("Telefono", justify="right")
        table.add_column("Direccion", justify="right")
        return table
    
def generarTablaBusquedaReserva() :
        table = Table(title="Tabla clientes")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Id reserva", style="dim", width=12)
        table.add_column("Fecha reserva")
        table.add_column("Cantidad de dias", justify="right")
        table.add_column("nombre cliente", justify="right")
        table.add_column("apellido cliente", justify="right")
        table.add_column("dni cliente", justify="right")
        table.add_column("telefono cliente", justify="right")
        table.add_column("direccion cliente", justify="right")
        return table
        
        
def generarTablaBusquedaRegistroAlquiler() :
        table = Table(title="Tabla clientes")
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Id registro", style="dim", width=12)
        table.add_column("Id auto")
        table.add_column(" auto", justify="right")
        table.add_column("fecha de entrega", justify="right")
        table.add_column("fecha de devolucion", justify="right")
        table.add_column("importe alquiler", justify="right")
        table.add_column("observaciones", justify="right")
        table.add_column("nombre", justify="right")
        table.add_column("apellido", justify="right")
        table.add_column("telefono", justify="right")
       
        return table
    
# Select id_reserva , fecha_reserva , cantidad_dias , nombre from reserva ,clientes   where id_reserva = ( select id_reserva  from Clientes_reserva_alquiler where  id_cliente = 2) AND id_cliente = 2;