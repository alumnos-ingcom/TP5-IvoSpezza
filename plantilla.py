################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
    
from ingreso_entero import ingreso_entero

    
def Codificador(texto, cantidad):
    
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
            
    palabra_codificada = "".join(armando_texto)
    
    return palabra_codificada
            

    
def Decodificador(texto,cantidad):
    
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
            
    palabra_codificada = "".join(armando_texto)
    
    return palabra_codificada


    
def prueba():
   
    texto = input("ingrese un texto ")
       
    nivel_codificado = ingreso_entero("nivel de codificado") 
    
    texto_codeado = Codificador(texto, nivel_codificado)
    
    print(texto_codeado)
    
    texto_otra_vez = Decodificador(texto_codeado, nivel_codificado)
    
    print(texto_otra_vez)
    
if __name__ == "__main__":
    prueba()

