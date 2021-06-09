################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

import random

def TextoGenerator(cantidad_de_palabras):
    
    texto = [] 
    
    palabras = ["casa", "lugar", "verde", "rojo", "caminando", "explorar", "patio", "calle","sistema","auto","color"]
    
    conectores = ["de", "el", "la", "en", "por", "es", "sera", "sos", "la", "tu", "mi", "depende de"]
    
    cantidad_de_palabras -= 1
    
    while cantidad_de_palabras > 0:
        
        texto.append(palabras[random.randint(-11,10)])
        
        texto.append(conectores[random.randint(-12,11)])
        
        cantidad_de_palabras -= 1
        
    texto.append(palabras[random.randint(-11,10)])
    
    texto_final = " ".join(texto)
    
    return texto_final

def BuscaPalabra(texto):

    palabra_a_buscar = input("que palabra del texto desea buscar? \n")
    
    creo = texto.find(palabra_a_buscar)
    
    return creo
    
def prueba():
   
    texto = TextoGenerator(random.randint(1,10))
    
    print(f"{texto} \n")
    
    posicion = BuscaPalabra(texto)
    
    if posicion != -1:
        
        print(f"esa palabra se encuentra en el lugar '{posicion}'")
    
    else:
        
        print("la palabra no pertenece al texto")

if __name__ == "__main__":
    prueba()

