################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from ingreso_entero import ingreso_entero

def Capicua(numero):
    
    lista = list(str(numero))
    
    lista_inversa = []
    
    cantidad_de_valores = 0
    
    for valor in lista:
        
        cantidad_de_valores -= 1
        
        lista_inversa.append(lista[cantidad_de_valores])
    
    numero_inverso = "".join(lista_inversa)
    
    numero_inverso = int(numero_inverso)
    
    if numero_inverso == numero:
        
        return True
    
    elif numero_inverso != numero:
        
        return False
    
def prueba():

    numero = ingreso_entero("ingrese un numero")
    
    capicua = Capicua(numero)
    
    if capicua:
        
        print(f"el numero '{numero}' es capicua")
    
    elif not capicua:
        
        print(f"el numero '{numero}' no es capicua")
        
if __name__ == "__main__":
    prueba()

