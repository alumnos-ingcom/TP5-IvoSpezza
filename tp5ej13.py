################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

import random

def TextoGenerator(cantidad_de_palabras):
    
    texto = [] 
    
    palabras = ["casa", "lugar", "verde", "rojo", "caminando", "explorar", "patio", "calle","sistema","auto","color"]
    
    conectores = ["de", "el", "la", "en", "por", "es", "sera", "sos", "la", "tu", "mi"]
    
    cantidad_de_palabras -= 1
    
    while cantidad_de_palabras > 0:
        
        texto.append(palabras[random.randint(-11,10)])
        
        texto.append(conectores[random.randint(-11,10)])
        
        cantidad_de_palabras -= 1
        
    texto.append(palabras[random.randint(-11,10)])
    
    texto_final = " ".join(texto)
    
    return texto_final

def BuscaPalabra(texto):

    pass

def prueba():
   
    texto = TextoGenerator(random.randint(1,10))

    print(texto)

if __name__ == "__main__":
    prueba()

