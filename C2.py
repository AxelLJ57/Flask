week = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
out=[]  #Lista vacia
for i, day in enumerate (week): #i = [0,Lunes]
    if day=='Sabado' or day=='Domingo':     #Hace la comparacion hasta la iteracion 5 que es sabado
        out.append(i)       #Una vez que hace la iteracion hace a out=[5], como domingo si entra en la iteracion lo agrega a la lista out=[5,6]
print(out)      #Lo imprime en la pantalla
        