################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

import random

def texto_generator(cantidad_de_palabras):
    
    texto = [] 
    
    palabras = ["casa", "lugar", "verde", "rojo", "caminando", "explorar", "patio", "calle","sistema","auto",
                "color","azul","juguete","jamon","gato","queso","para","que","supuestamente", "nunca","sera","siempre"]
    
    conectores = ["de", "el", "la", "en", "por", "es", "sera", "sos", "la", "tu", "mi",
                   "del","que","nosotros","ellos","vos","para", "cuando","nunca"]
    
    cantidad_de_palabras -= 1
    
    color = 0
    
    while cantidad_de_palabras > 0:
        
        color = random.randint(32,36)
        
        texto.append(f"\x1b[0;{color}m{palabras[random.randint(-22,21)]}\x1b[0;37m")
        
        texto.append(f"\x1b[0;{color}m{conectores[random.randint(-19,18)]}\x1b[0;37m")
        
        cantidad_de_palabras -= 1
        
    texto.append(f"\x1b[0;{color}m{palabras[random.randint(-22,21)]}\x1b[0;37m")
    
    texto_final = " ".join(texto)
    
    return texto_final

def busca_palabra(texto, palabra_a_buscar):
    
    lista_de_palabras = texto.split(" ")
    
    pocicion = 0
    
    for lugar,palabra in enumerate(lista_de_palabras):
        
        
        if palabra_a_buscar == palabra:
            
            pocicion = lugar + 1
            
            break
    
    return pocicion
    
def prueba():
   
    texto = texto_generator(random.randint(1,10))
    
    print(f"{texto} \n")
    
    palabra = input("que palabra del texto desea buscar? \n")
    
    posicion = busca_palabra(texto, palabra)
    
    if posicion != -1:
        
        print(f"esa palabra se encuentra en el lugar '{posicion}'")
    
    else:
        
        print("la palabra no pertenece al texto")

if __name__ == "__main__":
    prueba()

