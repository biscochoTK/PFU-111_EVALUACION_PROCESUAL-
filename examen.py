ARCHIVO = "inventario.txt"


def cargar_inventario():
    inventario = {}
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                codigo = datos[0]
                inventario[codigo] = {
                    "nombre": datos[1],
                    "precio": float(datos[2]),
                    "cantidad": int(datos[3])
                }
    except FileNotFoundError:
        print("No hay archivo guardado, se empieza con inventario vacío.")
    except (ValueError, IndexError):
        print("El archivo tiene datos dañados.")
    return inventario


def guardar_inventario(inventario):
    try:
        with open(ARCHIVO, "w") as archivo:
            for codigo in inventario:
                p = inventario[codigo]
                archivo.write(codigo + "," + p["nombre"] + "," +
                              str(p["precio"]) + "," + str(p["cantidad"]) + "\n")
    except OSError:
        print("Error: no se pudo guardar el archivo.")


def codigo_valido(codigo):
    # Formato PROD-001: empieza con "PROD-", mide 8 y termina en 3 números
    return len(codigo) == 8 and codigo[:5] == "PROD-" and codigo[5:].isdigit()


def registrar_producto(inventario):
    codigo = input("Código (ej. PROD-001): ").strip().upper()
    if codigo == "":
        print("Error: el código no puede estar vacío.")
        return
    if not codigo_valido(codigo):
        print("Error: el formato debe ser PROD-001.")
        return
    if codigo in inventario:
        print("Error: ese código ya existe.")
        return

    nombre = input("Nombre del producto: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    if "," in nombre:
        print("Error: el nombre no puede tener comas.")
        return

    try:
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad disponible: "))
    except ValueError:
        print("Error: ingrese solo números válidos.")
        return

    if precio <= 0:
        print("Error: el precio debe ser mayor que cero.")
        return
    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
        return

    inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    guardar_inventario(inventario)
    print("Producto registrado correctamente.")


def consultar_productos(inventario):
    if len(inventario) == 0:
        print("No hay productos registrados.")
        return
    print("\nCÓDIGO     NOMBRE               PRECIO    CANTIDAD")
    for codigo in inventario:
        p = inventario[codigo]
        print(codigo, "  ", p["nombre"], "  ", p["precio"], "  ", p["cantidad"])


def actualizar_cantidad(inventario):
    codigo = input("Código del producto: ").strip().upper()
    if codigo not in inventario:
        print("Error: el producto no está registrado.")
        return

    print("Cantidad actual:", inventario[codigo]["cantidad"])
    try:
        nueva = int(input("Nueva cantidad: "))
    except ValueError:
        print("Error: ingrese un número entero.")
        return

    if nueva < 0:
        print("Error: la cantidad no puede ser negativa.")
        return

    inventario[codigo]["cantidad"] = nueva
    guardar_inventario(inventario)
    print("Cantidad actualizada correctamente.")


def mostrar_menu():
    print("\n=== INVENTARIO DE LA DISTRIBUIDORA ===")
    print("1. Registrar un nuevo producto")
    print("2. Consultar los productos registrados")
    print("3. Actualizar la cantidad de un producto")
    print("4. Salir")


def main():
    inventario = cargar_inventario()
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            consultar_productos(inventario)
        elif opcion == "3":
            actualizar_cantidad(inventario)
        elif opcion == "4":
            print("Hasta luego.")
        else:
            print("Opción no válida. Elija de 1 a 4.")


main()