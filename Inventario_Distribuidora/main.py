
# SISTEMA DE INVENTARIO - DISTRIBUIDORA

productos = []


# FUNCION PARA REGISTRAR PRODUCTOS
def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese el codigo: ")
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)

    print("\nProducto registrado correctamente.")


# FUNCION PARA MOSTRAR EL MENU
def mostrar_menu():
    print("     SISTEMA DE INVENTARIO")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Salir")


# FUNCION PRINCIPAL
def iniciar_sistema():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            print("Consultar productos")

        elif opcion == "3":
            print("Actualizar productos")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


# EJECUTAR SISTEMA
iniciar_sistema()
 
