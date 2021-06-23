################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

# import rhinoscriptsytnax as rs

import random

def texto_generator(cantidad_de_palabras):
    
    texto = [] 
    
    palabras = ["casa", "lugar", "verde", "rojo", "caminando", "explorar", "patio", "calle","sistema","auto",
                "color","azul","juguete","jamon","gato","queso","para","que","supuestamente", "nunca","sera","siempre"]
    
    conectores = ["de", "el", "la", "en", "por", "es", "sera", "sos", "la", "tu", "mi",
                   "del","que","nosotros","ellos","vos","para", "cuando","nunca"]
    
    cantidad_de_palabras -= 1
    
    while cantidad_de_palabras > 0:
        
        texto.append(f"{palabras[random.randint(-22,21)]}")
        
        texto.append(f"{conectores[random.randint(-19,18)]}")
        
        cantidad_de_palabras -= 1
        
    texto.append(f"{palabras[random.randint(-22,21)]}")
    
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
    
    
def convierte_a_color(texto):
    
    lista_de_texto = texto.split(" ")
    
    texto_color = []
        
    for palabra in lista_de_texto:
        
        estilo = random.randint(1,9)
                    
        letra_color = random.randint(31,36)
                      
        fondo_color = random.randint(41,46)
            
        texto_color.append(f"\x1b[{estilo};{letra_color};{fondo_color}m"+f"{palabra}"+"\x1b[0m")

    texto_color = f"\x1b[{estilo};{letra_color};{fondo_color}m \x1b[0m".join(texto_color)
    
    return texto_color

def prueba():
   
    texto = texto_generator(100)
    
    print(f"{texto} \n")
    
    texto_a_color = convierte_a_color(texto)
    
    print(texto_a_color)
    
#     palabra = input("que palabra del texto desea buscar? \n")
#     
#     posicion = busca_palabra(texto, palabra)
#     
#     if posicion != -1:
#         
#         print(f"esa palabra se encuentra en el lugar '{posicion}'")
#     
#     else:
#         
#         print("la palabra no pertenece al texto")

    

if __name__ == "__main__":
    prueba()

