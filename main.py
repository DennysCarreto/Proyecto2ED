from clases import *
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Estructuras de Datos")
        self.geometry("650x450")

        # pila, cola, listas
        pila = Pila()

        # Crear el notebook
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Crear las pestañas
        pila_tab = ttk.Frame(notebook)
        notebook.add(pila_tab, text=" Pila")
        self.create_pila_tab(pila_tab)

        cola_tab = ttk.Frame(notebook)
        notebook.add(cola_tab, text=" Cola")
        self.create_cola_tab(cola_tab)

        listasimpleligada_tab = ttk.Frame(notebook)
        notebook.add(listasimpleligada_tab, text=" L SimpleL")
        self.create_cola_tab(listasimpleligada_tab)

        listacircular_tab = ttk.Frame(notebook)
        notebook.add(listacircular_tab, text=" L Circular")
        self.create_cola_tab(listacircular_tab)

        listadobleligada_tab = ttk.Frame(notebook)
        notebook.add(listadobleligada_tab, text=" L Doble Ligada")
        self.create_cola_tab(listadobleligada_tab)

        listacirculardoble_tab = ttk.Frame(notebook)
        notebook.add(listacirculardoble_tab, text=" L Circular Doble")
        self.create_cola_tab(listacirculardoble_tab)

        arbolbonario_tab = ttk.Frame(notebook)
        notebook.add(arbolbonario_tab, text=" A Binario")
        self.create_cola_tab(arbolbonario_tab)

        arbolBusqueda = ttk.Frame(notebook)
        notebook.add(arbolBusqueda, text=" A Busqueda")
        self.create_cola_tab(arbolBusqueda)

    def create_pila_tab(self, tab):
        # Crear un marco para los campos de entrada y botones
        frame = ttk.Frame(tab)
        frame.pack(padx=10, pady=10)

        # Campo de entrada para ingresar el valor
        self.valor_entrada = ttk.Entry(frame)
        self.valor_entrada.pack(pady=5)

        # Botón para insertar
        insertar_boton = ttk.Button(frame, text="Insertar", command=self.insertar_pila)
        insertar_boton.pack(pady=5)

        # Botón para eliminar
        eliminar_boton = ttk.Button(frame, text="Eliminar", command=self.eliminar_pila)
        eliminar_boton.pack(pady=5)

        # Campo de entrada para buscar
        self.buscar_entrada = ttk.Entry(frame)
        self.buscar_entrada.pack(pady=5)

        # Botón para buscar
        buscar_boton = ttk.Button(frame, text="Buscar", command=self.buscar_pila)
        buscar_boton.pack(pady=5)

        # Área de texto para mostrar la pila
        self.pila_texto = tk.Text(frame, height=10, width=30)
        self.pila_texto.pack(pady=5)

    def insertar_pila(self):
        valor = self.valor_entrada.get()
        if valor:
            pila.insertar(valor)
            self.valor_entrada.delete(0, tk.END)
            self.actualizar_pila_texto()
            print(pila.imprimir_pila())

    def eliminar_pila(self):
        delete = pila.eliminar()
        if delete is None:
            mensaje = f"Pila esta vacia"
            self.pila_texto.delete(1.0, tk.END)
            self.pila_texto.insert(tk.END, mensaje)
            print(pila.imprimir_pila())
        else:
            mensaje = f"Se elimino {delete} de la pila"
            self.pila_texto.delete(1.0, tk.END)
            self.pila_texto.insert(tk.END, mensaje)
            self.pila_texto.delete(1.0, tk.END)
            self.actualizar_pila_texto()
            print(pila.imprimir_pila())

    def buscar_pila(self):
        valor = self.buscar_entrada.get()
        sino = pila.buscar_valor(valor)
        if sino is True:
            mensaje = f"El valor {valor} se encuentra en la pila."
        else:
            mensaje = f"El valor {valor} no se encuentra en la pila."
        self.pila_texto.delete(1.0, tk.END)
        self.pila_texto.insert(tk.END, mensaje)

    def actualizar_pila_texto(self):
        self.pila_texto.delete(1.0, tk.END)  # Limpiar el contenido actual del widget de texto
        if pila.esta_vacia():
            mensaje = f"Lista vacia"
            self.pila_texto.delete(1.0, tk.END)
            self.pila_texto.insert(tk.END, mensaje)
        else:
            valor = pila.imprimir_pilax()
            self.pila_texto.delete(1.0, tk.END)
            self.pila_texto.insert(tk.END, valor)
            pila.imprimir_pilax()

    def create_cola_tab(self, tab):
            # Añade los campos y botones para la pestaña "Cola"
            pass

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


def menu_lista_circular_doble(lista):
    listacd = lista
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
            listacd.insertar_inicio(dato)
        elif opcion == "2":
            dato = input("Ingrese el dato a insertar al final: ")
            listacd.insertar_final(dato)
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
    pila = Pila()
    app = App()
    app.mainloop()
    # while True:
    #     print("Menú:")
    #     print("1. Pila")
    #     print("2. Cola")
    #     print("3. Lista simplemente ligada")
    #     print("4. Lista circular")
    #     print("5. Lista doblemente ligada")
    #     print("6. Lista circular doble")
    #     print("7. Árbol binario")
    #     print("8. Árbol de búsqueda")
    #     print("9. Salir")
    #
    #     opcion = input("Selecciona una opción: ")
    #
    #     if opcion == "1":
    #         menu_pila()
    #     elif opcion == "2":
    #         menu_cola()
    #     elif opcion == "3":
    #         menu_lista_simplemente_ligada()
    #     elif opcion == "4":
    #         menu_lista_circular()
    #     elif opcion == "5":
    #         menu_lista_doblemente_ligada()
    #     elif opcion == "6":
    #         menu_lista_circular_doble()
    #     elif opcion == "7":
    #         menu_arbol_binario()
    #     elif opcion == "8":
    #         menu_arbol_de_busqueda()
    #     elif opcion == "9":
    #         print("¡Hasta luego!")
    #         break
    #     else:
    #         print("Opción inválida. Inténtalo de nuevo.")
