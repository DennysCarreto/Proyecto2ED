import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Estructuras de Datos")

        self.label = tk.Label(master, text="Seleccione una estructura de datos:")
        self.label.pack()

        self.button_stack = tk.Button(master, text="Pila", command=self.create_stack)
        self.button_stack.pack()

        self.button_queue = tk.Button(master, text="Cola", command=self.create_queue)
        self.button_queue.pack()

        self.button_linked_list = tk.Button(master, text="Lista Simple", command=self.create_linked_list)
        self.button_linked_list.pack()

        self.button_circular_list = tk.Button(master, text="Lista Circular", command=self.create_circular_list)
        self.button_circular_list.pack()

        # Agrega más botones para las otras estructuras de datos

    def create_stack(self):
        stack_window = tk.Toplevel(self.master)
        stack_window.title("Pila")

        insert_button = tk.Button(stack_window, text="Insertar")
        insert_button.pack(side=tk.LEFT, padx=5)
        remove_button = tk.Button(stack_window, text="Eliminar")
        remove_button.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(stack_window, text="Buscar")
        search_button.pack(side=tk.LEFT, padx=5)

    def create_queue(self):
        queue_window = tk.Toplevel(self.master)
        queue_window.title("Cola")

        insert_button = tk.Button(queue_window, text="Insertar")
        insert_button.pack(side=tk.LEFT, padx=5)
        remove_button = tk.Button(queue_window, text="Eliminar")
        remove_button.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(queue_window, text="Buscar")
        search_button.pack(side=tk.LEFT, padx=5)

    def create_linked_list(self):
        linked_list_window = tk.Toplevel(self.master)
        linked_list_window.title("Lista Simple")

        insert_start_button = tk.Button(linked_list_window, text="Insertar al Inicio")
        insert_start_button.pack(side=tk.LEFT, padx=5)
        insert_end_button = tk.Button(linked_list_window, text="Insertar al Final")
        insert_end_button.pack(side=tk.LEFT, padx=5)
        remove_start_button = tk.Button(linked_list_window, text="Eliminar del Inicio")
        remove_start_button.pack(side=tk.LEFT, padx=5)
        remove_end_button = tk.Button(linked_list_window, text="Eliminar del Final")
        remove_end_button.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(linked_list_window, text="Buscar")
        search_button.pack(side=tk.LEFT, padx=5)

    def create_circular_list(self):
        circular_list_window = tk.Toplevel(self.master)
        circular_list_window.title("Lista Circular")

        insert_start_button = tk.Button(circular_list_window, text="Insertar al Inicio")
        insert_start_button.pack(side=tk.LEFT, padx=5)
        insert_end_button = tk.Button(circular_list_window, text="Insertar al Final")
        insert_end_button.pack(side=tk.LEFT, padx=5)
        remove_start_button = tk.Button(circular_list_window, text="Eliminar del Inicio")
        remove_start_button.pack(side=tk.LEFT, padx=5)
        remove_end_button = tk.Button(circular_list_window, text="Eliminar del Final")
        remove_end_button.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(circular_list_window, text="Buscar")
        search_button.pack(side=tk.LEFT, padx=5)
        rotate_left_button = tk.Button(circular_list_window, text="Rotar a la Izquierda")
        rotate_left_button.pack(side=tk.LEFT, padx=5)
        rotate_right_button = tk.Button(circular_list_window, text="Rotar a la Derecha")
        rotate_right_button.pack(side=tk.LEFT, padx=5)

    # Agrega métodos similares para las otras estructuras de datos

root = tk.Tk()
app = App(root)
root.mainloop()