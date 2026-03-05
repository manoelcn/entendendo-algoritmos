# Ordenação por seleção

## Como funciona a memória

Podemos imaginar a memória do computador como um grande conjunto de gavetas, onde cada gaveta possui um **endereço**.

Sempre que queremos armazenar um item na memória, solicitamos um espaço ao computador, e ele retorna um endereço onde esse item poderá ser guardado.

Portanto, uma forma simples de entender a memória é **imaginá-la como um grande conjunto de gavetas endereçadas**.

---

## Arrays e listas encadeadas

Muitas vezes precisamos armazenar uma **lista de elementos** na memória. Nesse caso, duas estruturas de dados são comuns:

- **Arrays**
- **Listas encadeadas**

Cada uma possui _características diferentes_.

---

### Arrays

Em um **array**, todos os elementos são armazenados em _posições consecutivas da memória_.

Isso permite acessar qualquer elemento diretamente através do seu índice.

**Vantagens**

- Acesso rápido a qualquer elemento

**Desvantagens**

- Inserções podem ser lentas
- Remoções também podem exigir deslocamentos de elementos, ou seja, também podem ser lentas

Isso acontece porque, ao inserir um elemento no meio de um array, pode ser necessário **mover todos os outros elementos seguintes**.

---

### Listas encadeadas

Em uma **lista encadeada**, os elementos podem estar em _qualquer lugar da memória_. Cada elemento da lista armazena **o valor do elemento** e **o endereço do próximo elemento**.

Ou seja, os elementos não precisam estar em posições consecutivas de memória.

**Vantagens**

- Inserções rápidas
- Remoções rápidas

**Desvantagens**

- Acesso lento a elementos específicos
- Para acessar um item no meio da lista, é necessário percorrer os elementos anteriores

Portanto, listas encadeadas são eficientes quando precisamos **inserir ou remover muitos elementos**.

---

## Ordenação por seleção

Agora vamos entender o algoritmo **Ordenação por Seleção**.

Imagine que você tenha uma lista de artistas no seu computador. Cada artista possui um contador de plays, ou seja, quantas vezes suas músicas foram reproduzidas.

Você deseja _ordenar os artistas do mais ouvido para o menos ouvido_.

### Como podemos fazer isso?

Uma forma simples seria:

1. Encontrar o artista com mais reproduções
2. Adicionar ele a uma nova lista
3. Remover ele da lista original
4. Repetir o processo com os elementos restantes

Se continuarmos fazendo isso até que a lista original fique vazia, teremos **uma nova lista completamente ordenada**.

Esse processo é chamado de **ordenação por seleção**.

---

## Para que isso serve?

Algoritmos de ordenação são **extremamente úteis** na computação.

Eles podem ser usados para ordenar:

- nomes em uma agenda telefônica
- datas de viagens
- emails do mais recente para o mais antigo
- produtos por preço
- resultados por pontuação
- entre outros

---

## Implementação

Veja um exemplo de implementação do algoritmo em Python no arquivo `ordenacao_por_selecao.py`.