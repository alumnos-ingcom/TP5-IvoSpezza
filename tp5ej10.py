################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from ingreso_entero import ingreso_entero

def BinarioInador(numero_a_binarisar):
    
    lista_para_binario = list(str(numero_a_binarisar))
    
    lista_binaria = []
    
    
    
    for num in lista_para_binario:
        
        num = int(num)
        
        if num == 0:
            
            lista_binaria.append("00110000")
        
        elif num == 1:
            
            lista_binaria.append("00110001")
            
        elif num == 2:
            
            lista_binaria.append("00110010")
            
        elif num == 3:
            
            lista_binaria.append("00110011")
            
        elif num == 4:
            
            lista_binaria.append("00110100")
            
        elif num == 5:
            
            lista_binaria.append("00110101")
            
        elif num == 6:
            
            lista_binaria.append("00110110")
            
        elif num == 7:
            
            lista_binaria.append("00110111")
            
        elif num == 8:
            
            lista_binaria.append("00111000")
            
        elif num == 9:
            
            lista_binaria.append("00111001")
    
    valor_binario_final = "".join(lista_binaria)
    
    return valor_binario_final

def DesbinarioInador(binaro_a_enteerizar):
    

    pass

def prueba():

    binario = BinarioInador(ingreso_entero("ingrese valor entero "))

    print(binario)
    
if __name__ == "__main__":
    prueba()

