################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def ingreso_float(mensaje):
    validante = True
    print(mensaje)
    while validante:
        try:
            numero = float(input())
            validante = False
        except ValueError:
            print(f"error, por favor {mensaje}")
    return numero
def prueba():
    
    numero = ingreso_float("ingresa un numero ")
    
    print(numero)
    
if __name__ == "__main__":
    prueba()
