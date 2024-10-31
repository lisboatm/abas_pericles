# Problema: Controle de Abas do Navegador

## Descrição

Péricles, um jovem interessado em história, enfrenta um problema peculiar com seu navegador de internet, que é infectado por um malware. A cada aba que ele fecha, duas novas abas são abertas. No entanto, se ele clicar em uma propaganda, uma aba é fechada sem abrir novas. Sua tarefa é determinar quantas abas restarão no navegador após uma sequência de ações.

## Entrada

A entrada é composta por:
- A primeira linha contém dois inteiros positivos \( N \) e \( M \) ( \( 0 < N, M < 500 \) ), representando o número inicial de abas e o número de ações que Péricles realizará.
- As \( M \) linhas seguintes contêm a descrição das ações, que podem ser:
  - `fechou`: Indica que uma aba foi fechada.
  - `clicou`: Indica que Péricles clicou em uma propaganda.

## Saída

A saída deve consistir em uma única linha contendo um único inteiro que representa o número final de abas no navegador de Péricles após todas as ações.

## Exemplo de Entrada

```
3 5
fechou
fechou
clicou
clicou
clicou
```

## Exemplo de Saída

```
2
```

## Restrições

- O número de abas deve ser sempre maior ou igual a zero.

## Observações

- Certifique-se de que o programa lida corretamente com as ações e não permite que o número de abas fique negativo.
