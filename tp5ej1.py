################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from ingreso_entero import ingreso_entero

def par_o_impar(numero):
    
    while numero > 0:
        
        numero -= 2
        
    if numero == 0:
        
        return True
    
    else:
        return False
        

def prueba():
    
    numero = ingreso_entero("ingrese un numero entero ")
    
    verificador = par_o_impar(numero)
    
    if verificador:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
    
if __name__ == "__main__":
    prueba()
