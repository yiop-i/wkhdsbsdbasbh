CONSIGNA
Sistema de manejo de stock de una despensa
Una despensa contrató tus servicios para ayudarles a crear un sistema que les ayuda a manejar su stock.

Estructura del proyecto
El sistema debe estar dividido en tres archivos, de modo que cada uno tenga una única responsabilidad:

Sistema.py: es el archivo principal. Debe importar las funciones de Menu.py para saber qué opción eligió el usuario y, según el retorno, enviar esa opción a Gestion_stock.py para que realice la lógica correspondiente. Alémás, es el encargado de inicializar el sistema y de armar el ciclo principal del menú.

Menu.py: debe contener las funciones que muestran el menú al usuario y leen la opción elegida. La función del menú debe devolver (retornar) la opción seleccionada para que Sistema.py pueda actuar sobre ella.

Gestion_stock.py: debe contener la lógica del stock: cargar stock, mostrar el total del stock, contar productos y la función de inicialización de los diccionarios.

Requisitos de la separación
Sistema.py debe usar import Menu e import Gestion_stock (o from ... import ...) para consumir las funciones de los otros dos archivos.
Ningún archivo debe contener toda la lógica por sí solo: la lógica de negocio va en Gestion_stock.py y la interacción con el usuario va en Menu.py.
Sistema.py no debe mostrar el menú directamente: debe pedirle a Menu.py la opción elegida y, a partir del retorno, invocar a la función correspondiente de Gestion_stock.py.
Comportamiento del menú
Requiere un menú que le muestre las siguientes opciones:
Cargar stock
Mostrar total del stock
Mostrar cantidad de productos
El stock debe estar representado por dos diccionarios:

Por un lado, uno cuyas claves sean los tipos de productos que se pueden vender (frutas, congelados, panadería, enlatados...) y los valores, listas que contengan el producto en cuestión.

Por otro lado, uno cuyas claves sean los mismos tipos de productos que se pueden vender (frutas, congelados, panadería, enlatados...) y los valores, listas que contengan la cantidad del producto en cuestión.

Ej:

stock_productos = { 'enlatados': ['Salsa de tomate', 'atún'], 'frutas': ['Manzana', 'Pera', 'Banana'] }

stock_cantidades = { 'enlatados': [5, 10], 'frutas': [0, 3, 20] }

En este ejemplo, el stock dice que hay 5 latas de salsa de tomate, 10 de atún, 0 manzanas, 3 peras y 20 bananas.

ESTOS DICCIONARIOS DEBEN COMENZAR VACÍOS AL PRINCIPIO EN SUS VALORES:

stock_productos = { 'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': [] } stock_cantidades = { 'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': [] }

Para esto NO se setea el estado inicial a mano en el main, sino que los diccionarios deben vaciarse (limpiarse) dentro de una función de inicialización. Por ejemplo:

def inicializar():
    """Deja los diccionarios de stock vacíos, listos para cargar productos."""
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []
Esa función de inicialización debe vivir en Gestion_stock.py y ser llamada por Sistema.py al comienzo de la ejecución, antes de mostrar el menú.

Cargar stock
Cargar stock debe permitir ingresar una categoría (enlatados, frutas, congelados, panadería) y luego preguntar qué producto se debe añadir y cuánto del producto. El nombre va a stock_productos y la cantidad a stock_cantidades.

Esta opción se implementa en Gestion_stock.py (por ejemplo, con una función cargar_stock()), a la que Sistema.py llama luego de recibir el retorno del menú.

Mostrar total del stock
Debe imprimir de forma ordenada ambos diccionarios, para que el usuario pueda ver el stock y la cantidad.

Esta opción se implementa en Gestion_stock.py (por ejemplo, con una función mostrar_stock()), a la que Sistema.py llama luego de recibir el retorno del menú.

Mostrar la cantidad de producto
Primero, debe preguntar el tipo de producto que desea contar (enlatados, frutas, congelados, panaderia).

Luego, debe llamar a una función contar(lista_productos), que tome como argumento una lista de productos de stock_cantidades e imprima dos números: La cantidad de productos que hay y la suma de las cantidades de todos los productos.

La función contar() debe estar definida en Gestion_stock.py.

Estructura esperada del código
Un ejemplo de cómo debería verse la separación de responsabilidades (el código exacto es libre, siempre que se respeten los requisitos):

# Menu.py
def mostrar_menu():
    print("1. Cargar stock")
    print("2. Mostrar total del stock")
    print("3. Mostrar cantidad de productos")
    opcion = int(input("Elija una opción: "))
    return opcion  # el menú devuelve la opción elegida
# Gestion_stock.py
stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}

def inicializar():
    ...

def cargar_stock():
    ...

def mostrar_stock():
    ...

def contar(lista_productos):
    ...
# Sistema.py
import Menu
import Gestion_stock

def main():
    Gestion_stock.inicializar()
    opcion = Menu.mostrar_menu()
    if opcion == 1:
        Gestion_stock.cargar_stock()
    elif opcion == 2:
        Gestion_stock.mostrar_stock()
    elif opcion == 3:
        # pedir la categoría y llamar a Gestion_stock.contar(...)
        ...

if __name__ == "__main__":
    main()