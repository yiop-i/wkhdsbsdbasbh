import gestion_stock
import menu


def main():
    gestion_stock.inicializar()

    opcion = 1
    while opcion != 0:
        opcion = menu.mostrar_menu()

        if opcion == 0:
            print("Hasta luego.")
        elif opcion == 1:
            gestion_stock.cargar_stock()
        elif opcion == 2:
            gestion_stock.mostrar_stock()
        elif opcion == 3:
            gestion_stock.contar_categoria()
        else:
            print("La opción ingresada no es válida.")


if __name__ == "__main__":
    main()