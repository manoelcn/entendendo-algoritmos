# Pesquisa binária

Antes de entendermos a pesquisa binária, precisamos compreender o conceito de **algoritmo**.

Segundo Aditya Bhargava, um *algoritmo* é um **conjunto de instruções que realizam uma tarefa**.

---

## Para que servem pesquisas binárias?

A pesquisa binária é usada para encontrar um elemento em uma lista ordenada de forma **eficiente**.

Por exemplo, quero encontrar um nome que começa com a letra _P_ em uma lista telefônica.  
Se eu começar da letra _A_, posso levar muito tempo até chegar à letra desejada.

Uma estratégia melhor é abrir a lista na metade.  
Se a página aberta estiver antes da letra _P_, sei que devo procurar na metade direita.  
Se estiver depois, devo procurar na metade esquerda.

A cada passo, **elimino metade das possibilidades**.

---

## Definição

A **pesquisa binária** é um algoritmo que:

- Recebe como entrada uma **lista ordenada**
- Recebe um **valor alvo**
- Retorna o **índice do elemento**, se ele existir
- Caso contrário, retorna `None` ou outro valor que indique ausência.

Importante:  
A lista **precisa estar ordenada**. Caso contrário, o algoritmo não funciona corretamente.

---

## Pesquisa simples

Imagine que estou pensando em um número de 1 a 100 e você precisa adivinhar qual é.

Se você começar pelo 1 e for aumentando de 1 em 1:

Você: 1 --> Muito baixo  
Você: 2 --> Muito baixo  
Você: 3 --> Muito baixo  
...

Se o número for 99, você precisará de 99 tentativas.


Esse, com certeza, é um método ruim de acertar o número. Esse método se chama de _pesquisa simples_. Ou seja, no pior caso, precisamos testar todos os elementos

---

## Uma maneira melhor de buscar

Agora imagine o mesmo desafio, mas usando pesquisa binária.

Estou pensando no número 63.

1. Você começa pelo 50  
   --> Muito baixo  
   Eliminamos 1 até 50  

2. Você tenta 75  
   --> Muito alto  
   Eliminamos 75 até 100  

Perceba o padrão:  
A cada tentativa, eliminamos **metade** dos números restantes.

>**Isso é o que torna a pesquisa binária tão eficiente.**

No intervalo de 1 a 100:

100 --> 50 --> 25 --> 13 --> 7 --> 4 --> 2 --> 1

São necessárias no máximo **7 etapas**.


Nesse exemplo do 1 ao 100, seja qual for o número que eu estiver pensando, você pode adivinhá-lo em um máximo de 7 tentativas. Porque a pesquisa binária elimina muitas possibilidades!

>**Isso é a pesquisa binária**.

---

## Como funciona

A cada etapa da pesquisa binária, você **elimina o número de elementos pela metade** até que só reste um elemento.

De maneira geral, para uma lista de _n_ números, a pesquisa binária precisa de log2 _n_ para retornar o valor correto, enquanto a pesquisa simples precisa de _n_ etapas.

---

## Implementação

Veja o exemplo de uma pesquisa binária em Python no arquivo `pesquisa_binaria.py`.