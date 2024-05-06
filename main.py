from clases import *


def menu_pila():
    pila = Pila()
    while True:
        print("\nMenú Pila:")
        print("1. Insertar")
        print("2. Eliminar")
        print("3. Buscar valor")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a insertar: ")
            pila.insertar(valor)
        elif opcion == "2":
            print("Se ha eliminado el valor:", pila.eliminar())
        elif opcion == "3":
            valor = input("Ingrese el valor a buscar: ")
            if pila.buscar_valor(valor):
                print("El valor", valor, "se encuentra en la pila.")
            else:
                print("El valor", valor, "no se encuentra en la pila.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


def menu_cola():
    cola = Cola()
    while True:
        print("\nMenú Cola:")
        print("1. Insertar")
        print("2. Eliminar")
        print("3. Buscar valor")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a insertar: ")
            cola.insertar(valor)
        elif opcion == "2":
            print("Se ha eliminado el valor:", cola.eliminar())
        elif opcion == "3":
            valor = input("Ingrese el valor a buscar: ")
            if cola.buscar_valor(valor):
                print("El valor", valor, "se encuentra en la cola.")
            else:
                print("El valor", valor, "no se encuentra en la cola.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


def menu_lista_simplemente_ligada():
    lista = LSimplementeLigada()
    while True:
        print("\nMenú Lista Simplemente Ligada:")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar inicio")
        print("4. Eliminar final")
        print("5. Buscar valor")
        print("6. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a insertar al inicio: ")
            lista.insertar_inicio(valor)
        elif opcion == "2":
            valor = input("Ingrese el valor a insertar al final: ")
            lista.insertar_final(valor)
        elif opcion == "3":
            print("Se ha eliminado el valor:", lista.eliminar_inicio())
        elif opcion == "4":
            print("Se ha eliminado el valor:", lista.eliminar_final())
        elif opcion == "5":
            valor = input("Ingrese el valor a buscar: ")
            if lista.buscar_valor(valor):
                print("El valor", valor, "se encuentra en la lista.")
            else:
                print("El valor", valor, "no se encuentra en la lista.")
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


def menu_lista_circular():
    lista = ListaCircular()
    while True:
        print("\n--- Menú Lista Circular Simple ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar al inicio")
        print("4. Eliminar al final")
        print("5. Buscar valor")
        print("6. Rotar a la izquierda")
        print("7. Rotar a la derecha")
        print("8. Imprimir lista")
        print("9. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dato = input("Ingrese el dato a insertar al inicio: ")
            lista.insertar_inicio(dato)
        elif opcion == "2":
            dato = input("Ingrese el dato a insertar al final: ")
            lista.insertar_final(dato)
        elif opcion == "3":
            dato_eliminado = lista.eliminar_inicio()
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "4":
            dato_eliminado = lista.eliminar_final()
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "5":
            dato = input("Ingrese el valor a buscar: ")
            resultado = lista.buscar_dato(dato)
            if resultado:
                print("El valor", dato, "se encuentra en la lista.")
            else:
                print("El valor", dato, "no se encuentra en la lista.")
        elif opcion == "6":
            lista.rotar_izquierda()
            print("Se ha rotado la lista a la izquierda.")
        elif opcion == "7":
            lista.rotar_derecha()
            print("Se ha rotado la lista a la derecha.")
        elif opcion == "8":
            print("Lista actual:")
            lista.imprimir_lista()
        elif opcion == "9":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def menu_lista_doblemente_ligada():
    lista = LDobleLigada
    while True:
        print("\n--- Menú Lista Doblemente Ligada ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar por posición")
        print("4. Eliminar al inicio")
        print("5. Eliminar al final")
        print("6. Eliminar por posición")
        print("7. Buscar valor")
        print("8. Imprimir lista")
        print("9. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dato = input("Ingrese el dato a insertar al inicio: ")
            lista.insertar_inicio(dato)
        elif opcion == "2":
            dato = input("Ingrese el dato a insertar al final: ")
            lista.insertar_final(dato)
        elif opcion == "3":
            dato = input("Ingrese el dato a insertar: ")
            posicion = int(input("Ingrese la posición donde desea insertar el dato: "))
            lista.insertar_por_posicion(dato, posicion)
        elif opcion == "4":
            dato_eliminado = lista.eliminar_inicio()
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "5":
            dato_eliminado = lista.eliminar_final()
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "6":
            posicion = int(input("Ingrese la posición del dato que desea eliminar: "))
            dato_eliminado = lista.eliminar_por_posicion(posicion)
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "7":
            dato = input("Ingrese el valor a buscar: ")
            resultado = lista.buscar_dato(dato)
            if resultado:
                print("El valor", dato, "se encuentra en la lista.")
            else:
                print("El valor", dato, "no se encuentra en la lista.")
        elif opcion == "8":
            print("Lista actual:")
            lista.imprimir_lista()
        elif opcion == "9":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def menu_lista_circular_doble():
    lista = LCircularDoble
    while True:
        print("\n--- Menú Lista Circular Doble ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar al inicio")
        print("4. Eliminar al final")
        print("5. Buscar valor")
        print("6. Rotar a la izquierda")
        print("7. Rotar a la derecha")
        print("8. Imprimir lista")
        print("9. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dato = input("Ingrese el dato a insertar al inicio: ")
            lista.insertar_inicio(dato)
        elif opcion == "2":
            dato = input("Ingrese el dato a insertar al final: ")
            lista.insertar_final(dato)
        elif opcion == "3":
            dato_eliminado = lista.eliminar_inicio()
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "4":
            dato_eliminado = lista.eliminar_final()
            if dato_eliminado:
                print("Se ha eliminado el dato", dato_eliminado)
        elif opcion == "5":
            dato = input("Ingrese el valor a buscar: ")
            resultado = lista.buscar_dato(dato)
            if resultado:
                print("El valor", dato, "se encuentra en la lista.")
            else:
                print("El valor", dato, "no se encuentra en la lista.")
        elif opcion == "6":
            lista.rotar_izquierda()
            print("Se ha rotado la lista a la izquierda.")
        elif opcion == "7":
            lista.rotar_derecha()
            print("Se ha rotado la lista a la derecha.")
        elif opcion == "8":
            print("Lista actual:")
            lista.imprimir_lista()
        elif opcion == "9":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def menu_arbol_binario():
    arbol = ABinario()
    while True:
        print("\n--- Menú Árbol Binario ---")
        print("1. Insertar a la izquierda")
        print("2. Insertar a la derecha")
        print("3. Eliminar")
        print("4. Buscar valor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a insertar a la izquierda: ")
            arbol.insertar(valor)
        elif opcion == "2":
            valor = input("Ingrese el valor a insertar a la derecha: ")
            arbol.insertar(valor)
        elif opcion == "3":
            valor = input("Ingrese el valor a eliminar: ")
            arbol.eliminar(valor)
        elif opcion == "4":
            valor = input("Ingrese el valor a buscar: ")
            resultado = arbol.buscar(valor)
            if resultado:
                print("El valor", valor, "se encuentra en el árbol.")
            else:
                print("El valor", valor, "no se encuentra en el árbol.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def menu_arbol_de_busqueda():
    arbol = ABusqueda()
    while True:
        print("\n--- Menú Árbol de Búsqueda ---")
        print("1. Insertar valor")
        print("2. Eliminar valor")
        print("3. Buscar valor")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a insertar: ")
            arbol.insertar(valor)
        elif opcion == "2":
            valor = input("Ingrese el valor a eliminar: ")
            arbol.eliminar(valor)
        elif opcion == "3":
            valor = input("Ingrese el valor a buscar: ")
            resultado = arbol.buscar(valor)
            if resultado:
                print("El valor", valor, "se encuentra en el árbol.")
            else:
                print("El valor", valor, "no se encuentra en el árbol.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    while True:
        print("Menú:")
        print("1. Pila")
        print("2. Cola")
        print("3. Lista simplemente ligada")
        print("4. Lista circular")
        print("5. Lista doblemente ligada")
        print("6. Lista circular doble")
        print("7. Árbol binario")
        print("8. Árbol de búsqueda")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_pila()
        elif opcion == "2":
            menu_cola()
        elif opcion == "3":
            menu_lista_simplemente_ligada()
        elif opcion == "4":
            menu_lista_circular()
        elif opcion == "5":
            menu_lista_doblemente_ligada()
        elif opcion == "6":
            menu_lista_circular_doble()
        elif opcion == "7":
            menu_arbol_binario()
        elif opcion == "8":
            menu_arbol_de_busqueda()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
