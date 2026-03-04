def pesquisa_binaria(lista, item):
    inicio = 0 # início da lista
    final = len(lista) - 1 # final da lista

    while inicio <= final: # enquanto ainda não conseguiu chegar a um único elemento
        meio = (inicio + final) // 2 # verifica o elemento central
        chute = lista[meio]
        if chute == item: # se acha o item
            return meio
        if chute > item: # se o chute foi muito alto
            final = meio - 1
        else: # se o chute foi muito baixo
            inicio = meio + 1
    return None # se o item não existe

minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 3)) # o resultado é 1
print(pesquisa_binaria(minha_lista, -1)) # o resultado é None