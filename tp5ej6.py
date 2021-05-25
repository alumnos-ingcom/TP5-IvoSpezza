################
# Ivo Spezzacatena - @ivospezza
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
    
def CadenaDeParentesis(cadena):
    
    prueba = list(cadena)
    
    for i in prueba:
        
        if i != "[" and i != "]" and i != "}" and i != "{" and i!= "(" and i != ")":
            raise NameError('no ingresaste parentesis')
        
  
    parentesis ="".join(prueba)
    return parentesis

def Balanceo(cadena_de_parentesis):

    testeo = list(cadena_de_parentesis)
  
    valor=0
    
    for i in testeo:
        valor += 1
        
    valor -= 1
    
    if testeo[0] == "]" or testeo[0] == "}" or testeo[0] == ")":
        return "cadena no balanceada"
    
    elif testeo[valor] == "[" or testeo[valor] == "{" or testeo[valor] == "(":
        return "cadena no balanceada"
    
    conteo = 0
    
    while conteo < valor:
        if testeo[conteo] == testeo[conteo + 1]:
            
        conteo += 1
    

def prueba():
    
    cadena = input("increse SOLO paretesis ")
    cadena = CadenaDeParentesis(cadena)
    
    casa = Balanceo(cadena)
    print(f"'{cadena}' {casa}")
  
    
    
if __name__ == "__main__":
    prueba()

