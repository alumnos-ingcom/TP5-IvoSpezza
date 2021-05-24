################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio



from ingreso_entero import ingreso_entero

def numero_perfecto(numero):
    
    numero_perfecto = 0
    lista_resultante = []
        
    divisor= 0
    while divisor < numero:
        divisor += 1
        copia = numero
        
        while copia > 0:
            copia -= divisor
            
            if copia == 0:
                
                if divisor == numero:
                    pass
            
                else:
                    lista_resultante.append(divisor)
            
    for i in lista_resultante:
        
        numero_perfecto += i
    
    if numero_perfecto == numero:
         
        return True
        
    else:
        return False
    


def prueba():
    
    numero = ingreso_entero("ingrese un numero entero positivo")
    
    verificador = numero_perfecto(numero)
    
    if verificador:
    
        print(f"'{numero}' es un numero perfecto")
    
    else:
        
        print(f"'{numero}' no es un numero perfecto")

if __name__ == "__main__":
    prueba()