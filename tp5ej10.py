################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from ingreso_entero import ingreso_entero

def binario_inador(numero_a_binarisar):
    
    numero_a_dividir = numero_a_binarisar
    
    binario = []
    
    while numero_a_dividir >= 1:
        
        resto = numero_a_dividir
        
        numero_a_dividir = numero_a_dividir / 2
        
        numero_a_dividir = int(numero_a_dividir)
        
        while resto >= 1:
            
            resto -= 2
            
            if resto == 0:
                
                binario.append("0")
                
            elif resto == -1:
                
                binario.append("1")
    
    binario.reverse()
    
    binario = "".join(binario)
    
    return binario




def desbinario_inador(binario_a_enteerizar):
    
    
    binario = list(binario_a_enteerizar)
    
    
    entero = 1
    
    salto = True
    
    for numero in binario:
            
        if salto:
            
            salto = False
            
        else:
            
            entero = (entero * 2) + int(numero)
    
    return entero
                         
def prueba():

    binario = binario_inador(ingreso_entero("ingrese valor entero "))

    yanobinario = desbinario_inador(binario)
    
    print(binario)
    
    print(yanobinario)
    
if __name__ == "__main__":
    prueba()

