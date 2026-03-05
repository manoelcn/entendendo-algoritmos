def buscar_menor(array):
    menor_valor = array[0] # assume que o primeiro elemento é o menor
    menor_indice = 0 # armazena o índice do menor valor
    for i in range(1, len(array)): # percorre o array do segundo elemento em diante
        if array[i] < menor_valor: # se encontrar algo menor
            menor_valor = array[i] # atualiza o menor valor
            menor_indice = i # salva sua posição
    return menor_indice # retorna a posição, não o valor

def ordenacao_por_selecao(array):
    novo_array = []
    for i in range(len(array)):
        menor_elemento = buscar_menor(array) # acha a posição do menor
        novo_array.append(array.pop(menor_elemento)) # # remove do original e adiciona ao novo array
    return novo_array

print(ordenacao_por_selecao([5, 3, 6, 10, 2]))