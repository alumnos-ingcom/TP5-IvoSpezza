################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def busca_factoriones():
    
    lista_de_i = []
    
    lista_de_factoriones = []
    
    for numero in range(1500000):
        
        numero += 1
        
        valor_final = 0
        
        if numero >= 1:
            
            lista_del_numero = list(str(numero))
            
            for valor in lista_del_numero:
                
                conteo = 0
                factor = 1
                
                valor = int(valor)
                
                while conteo < valor:
                    
                    conteo += 1
                    
                    factor = factor * conteo
                    
                valor_final = valor_final + factor
        
        if numero == valor_final:
            
            lista_de_factoriones.append(numero)
            
    return lista_de_factoriones
            
    
    
def prueba():
    
    factoriones = busca_factoriones()
    
    print(factoriones)
    
    
if __name__ == "__main__":
    prueba()

