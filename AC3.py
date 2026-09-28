nums = ['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']
colors = ['Rojo','Azul','Verde','Naranja','Amarillo','Morado','Rosa','Blanco','Negro','Cafe']

listnew=[]
nums.reverse()
for num in nums:
    output = f"[{num}, {colors[nums.index(num)]}]"
    listnew.append(output)
print(listnew)  