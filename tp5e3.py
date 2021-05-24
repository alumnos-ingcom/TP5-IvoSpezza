################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def tribonaci(numero_de_la_sucecion):
    ultimo_valor = 1
    valor_del_medio = 1
    primer_valor = 1
    
    tribonaci = 1
    cuenta = 0
    
    
    
    while cuenta < 9:
        cuenta += 1
        
        ultimo_valor = valor_del_medio
        valor_del_medio = primer_valor
        primer_valor = tribonaci
        
        lista_de_prueba = [ultimo_valor, valor_del_medio, primer_valor]
        
        tribonaci = ultimo_valor + valor_del_medio + primer_valor
        print(lista_de_prueba)
    return tribonaci


def prueba():
    
    numero = tribonaci()
    print(f" el enesimo valor en la sucecion de tribonaci es '{numero}'")
    
if __name__ == "__main__":
    prueba()
