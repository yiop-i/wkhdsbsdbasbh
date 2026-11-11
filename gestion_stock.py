stock_productos = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": [],
}

stock_cantidades = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": [],
}


def inicializar():
    """Deja los diccionarios de stock vacíos."""
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []


def pedir_categoria():
    categoria = input(
        "Ingrese una categoría (enlatados, frutas, congelados, panaderia): "
    )

    if (
        categoria == "enlatados"
        or categoria == "frutas"
        or categoria == "congelados"
        or categoria == "panaderia"
    ):
        return categoria
    else:
        print("La categoría ingresada no existe.")
        return ""


def cargar_stock():
    categoria = pedir_categoria()
    if categoria != "":
        producto = input("Ingrese el nombre del producto: ")
        if producto == "":
            print("El nombre del producto no puede estar vacío.")
        else:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            while cantidad < 0:
                print("La cantidad no puede ser negativa.")
                cantidad = int(input("Ingrese la cantidad del producto: "))

            stock_productos[categoria].append(producto)
            stock_cantidades[categoria].append(cantidad)
            print("Producto cargado correctamente.")


def mostrar_stock():
    print("\nStock de la despensa")
    for categoria in stock_productos.keys():
        print("\n" + categoria + ":")
        if len(stock_productos[categoria]) == 0:
            print("  No hay productos cargados.")
        else:
            for indice in range(len(stock_productos[categoria])):
                producto = stock_productos[categoria][indice]
                cantidad = stock_cantidades[categoria][indice]
                print(f"  {producto}: {cantidad}")


def contar(lista_productos):
    cantidad_productos = len(lista_productos)
    cantidad_total = 0
    for cantidad in lista_productos:
        cantidad_total += cantidad

    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Cantidad total en stock: {cantidad_total}")


def contar_categoria():
    categoria = pedir_categoria()
    if categoria != "":
        contar(stock_cantidades[categoria])