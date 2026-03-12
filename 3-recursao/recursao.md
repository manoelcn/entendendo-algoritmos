# Recursão

## O que é?

Recursão é quando uma função chama a si mesma para resolver um problema. A ideia é quebrar um problema grande em versões menores do mesmo problema, até chegar em um caso simples o suficiente para ser resolvido diretamente.

---

## Estrutura básica

Toda função recursiva precisa de duas partes obrigatórias:

- **Caso base:** a condição de parada. Sem ela, a função chama a si mesma infinitamente.
- **Caso recursivo:** a chamada da função para si mesma com um valor menor/simplificado.

```python
def fatorial(x):
    if x == 1:          # caso base
        return 1
    else:
        return x * fatorial(x - 1)   # caso recursivo
```

---

## Como a pilha funciona

A cada chamada de função, o computador aloca um **stack frame** na memória, contendo as variáveis locais e o endereço de retorno.

Em recursão, os frames se acumulam enquanto a função desce, e são desempilhados conforme os resultados sobem:

```
# fatorial(3)

Descida (empilhando):
  fatorial(3) → espera 3 * fatorial(2)
    fatorial(2) → espera 2 * fatorial(1)
      fatorial(1) → retorna 1  ✅ caso base

Subida (desempilhando):
      fatorial(1) = 1
    fatorial(2) = 2 * 1 = 2
  fatorial(3) = 3 * 2 = 6
```

---

## Quando a ação acontece importa

A posição da ação em relação à chamada recursiva determina se ela ocorre na descida ou na subida da pilha.

**Ação na descida** → executada antes da chamada recursiva:
```python
def contagem(x):
    print(x)              # executa imediatamente, na descida
    if x <= 1:
        return
    contagem(x - 1)
# saída: 3, 2, 1
```

**Ação na subida** → executada depois da chamada recursiva:
```python
def fatorial(x):
    if x == 1:
        return 1
    return x * fatorial(x - 1)   # multiplicação espera o retorno, ocorre na subida
```

---

## Stack Overflow

Se uma função recursiva não tiver um caso base (ou ele nunca for atingido), ela chama a si mesma infinitamente. A pilha enche completamente e ocorre um **Stack Overflow**, encerrando o programa com erro.

```
RecursionError: maximum recursion depth exceeded  # Python
StackOverflowError                                # Java
```

---

## Exemplos

**Fatorial:**
```python
def fatorial(x):
    if x == 1:
        return 1
    return x * fatorial(x - 1)
```

**Potência:**
```python
def potencia(base, expoente):
    if expoente <= 0:
        return 1
    return base * potencia(base, expoente - 1)
```

**Soma de lista:**
```python
def soma_de_lista(lista):
    if len(lista) == 0:
        return 0
    elemento = lista.pop(len(lista) - 1)
    return elemento + soma_de_lista(lista)
```

---

## Resumo

| Conceito | Descrição |
|---|---|
| Caso base | Condição de parada da recursão |
| Caso recursivo | Chamada da função com valor reduzido |
| Stack frame | Memória alocada para cada chamada |
| Descida | Fase de empilhamento das chamadas |
| Subida | Fase de desempilhamento e retorno dos resultados |
| Stack Overflow | Erro causado por recursão infinita |