network_config2={
    "0001":{
        "ip":"192.168.0.2",
        "device":"Switch",
        "policity":"Deny All",
        "status": False,
        "lista":[1,2,3,4,5,6]
    },
    "0002":{
            "ip":"192.168.0.1",
            "device":"Firewall",
            "policity":"Avoid .2 .3 .4",
            "status": True
        },
    "0003":{
        "ip":"192.168.0.3",
        "device":"Router",
        "policity":"Avoid .1",
        "status": True
        },
    "0004":{
            "ip":"192.168.0.4",
            "device":"Acces point",
            "policity":"Avoid.3",
            "status": False
        },
    "0005":{
            "ip":"192.168.0.5",
            "device":"Server",
            "policity":"Allow All",
            "status": True
        }
}
contenido = network_config2.get("0001")
lista_A = contenido.get('lista')
num = lista_A[2]
print(num)

#yaEnUso = lista_A.pop(2)
#print(num)

network_config2['0006']={"ip":1

}
print(network_config2)
#print(network_config2.get("0001").get("lista")[2])
      #Obtener elementos de una seccion con .get y cierta parte de una lista con [] 
      #[listas] {Diccionarios}
#Cualquier tipo de clave puede ser ocupada por cualquier valor

