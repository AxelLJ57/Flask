def funcion1():
    lista = []

    
    for i in range(5):
        elemento = (i+1)
        lista.append(elemento)

    return lista

lista = funcion1()
print(lista)


def funcion2():
    diccionario={}

    dias=['lunes','marter','miercoles']

    for i in range(3):
        diccionario[i]=dias[i]
        print(diccionario)    

funcion2()