import random

def OrdenarLista(A1,A2):
    #Este codigo tiene como funcion ordenar una lista aleatoria de acuerdo a otra lista que  poroporcionaré
    merged_A=[]#Estoy inicializando una nueva lista donde colocaré mis valores
    
    for num in A2:#Voy a recorrer cada valor de Mi lista A2 con num
        for j in range(len(A1)): #vpy a asignarle a j valores de posición de una lista llamada  A1
            if A1[j]==num:#  si los valores de posición de A1 coinciden con numeros de A2 almacenarlos
                merged_A.append(A1[j])#Voy a almacenar en una nueva lista
    #A2_fil=list(set(A2)) #convierte A2 en una lista y almacena los elementos sin duplicados
    A1_filtered=sorted([x for x in A1 if x not in A2])#va aordenar los elementos que no se encuentran en A2
    return merged_A+A1_filtered
        

    # Filtrar los elementos nulos y ordenar los restantes de A1
    
                    
                
A1=[random.randint(1,10)for _ in range(8)]#voy a escoger 8 cifras del 1 al 10 para ordenar

A2=[random.randint(1,10)for _ in range(8)]#[8,7,9,10,5,6]
print(A1)
print(A2)
resultado=OrdenarLista(A1, A2)

print("Ordenado",resultado)
