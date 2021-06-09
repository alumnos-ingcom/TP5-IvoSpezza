################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from ingreso_entero import ingreso_entero

def GeneraListas(cantidad_de_valores, numero_de_lista):
    
    lista = []
    
    while cantidad_de_valores > 0:
        
        lista.append(input(f"ingrese contenido para la lista {numero_de_lista}\n"))
        
        cantidad_de_valores -= 1
    
    return lista

def ComparaListas(lista_a, lista_b):
    
    contenido_compartido = True
    
    for contenido in lista_a:
        
        contenido = str(contenido)
        
        try:
        
            lista_b.index(contenido)
            
            contenido_compartido = True
    
    
        except ValueError:
            
            contenido_compartido = False
            
            break
            
    return contenido_compartido
    

def prueba():
   
    cantidad_de_valores = ingreso_entero("cuantos valores quiere en sus listas?")
    
    lista1 = GeneraListas(cantidad_de_valores,1)
    lista2 = GeneraListas(cantidad_de_valores,2)
    
    tienen_lo_mismo = ComparaListas(lista1, lista2)
    
    if tienen_lo_mismo:
        
        print(f"la lista {lista1} y la lista {lista2} poseen el mismo contenido")
        
    elif not tienen_lo_mismo:
        
        print(f"la lista {lista1} y la lista {lista2} no comparten el contenido")


if __name__ == "__main__":
    prueba()

