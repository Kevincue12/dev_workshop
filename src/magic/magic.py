class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
            raise ValueError("El índice de Fibonacci no puede ser negativo")
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        fibonacci = [0, 1]
        for _ in range(2, n):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
        return fibonacci
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        if n < 2:
            return []

        primos = []
        for num in range(2, n + 1):
            es_primo = True
            for div in range(2, int(num ** 0.5) + 1):
                if num % div == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)

        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False  # No hay números perfectos menores que 2

        suma_divisores = sum([i for i in range(1, n) if n % i == 0])
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas <= 0:
            return []

        triangulo = [[1]]  # Primera fila siempre es [1]

        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]  # El primer elemento siempre es 1
            
            # Calcular los elementos intermedios
            for j in range(1, len(fila_anterior)):
                nueva_fila.append(fila_anterior[j - 1] + fila_anterior[j])
            
            nueva_fila.append(1)  # El último elemento siempre es 1
            triangulo.append(nueva_fila)

        return triangulo

    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i

        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
            return 0  
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(digito) for digito in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        digitos = str(n)
        num_digitos = len(digitos)
        suma = sum(int(d)**num_digitos for d in digitos)
        
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        filas = len(matriz)
        for fila in matriz:
            if len(fila) != filas:
                return False  
            
        suma_esperada = sum(matriz[0])
    
        for fila in matriz:
            if sum(fila) != suma_esperada:
                return False  
            
        for i in range(filas):
            suma_columna = sum(matriz[j][i] for j in range(filas))
            if suma_columna != suma_esperada:
                return False 
            
        suma_diagonal_principal = sum(matriz[i][i] for i in range(filas))
        suma_diagonal_secundaria = sum(matriz[i][filas - 1 - i] for i in range(filas))
        
        if suma_diagonal_principal != suma_esperada or suma_diagonal_secundaria != suma_esperada:
            return False  
        
        return True