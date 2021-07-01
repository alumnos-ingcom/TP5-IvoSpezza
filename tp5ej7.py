################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from ingreso_float import ingreso_float
    
def distancia(valor_a, valor_b):
    
    if valor_a > valor_b:
        valor_b = valor_b * -1
        
    elif valor_b > valor_a:
        valor_a = valor_a * -1
        
    distancia = valor_a + valor_b
    
    return distancia
    
def prueba():
    valor_a = ingreso_float("ingrese el primer valor")
    valor_b = ingreso_float("ingrese el segundo valor")
    
    distancia_entre = distancia(valor_a, valor_b)
    
    print(f"la distancia entre '{valor_a}' y '{valor_b}' es '{distancia_entre}'")
    
if __name__ == "__main__":
    prueba()

