class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_invertida = []
        for i in range(len(lista) - 1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):  
            if lista[i] == elemento:
                return i  
        return -1  
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        lista_sin_duplicados = []
        seen = set()  

        for elemento in lista:
            clave = (elemento, type(elemento))  
            if clave not in seen:
                lista_sin_duplicados.append(elemento)
                seen.add(clave)  

        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        if not isinstance(lista1, list) or not isinstance(lista2, list):
            raise TypeError("Ambos argumentos deben ser listas")
    
        resultado = []
        i, j = 0, 0
        len1, len2 = len(lista1), len(lista2)  

        while i < len1 and j < len2:
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])

        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not isinstance(lista, list) or not isinstance(k, int):
            raise TypeError("Los argumentos deben ser una lista y un entero")
    
        if not lista:
            return lista  
    
        k = k % len(lista)  
        return lista[-k:] + lista[:-k]  
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        if not lista:
            raise ValueError("La lista no puede estar vacía")

        n = len(lista) + 1  
        suma_esperada = (n * (n + 1)) // 2  
        suma_real = sum(lista)  

        return suma_esperada - suma_real  
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []

        def push(elemento):
            """ Agrega un elemento a la pila """
            pila.append(elemento)

        def pop():
            """ Elimina y devuelve el último elemento de la pila (LIFO) """
            return pila.pop() if not is_empty() else None

        def peek():
            """ Devuelve el último elemento de la pila sin eliminarlo """
            return pila[-1] if not is_empty() else None

        def is_empty():
            """ Verifica si la pila está vacía """
            return len(pila) == 0

        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []

        def enqueue(elemento):
            """ Agrega un elemento al final de la cola """
            cola.append(elemento)

        def dequeue():
            """ Elimina y devuelve el primer elemento de la cola (FIFO) """
            return cola.pop(0) if not is_empty() else None

        def peek():
            """ Devuelve el primer elemento de la cola sin eliminarlo """
            return cola[0] if not is_empty() else None

        def is_empty():
            """ Verifica si la cola está vacía """
            return len(cola) == 0

        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz:  # Verifica si la matriz está vacía
            return []
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]