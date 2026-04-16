# 💰 Contador de Moedas (Euro)

Este projeto em Python calcula a quantidade mínima de moedas necessárias para representar um determinado valor em euros.

## 📌 Descrição

A função `EX1_Nivel_1(valor)` recebe um valor entre 0.01€ e 20€ e devolve um dicionário com a quantidade de cada moeda necessária.

O cálculo é feito usando as seguintes moedas:

* 2€
* 1€
* 50 cêntimos
* 20 cêntimos
* 10 cêntimos
* 5 cêntimos
* 2 cêntimos
* 1 cêntimo


## ⚙️ Como funciona

O algoritmo:

* Usa divisões inteiras `//` para calcular o número de moedas
* Usa o resto `%` para calcular o valor restante
* Arredonda os valores para evitar erros de precisão com números decimais
* Guarda os resultados num dicionário

## 🧪 Exemplo de utilização
```
Entrada:
3.87

Saída:
{'2€': 1.0, '1€': 1.0, '50cent': 1.0, '20cent': 1.0, '10cent': 1.0, '5cent': 1.0, '2cent': 1.0, '1cent': 0.0}
