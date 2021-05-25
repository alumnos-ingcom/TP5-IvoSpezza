################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def ingreso_entero(mensaje):
    validante = True
    print(mensaje)
    while validante:
        try:
            numero = int(input())
            validante = False
        except ValueError:
            print(f"error, por favor {mensaje}")
    return numero
def prueba():
    
    numero = ingreso_entero("ingresa un numero ")
    
    print(numero)
    
if __name__ == "__main__":
    prueba()
