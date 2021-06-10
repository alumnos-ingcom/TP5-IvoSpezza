################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
    
from ingreso_entero import ingreso_entero

    
def codificador(texto, cantidad):
    
    cantidad = abs(cantidad)
    
    texto_ingresado = list(texto)
    
    armando_texto = []
    
    
    
    if cantidad > 26:
        
        while cantidad > 26:
            cantidad -= 26
            
    minus = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    mayus = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    pocicion = 0
    
    pocicion_final = 0
    
    for letra in texto_ingresado:
        
        if letra.islower():
           
            pocicion = minus.index(letra)
            pocicion_final = pocicion + cantidad 
            armando_texto.append(minus[pocicion_final])
            
        elif letra.isupper():
            pocicion = mayus.index(letra)
            pocicion_final = pocicion + cantidad 
            armando_texto.append(mayus[pocicion_final])
            
        elif letra == " ":
            armando_texto.append(" ")
            
        elif letra.isdigit():
        
            letra = int(letra)
            letra = letra + cantidad
            
            while letra > 9:
                letra -= 10
            letra = str(letra)
            armando_texto.append(letra)
            
        else:
            armando_texto.append(letra)
            
    palabra_codificada = "".join(armando_texto)
    
    return palabra_codificada
            

    
def decodificador(texto,cantidad):
    
    cantidad = abs(cantidad)
    
    texto_ingresado = list(texto)
    
    armando_texto = []
    
    
    
    if cantidad > 26:
        
        while cantidad > 26:
            cantidad -= 26
            
    minus = list("zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba")
    mayus = list("ZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBA")
    
    pocicion = 0
    
    pocicion_final = 0
    
    for letra in texto_ingresado:
        
        if letra.islower():
           
            pocicion = minus.index(letra)
            pocicion_final = pocicion + cantidad 
            armando_texto.append(minus[pocicion_final])
            
        elif letra.isupper():
            pocicion = mayus.index(letra)
            pocicion_final = pocicion + cantidad 
            armando_texto.append(mayus[pocicion_final])
            
        elif letra == " ":
            armando_texto.append(" ")
        
        elif letra.isdigit():
        
            letra = int(letra)
            letra = letra - cantidad
            while letra < 0:
                letra += 10
            letra = str(letra)
            armando_texto.append(letra)
        
        else:
            armando_texto.append(letra)
            
    palabra_codificada = "".join(armando_texto)
    
    return palabra_codificada


    
def prueba():
   
    texto = input("ingrese un texto ")
       
    nivel_codificado = ingreso_entero("nivel de codificado") 
    
    texto_codeado = codificador(texto, nivel_codificado)
    
    print(texto_codeado)
    
    texto_otra_vez = decodificador(texto_codeado, nivel_codificado)
    
    print(texto_otra_vez)
    
if __name__ == "__main__":
    prueba()

