################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from ingreso_entero import ingreso_entero

def fibonaci(numero_de_la_sucecion):
    
    ultimo_valor = 1
    primer_valor = 1
    
    fibonaci = 1
    cuenta = 0
    
    
    
    while cuenta < numero_de_la_sucecion:
        cuenta += 1
        
        ultimo_valor = primer_valor
        primer_valor = fibonaci
        
        lista_de_prueba = [ultimo_valor, primer_valor]
        
        fibonaci = ultimo_valor + primer_valor
        print(lista_de_prueba)
    return fibonaci


def prueba():
    
    cantidad = ingreso_entero("ingrese la cantidad de veces que se va a ejecutar fibonaci")
    numero = fibonaci(cantidad)
    print(f"el valor tras ejecutar fibonaci {cantidad} veces es '{numero}'")
    
if __name__ == "__main__":
    prueba()
