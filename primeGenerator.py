# Programa en Python para generar lista de numeros pares dentro de un limite
# Link de Teoria: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# El programa elimina cada 2o numero a partior del 2, cada 3ero a partir del 3, 
# cada 5o apartir del 5 y cada 7imo a partir del 7

lim = 100
# Crea una lista con todos los numeros del rango
nums = [i for i in range(1, lim)]
# Cambia el primer valor a 0
nums[0] = 0

# Contadores para incrementar el salto
c = 2
c2 = 1

while c < 8:                                    # Ciclo para identificar primos                                
    for i in range(c-1, len(nums), c):          # Recorre toda la lista, saltando con un valor de C para
                                                # cambiar todos los numeros pares a 0
        if nums[i] != c:                        # Cambia los numeros pares a 0
            nums[i] = 0
    # Cambia valor de C
    c += c2
    c2 = 2

# Quita todos los 0s de la lista
nums = list(filter((0).__ne__, nums))
#print(nums)
