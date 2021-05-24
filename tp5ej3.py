################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from ingreso_entero import ingreso_entero

def tribonaci(numero_de_la_sucecion):
    
    ultimo_valor = 1
    valor_del_medio = 1
    primer_valor = 1
    
    tribonaci = 1
    cuenta = 0
    
    
    
    while cuenta < numero_de_la_sucecion:
        cuenta += 1
        
        ultimo_valor = valor_del_medio
        valor_del_medio = primer_valor
        primer_valor = tribonaci
        
        lista_de_prueba = [ultimo_valor, valor_del_medio, primer_valor]
        
        tribonaci = ultimo_valor + valor_del_medio + primer_valor
        print(lista_de_prueba)
    return tribonaci


def prueba():
    
    cantidad = ingreso_entero("ingrese la cantidad de veces que se va a ejecutar tribonaci")
    numero = tribonaci(cantidad)
    print(f"el valor tras ejecutar tribonaci {cantidad} veces es '{numero}'")
    
if __name__ == "__main__":
    prueba()
