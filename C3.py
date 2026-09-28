nums = ['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']
colors = ['Rojo','Azul','Verde','Naranja','Amarillo','Morado','Rosa','Blanco','Negro','Cafe']

print(nums)
#colors.append('Magenta')   #Agrega a la lista
#colors.extend(['Violeta','Gris']) agregar mas de 1 elemento
#colors.insert(0,'Violeta') Agrega un elemento y lo posiciona empujando/acomodando los demas
#colors.clear()  Limpia o borra la lista
#print(colors.pop(9))    #Muestra el elemento que extrajo de la lista y si imprimes de nuevo la lista ya no aparece
#colors.sort(reverse=False)  #Ordena en orden alfabetico a/z (true) y de forma z/a (false) 
#colors.reverse()    #Ordena de forma alfabetica
#colors_1 = colors.copy()    #Copia superficial de una lista
#print(colors_1)
print(colors)
"""Ejemplo"""

"""for num in nums:
    output = f"[{num}, {colors[nums.index(num)]}]"
    print(output)"""
print([nums[0], colors[0]])