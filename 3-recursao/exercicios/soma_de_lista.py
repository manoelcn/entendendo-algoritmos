def soma_de_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        elemento = (lista.pop(len(lista) - 1))
        return elemento + soma_de_lista(lista)
    

print(soma_de_lista([1, 2, 3, 4, ]))