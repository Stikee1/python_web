lista_datos=[14,26,39,25,11,18,42,39,17,23]
dato_buscado=31

def busqueda_secuencial(lista, objetivo):
    for elemento in lista:
        if elemento==objetivo: 
            return True
def busqueda_binaria(lista, objetivo):
    pass

if busqueda_secuencial(lista_datos, dato_buscado):
    print ("Dato encontrado")
else:
    print("Dato no encontrado")