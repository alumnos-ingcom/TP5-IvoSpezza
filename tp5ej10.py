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

def DesbinarioInador(binario_a_enteerizar):
    
    lista_del_binario = list(binario_a_enteerizar)
    
    comprobador = []
    
    lista_final = []
    
    for binn in lista_del_binario:
        
        comprobador.append(binn)
        
        if len(comprobador) == 8:
            
            binario = "".join(comprobador)
            
            if binario == "00110000":
            
                lista_final.append("0")
        
            elif binario == "00110001":
            
                lista_final.append("1")
            
            elif binario == "00110010":
            
                lista_final.append("2")
            
            elif binario == "00110011":
            
                lista_final.append("3")
            
            elif binario == "00110100":
            
                lista_final.append("4")
            
            elif binario == "00110101":
            
                lista_final.append("5")
            
            elif binario == "00110110":
            
                lista_final.append("6")
            
            elif binario == "00110111":
            
                lista_final.append("7")
            
            elif binario == "00111000":
            
                lista_final.append("8")
            
            elif binario == "00111001":
            
                lista_final.append("9")
            
            comprobador = []
            
            
    valor_final = "".join(lista_final)
    
    return valor_final
                         
def prueba():

    binario = BinarioInador(ingreso_entero("ingrese valor entero "))

    yanobinario = DesbinarioInador(binario)
    
    print(binario)
    
    print(yanobinario)
    
if __name__ == "__main__":
    prueba()

