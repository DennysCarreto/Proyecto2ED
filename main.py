import tkinter as tk
from operaciones import VentanaOperaciones

class AplicacionEstructurasDatos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Estructuras de Datos")
        self.geometry("700x600")

        # Crear secciones principales
        self.tipo_dato()
        self.estructura_datos()

    def tipo_dato(self):
        marco_tipo_dato = tk.LabelFrame(self, text="Tipo de Dato", padx=10, pady=10)
        marco_tipo_dato.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tipos_datos = ["Entero", "Flotante", "Booleano", "Cadena", "TAD"]
        self.variable_tipo_dato = tk.StringVar(value=tipos_datos[0])
        for tipo_dato in tipos_datos:
            radio_tipo_dato = tk.Radiobutton(marco_tipo_dato, text=tipo_dato, variable=self.variable_tipo_dato, value=tipo_dato)
            radio_tipo_dato.pack(side=tk.LEFT, padx=5)

    def estructura_datos(self):
        marco_estructura_datos = tk.LabelFrame(self, text="Estructura de Datos", padx=10, pady=10)
        marco_estructura_datos.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.variable_estructura_datos = tk.StringVar()
        self.marco_operaciones = tk.Frame(self)
        self.marco_operaciones.pack(side=tk.BOTTOM, padx=10, pady=10)

        fila = 0
        columna = 0

        boton_pila = tk.Button(marco_estructura_datos, text="Pila", command=lambda: self.mostrar_operaciones("Pila"))
        boton_pila.grid(row=fila, column=columna, padx=5, pady=5)
        columna += 1

        boton_cola = tk.Button(marco_estructura_datos, text="Cola", command=lambda: self.mostrar_operaciones("Cola"))
        boton_cola.grid(row=fila, column=columna, padx=5, pady=5)
        columna += 1

        boton_lista_simple = tk.Button(marco_estructura_datos, text="Lista Simple", command=lambda: self.mostrar_operaciones("Lista Simple"))
        boton_lista_simple.grid(row=fila, column=columna, padx=5, pady=5)
        columna += 1

        boton_lista_circular = tk.Button(marco_estructura_datos, text="Lista Circular", command=lambda: self.mostrar_operaciones("Lista Circular"))
        boton_lista_circular.grid(row=fila, column=columna, padx=5, pady=5)
        columna = 0
        fila += 1

        boton_lista_doble = tk.Button(marco_estructura_datos, text="Lista Doblemente Ligada", command=lambda: self.mostrar_operaciones("Lista Doblemente Ligada"))
        boton_lista_doble.grid(row=fila, column=columna, padx=5, pady=5)
        columna += 1

        boton_lista_circular_doble = tk.Button(marco_estructura_datos, text="Lista Circular Doble", command=lambda: self.mostrar_operaciones("Lista Circular Doble"))
        boton_lista_circular_doble.grid(row=fila, column=columna, padx=5, pady=5)
        columna += 1

        boton_arbol_binario = tk.Button(marco_estructura_datos, text="Arbol Binario", command=lambda: self.mostrar_operaciones("Arbol Binario"))
        boton_arbol_binario.grid(row=fila, column=columna, padx=5, pady=5)
        columna += 1

        boton_arbol_busqueda = tk.Button(marco_estructura_datos, text="Arbol de Busqueda", command=lambda: self.mostrar_operaciones("Arbol de Busqueda"))
        boton_arbol_busqueda.grid(row=fila, column=columna, padx=5, pady=5)

    # def mostrar_operaciones(self, estructura_datos):
    #     for widget in self.marco_operaciones.winfo_children():
    #         widget.destroy()
    #
    #     if estructura_datos == "Pila":
    #         boton_insertar = tk.Button(self.marco_operaciones, text="Insertar")
    #         boton_insertar.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar = tk.Button(self.marco_operaciones, text="Eliminar")
    #         boton_eliminar.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos == "Cola":
    #         boton_insertar = tk.Button(self.marco_operaciones, text="Insertar")
    #         boton_insertar.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar = tk.Button(self.marco_operaciones, text="Eliminar")
    #         boton_eliminar.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos == "Lista Simple":
    #         boton_insertar_inicio = tk.Button(self.marco_operaciones, text="Insertar al Inicio")
    #         boton_insertar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_insertar_final = tk.Button(self.marco_operaciones, text="Insertar al Final")
    #         boton_insertar_final.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_inicio = tk.Button(self.marco_operaciones, text="Eliminar del Inicio")
    #         boton_eliminar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_final = tk.Button(self.marco_operaciones, text="Eliminar del Final")
    #         boton_eliminar_final.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos =="Lista Circular":
    #         boton_insertar_inicio = tk.Button(self.marco_operaciones, text="Insertar al Inicio")
    #         boton_insertar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_insertar_final = tk.Button(self.marco_operaciones, text="Insertar al Final")
    #         boton_insertar_final.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_inicio = tk.Button(self.marco_operaciones, text="Eliminar del Inicio")
    #         boton_eliminar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_final = tk.Button(self.marco_operaciones, text="Eliminar del Final")
    #         boton_eliminar_final.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #         btn_rotar_derecha = tk.Button(self.marco_operaciones, text="Rotar Derecha")
    #         btn_rotar_derecha.pack(side=tk.LEFT, padx=5)
    #         btn_rotar_izquierda = tk.Button(self.marco_operaciones, text="Rotar Izquierda")
    #         btn_rotar_izquierda.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos == "Lista Doblemente Ligada":
    #         boton_insertar_inicio = tk.Button(self.marco_operaciones, text="Insertar al Inicio")
    #         boton_insertar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_insertar_final = tk.Button(self.marco_operaciones, text="Insertar al Final")
    #         boton_insertar_final.pack(side=tk.LEFT, padx=5)
    #         boton_insertar_posicion = tk.Button(self.marco_operaciones, text="Insertar por Posicion")
    #         boton_insertar_posicion.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_inicio = tk.Button(self.marco_operaciones, text="Eliminar del Inicio")
    #         boton_eliminar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_final = tk.Button(self.marco_operaciones, text="Eliminar del Final")
    #         boton_eliminar_final.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_posicion = tk.Button(self.marco_operaciones, text="Eliminar por Posicion")
    #         boton_eliminar_posicion.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos == "Lista Circular Doble":
    #         boton_insertar_inicio = tk.Button(self.marco_operaciones, text="Insertar al Inicio")
    #         boton_insertar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_insertar_final = tk.Button(self.marco_operaciones, text="Insertar al Final")
    #         boton_insertar_final.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_inicio = tk.Button(self.marco_operaciones, text="Eliminar del Inicio")
    #         boton_eliminar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar_final = tk.Button(self.marco_operaciones, text="Eliminar del Final")
    #         boton_eliminar_final.pack(side=tk.LEFT, padx=5)
    #         btn_rotar_derecha = tk.Button(self.marco_operaciones, text="Rotar Derecha")
    #         btn_rotar_derecha.pack(side=tk.LEFT, padx=5)
    #         btn_rotar_izquierda = tk.Button(self.marco_operaciones, text="Rotar Izquierda")
    #         btn_rotar_izquierda.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos == "Arbol Binario":
    #         boton_insertar_inicio = tk.Button(self.marco_operaciones, text="Insertar al Izquierda")
    #         boton_insertar_inicio.pack(side=tk.LEFT, padx=5)
    #         boton_insertar_final = tk.Button(self.marco_operaciones, text="Insertar al Derecha")
    #         boton_insertar_final.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar = tk.Button(self.marco_operaciones, text="Eliminar")
    #         boton_eliminar.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     elif estructura_datos == "Arbol de Busqueda":
    #         boton_insertar = tk.Button(self.marco_operaciones, text="Insertar al Derecha")
    #         boton_insertar.pack(side=tk.LEFT, padx=5)
    #         boton_eliminar = tk.Button(self.marco_operaciones, text="Eliminar")
    #         boton_eliminar.pack(side=tk.LEFT, padx=5)
    #         boton_buscar = tk.Button(self.marco_operaciones, text="Buscar")
    #         boton_buscar.pack(side=tk.LEFT, padx=5)
    #     # Agrega más condiciones para las demás estructuras de datos

    def mostrar_operaciones(self, estructura_datos):
        ventana_operaciones = VentanaOperaciones(self, estructura_datos)

if __name__ == "__main__":
    app = AplicacionEstructurasDatos()
    app.mainloop()
