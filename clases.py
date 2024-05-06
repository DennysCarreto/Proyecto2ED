from nodos import *


class Pila:
    def __init__(self):
        self.tope = None
        self.fondo = None
        self.tamano = 0

    def esta_vacia(self):
        return self.tope is None

    def insertar(self, dato):
        nuevo_nodo = NodoPila(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        if self.fondo is None:
            self.fondo = nuevo_nodo
        self.tamano += 1

    def eliminar(self):
        if self.esta_vacia():
            print("La pila está vacía")
            return None
        valor_eliminado = self.tope.dato
        self.tope = self.tope.siguiente
        if self.tope is None:
            self.fondo = None
        self.tamano -= 1
        return valor_eliminado

    def tamano_pila(self):
        return self.tamano

    def obtener_tope(self):
        if self.esta_vacia():
            print("La pila está vacía")
            return None
        return self.tope.dato

    def obtener_fondo(self):
        if self.esta_vacia():
            print("La pila está vacía")
            return None
        return self.fondo.dato

    def imprimir_pila(self):
        actual = self.tope
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def buscar_valor(self, dato):
        actual = self.tope
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    # retorna el dato que esta buscando, si lo encuentra
    def buscar_rdato(self, dato):
        actual = self.tope
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None


class Cola:
    def __init__(self):
        self.frente = None
        self.fondo = None
        self.tamano = 0

    def esta_vacia(self):
        return self.frente is None

    def insertar(self, dato):
        nuevo_nodo = NodoCola(dato)
        if self.esta_vacia():
            self.frente = nuevo_nodo
        else:
            self.fondo.siguiente = nuevo_nodo
        self.fondo = nuevo_nodo
        self.tamano += 1

    def eliminar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        valor_eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.fondo = None
        self.tamano -= 1
        return valor_eliminado

    def tamano_cola(self):
        return self.tamano

    def obtener_frente(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        return self.frente.dato

    def obtener_fondo(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        return self.fondo.dato

    def imprimir_cola(self):
        actual = self.frente
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def buscar_valor(self, dato):
        actual = self.frente
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None


class LSimplementeLigada:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        return self.inicio is None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoListaSimplementeLigada(dato)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo
        self.tamano += 1

    def insertar_final(self, dato):
        nuevo_nodo = NodoListaSimplementeLigada(dato)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.inicio.dato
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.inicio = self.inicio.siguiente
        self.tamano -= 1
        return valor_eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.final.dato
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            actual = self.inicio
            while actual.siguiente != self.final:
                actual = actual.siguiente
            actual.siguiente = None
            self.final = actual
        self.tamano -= 1
        return valor_eliminado

    def tamano_lista(self):
        return self.tamano

    def obtener_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.inicio.dato

    def obtener_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.final.dato

    def imprimir_lista(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def buscar_valor(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None


class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        return self.inicio is None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoListaCircular(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo  # El siguiente apunta a sí mismo
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.final.siguiente = nuevo_nodo
            self.inicio = nuevo_nodo
        self.tamano += 1

    def insertar_final(self, dato):
        nuevo_nodo = NodoListaCircular(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo  # El siguiente apunta a sí mismo
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.inicio.dato
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.final.siguiente = self.inicio.siguiente
            self.inicio = self.inicio.siguiente
        self.tamano -= 1
        return valor_eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.final.dato
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            actual = self.inicio
            while actual.siguiente != self.final:
                actual = actual.siguiente
            actual.siguiente = self.inicio
            self.final = actual
        self.tamano -= 1
        return valor_eliminado

    def tamano_lista(self):
        return self.tamano

    def obtener_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.inicio.dato

    def obtener_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.final.dato

    def imprimir_lista(self):
        actual = self.inicio
        if actual:
            while actual.siguiente != self.inicio:
                print(actual.dato, end=" -> ")
                actual = actual.siguiente
            print(actual.dato, end=" -> ")
            print("None")
        else:
            print("None")

    def buscar_dato(self, dato):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        actual = self.inicio
        while True:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
            if actual == self.inicio:
                break
        return None

    def rotar_izquierda(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return
        self.final = self.inicio
        self.inicio = self.inicio.siguiente

    def rotar_derecha(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return
        actual = self.inicio
        while actual.siguiente != self.final:
            actual = actual.siguiente
        self.final = actual
        self.inicio = actual.siguiente


class LDobleLigada:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        return self.inicio is None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoDobleLista(dato)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo
        self.tamano += 1

    def insertar_final(self, dato):
        nuevo_nodo = NodoDobleLista(dato)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def insertar_por_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.tamano:
            print("Posición inválida")
            return
        if posicion == 0:
            self.insertar_inicio(dato)
        elif posicion == self.tamano:
            self.insertar_final(dato)
        else:
            nuevo_nodo = NodoDobleLista(dato)
            actual = self.inicio
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            self.tamano += 1

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.inicio.dato
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = None
        self.tamano -= 1
        return valor_eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.final.dato
        if self.inicio == self.final:
            self.inicio = None
            self.final = None
        else:
            self.final = self.final.anterior
            self.final.siguiente = None
        self.tamano -= 1
        return valor_eliminado

    def eliminar_por_posicion(self, posicion):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        if posicion < 0 or posicion >= self.tamano:
            print("Posición inválida")
            return
        if posicion == 0:
            return self.eliminar_inicio()
        elif posicion == self.tamano - 1:
            return self.eliminar_final()
        else:
            actual = self.inicio
            for _ in range(posicion):
                actual = actual.siguiente
            valor_eliminado = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamano -= 1
            return valor_eliminado

    def tamano_lista(self):
        return self.tamano

    def obtener_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.inicio.dato

    def obtener_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.final.dato

    def obtener_siguiente(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                if actual.siguiente:
                    return actual.siguiente.dato
                else:
                    return None
            actual = actual.siguiente
        print("El dato no está en la lista")
        return None

    def obtener_anterior(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    return actual.anterior.dato
                else:
                    return None
            actual = actual.siguiente
        print("El dato no está en la lista")
        return None

    def imprimir_lista(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def buscar_dato(self, dato):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
        return None


class LCircularDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def esta_vacia(self):
        return self.primero is None

    def insertar_inicio(self, dato):
        nuevo_nodo = NodoCircularDoble(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = self.ultimo
            self.primero.anterior = nuevo_nodo
            self.ultimo.siguiente = nuevo_nodo
            self.primero = nuevo_nodo
        self.tamano += 1

    def insertar_final(self, dato):
        nuevo_nodo = NodoCircularDoble(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = self.ultimo
            self.primero.anterior = nuevo_nodo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.tamano += 1

    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.primero.dato
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
        self.tamano -= 1
        return valor_eliminado

    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        valor_eliminado = self.ultimo.dato
        if self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        self.tamano -= 1
        return valor_eliminado

    def tamano_lista(self):
        return self.tamano

    def obtener_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.primero.dato

    def obtener_final(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        return self.ultimo.dato

    def imprimir_lista(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return
        actual = self.primero
        while True:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
            if actual == self.primero:
                break
        print()

    def buscar_dato(self, dato):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        actual = self.primero
        while True:
            if actual.dato == dato:
                return actual.dato
            actual = actual.siguiente
            if actual == self.primero:
                break
        return None

    def rotar_izquierda(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return
        self.primero = self.primero.siguiente
        self.ultimo = self.ultimo.siguiente

    def rotar_derecha(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return
        self.primero = self.primero.anterior
        self.ultimo = self.ultimo.anterior


class ABinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbolBinario(dato)
        else:
            self._insertar_recursivo(dato, self.raiz)

    def _insertar_recursivo(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbolBinario(dato)
            else:
                self._insertar_recursivo(dato, nodo.izquierda)
        elif dato > nodo.dato:
            if nodo.derecha is None:
                nodo.derecha = NodoArbolBinario(dato)
            else:
                self._insertar_recursivo(dato, nodo.derecha)
        else:
            print("El dato ya existe en el árbol")

    def buscar(self, dato):
        return self._buscar_recursivo(dato, self.raiz)

    def _buscar_recursivo(self, dato, nodo):
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        elif dato < nodo.dato:
            return self._buscar_recursivo(dato, nodo.izquierda)
        else:
            return self._buscar_recursivo(dato, nodo.derecha)

    def eliminar(self, dato):
        self.raiz = self._eliminar_recursivo(dato, self.raiz)

    def _eliminar_recursivo(self, dato, nodo):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(dato, nodo.izquierda)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(dato, nodo.derecha)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_min(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.dato, nodo.derecha)
        return nodo

    def _encontrar_min(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo.dato


class ABusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbolBusqueda(dato)
        else:
            self._insertar_recursivo(dato, self.raiz)

    def _insertar_recursivo(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbolBusqueda(dato)
            else:
                self._insertar_recursivo(dato, nodo.izquierda)
        elif dato > nodo.dato:
            if nodo.derecha is None:
                nodo.derecha = NodoArbolBusqueda(dato)
            else:
                self._insertar_recursivo(dato, nodo.derecha)
        else:
            print("El dato ya existe en el árbol")

    def buscar(self, dato):
        return self._buscar_recursivo(dato, self.raiz)

    def _buscar_recursivo(self, dato, nodo):
        if nodo is None:
            return False
        if dato == nodo.dato:
            return True
        elif dato < nodo.dato:
            return self._buscar_recursivo(dato, nodo.izquierda)
        else:
            return self._buscar_recursivo(dato, nodo.derecha)

    def eliminar(self, dato):
        if self.raiz is None:
            print("El árbol está vacío")
            return False
        else:
            self.raiz = self._eliminar_recursivo(dato, self.raiz)

    def _eliminar_recursivo(self, dato, nodo):
        if nodo is None:
            return nodo

        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(dato, nodo.izquierda)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(dato, nodo.derecha)
        else:
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp
            else:
                temp = self._encontrar_minimo(nodo.derecha)
                nodo.dato = temp.dato
                nodo.derecha = self._eliminar_recursivo(temp.dato, nodo.derecha)
        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual