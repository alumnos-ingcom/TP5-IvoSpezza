################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio



import random


def PromedioLista(lista):
    
    promedio_final = 0
    
    promedio = 0
    
    for numero in lista:
        
        promedio_final += numero
        
        promedio += 1
        
    promedio_final = float(promedio_final)
    
    promedio_final = promedio_final / promedio
    
    
    return promedio_final
    
    
def RandomLista(cantidad_de_valores):

    lista = []
    
    while cantidad_de_valores > 0:
        
        lista.append(random.randint(1,10))
        
        cantidad_de_valores -= 1
        
    return lista


def prueba():

    cantidad = random.randint(1,20)

    lista = RandomLista(cantidad)

    promedio = PromedioLista(lista)
    
    print(promedio)

if __name__ == "__main__":
    prueba()

