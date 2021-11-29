from menus import *

from funciones import *

from rich import print




seguir = True

while seguir:
    inicio = funcionMenu(menuPrincipal)

    if inicio == '1':
        seguirEnClientes = True
        while seguirEnClientes:
            
         
            
            opcionClientes = funcionMenu(menuClientes)
            if opcionClientes == '1':
                borrar_pantalla()
                insertarClientes()
            if opcionClientes == '2':
                borrar_pantalla()
                borrarCliente()
            if opcionClientes == '3':
                borrar_pantalla()
                editarCliente()
            if opcionClientes == '4':
                borrar_pantalla()
                listarClientes()
            if opcionClientes == '5':
                seguirEnBusqueda = True
                while seguirEnBusqueda:
                 
                    
                    opcionBusquedaClientes = funcionMenu(menuBuscarClientes)
                    
                    if opcionBusquedaClientes == '1':
                                        print("""
                        ####################################
                        
                        esta opcion no ha sido implementada
                        
                        ####################################
                    
                        """)
                    if opcionBusquedaClientes == '6':
                        borrar_pantalla()
                        seguirEnBusqueda = False
                    if opcionBusquedaClientes == '2':
                       
                        borrar_pantalla()
                        buscarClientePorDni()
                    if opcionBusquedaClientes == '3':
                        borrar_pantalla()
                        buscarReservaPorCliente()
                    if  opcionBusquedaClientes == '4':   
                        borrar_pantalla()
                        buscarClienteRegistroAlquiler()
                        
                    if  opcionBusquedaClientes == '5':   
                                      print("""
                        ####################################
                        
                        esta opcion no ha sido implementada
                        
                        ####################################
                    
                        """)
                    
            if opcionClientes == '6':
                seguirEnClientes = False
        
    elif inicio == '2':
        # funcionMenu(menuAutos)
            print("""
              ####################################
              
              esta opcion no ha sido implementada
              
              ####################################
          
              """)

    elif inicio == '3':
        # funcionMenu(menuSucursal)
          print("""
              ####################################
              
              esta opcion no ha sido implementada
              
              ####################################
          
              """)
        
    elif inicio == '4':
        # funcionMenu(menuRegistro)
              print("""
              ####################################
              
              esta opcion no ha sido implementada
              
              ####################################
          
              """)
        
    elif inicio == '5':
        # funcionMenu(menuCategorias)
          print("""
              ####################################
              
              esta opcion no ha sido implementada
              
              ####################################
          
              """)
    elif inicio == '6':
        seguir=False
        
    
    
    
