################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
    
    
def PalabraInador(palabra): 
    
    palabra_separada = list(palabra)
    
    palabra_separada_cambiada = []
    
    for letra in palabra_separada:
        
        if letra.islower():
            
            letra_cambiada = letra.upper()
            
            palabra_separada_cambiada.append(letra_cambiada)
            
        elif letra.isupper():
            
            letra_cambiada = letra.lower()
            
            palabra_separada_cambiada.append(letra_cambiada)
        
        else:
            palabra_separada_cambiada.append(letra)
    
    cambio_listo = "".join(palabra_separada_cambiada)
   
    return cambio_listo
    
def prueba():
    
    palabra = PalabraInador(input("ingrese una palabra "))
    
    print(palabra)

if __name__ == "__main__":
    prueba()

