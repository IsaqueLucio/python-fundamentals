'''
# NumPy — Estatística e Agregação de Dados

## 1. Introdução

O **NumPy** é uma das principais bibliotecas do Python para trabalhar com números, vetores, matrizes e grandes conjuntos de dados.

Neste módulo, vamos aprender a utilizar o NumPy para realizar operações estatísticas e agregações, como:

* Soma;
* Média;
* Mediana;
* Desvio padrão;
* Variância;
* Percentis;
* Quartis;
* Identificação do maior e menor valor;
* Descoberta do índice de determinado valor;
* Tratamento de valores ausentes (`NaN`);
* Agregações seguras em dados que possuem valores ausentes.

Essas operações são muito comuns em **análise de dados, ciência de dados, inteligência artificial, estatística e engenharia de dados**.

---

# 2. Importando o NumPy

Antes de utilizar o NumPy, precisamos importá-lo:

```python
import numpy as np
```

O `as np` cria um apelido para a biblioteca.

Assim, em vez de escrever:

```python
numpy.mean()
```

podemos escrever:

```python
np.mean()
```

Essa é a forma mais comum de importar o NumPy.

---

# 3. Criando nosso conjunto de dados

Vamos trabalhar com um exemplo de receitas mensais:

```python
import numpy as np

revenue = np.array([1200, 1500, 800, 2200, 3100, 1500, 950])
```

Temos os seguintes valores:

```text
Jan = 1200
Fev = 1500
Mar = 800
Abr = 2200
Mai = 3100
Jun = 1500
Jul = 950
```

Podemos visualizar o array:

```python
print(revenue)
```

Resultado:

```text
[1200 1500  800 2200 3100 1500  950]
```

A partir desse array podemos realizar diversas análises estatísticas.

---

# 4. Soma — `np.sum()`

A função `np.sum()` calcula a soma de todos os valores.

```python
total = np.sum(revenue)

print(total)
```

Resultado:

```text
11250
```

Isso significa que a receita total dos sete meses foi:

```text
R$ 11.250
```

Também podemos fazer diretamente:

```python
print(np.sum(revenue))
```

### Quando utilizar?

A soma é útil quando queremos descobrir:

* Receita total;
* Quantidade total;
* Vendas totais;
* Horas trabalhadas;
* Custos totais;
* Quantidade total de produtos vendidos.

Exemplo:

```python
sales = np.array([10, 20, 15, 30, 25])

print(np.sum(sales))
```

Resultado:

```text
100
```

---

# 5. Média — `np.mean()`

A média aritmética é calculada somando todos os valores e dividindo pela quantidade de valores.

Podemos utilizar:

```python
np.mean(revenue)
```

Exemplo:

```python
average = np.mean(revenue)

print(average)
```

Resultado:

```text
1607.142857142857
```

Como temos muitas casas decimais, podemos formatar o resultado:

```python
print(f"{np.mean(revenue):.2f}")
```

Resultado:

```text
1607.14
```

Portanto, a receita média mensal foi aproximadamente:

```text
R$ 1.607,14
```

### O que significa `.2f`?

O `.2f` significa que queremos mostrar o número com **duas casas decimais**.

Por exemplo:

```python
value = 10.56789

print(f"{value:.2f}")
```

Resultado:

```text
10.57
```

---

# 6. Mediana — `np.median()`

A mediana é o valor que fica no meio de um conjunto de dados quando os valores estão organizados.

Nossa receita é:

```text
1200, 1500, 800, 2200, 3100, 1500, 950
```

Primeiro organizamos:

```text
800
950
1200
1500
1500
2200
3100
```

O valor central é:

```text
1500
```

Portanto:

```python
print(np.median(revenue))
```

Resultado:

```text
1500.0
```

### Média x Mediana

É importante entender a diferença.

A média pode ser influenciada por valores muito altos ou muito baixos.

Por exemplo:

```python
data = np.array([10, 10, 10, 10, 1000])

print("Média:", np.mean(data))
print("Mediana:", np.median(data))
```

A média será muito alta porque o valor `1000` influencia fortemente o resultado.

A mediana continuará sendo:

```text
10
```

Por isso, em alguns tipos de análise, a mediana representa melhor o comportamento típico dos dados.

---

# 7. Desvio padrão — `np.std()`

O desvio padrão indica o quanto os valores estão espalhados em relação à média.

Utilizamos:

```python
np.std(revenue)
```

Exemplo:

```python
standard_deviation = np.std(revenue)

print(standard_deviation)
```

Podemos formatar:

```python
print(f"{np.std(revenue):.2f}")
```

### Como interpretar?

Imagine dois conjuntos:

```python
data1 = np.array([9, 10, 11])
data2 = np.array([1, 10, 19])
```

Os dois possuem média igual a:

```text
10
```

Porém, os valores de `data1` estão muito próximos da média.

Já os valores de `data2` estão muito mais espalhados.

Portanto:

```python
print(np.std(data1))
print(np.std(data2))
```

O segundo conjunto terá um desvio padrão maior.

### Regra geral

**Desvio padrão pequeno:**

Os valores estão próximos da média.

**Desvio padrão grande:**

Os valores estão mais espalhados.

---

# 8. Variância — `np.var()`

A variância também mede a dispersão dos dados.

Utilizamos:

```python
np.var(revenue)
```

Exemplo:

```python
variance = np.var(revenue)

print(variance)
```

A relação entre variância e desvio padrão é:

```text
Variância = Desvio Padrão²
```

E:

```text
Desvio Padrão = √Variância
```

Por exemplo, se a variância for:

```text
100
```

o desvio padrão será:

```text
10
```

porque:

```text
10² = 100
```

No NumPy:

```python
variance = np.var(revenue)
standard_deviation = np.std(revenue)

print("Variância:", variance)
print("Desvio padrão:", standard_deviation)
```

---

# 9. Percentis — `np.percentile()`

Percentis são muito importantes para análise de dados.

Um percentil indica um valor abaixo do qual está determinada porcentagem dos dados.

Por exemplo:

```python
np.percentile(revenue, 90)
```

significa:

> Qual é o valor abaixo do qual aproximadamente 90% das observações estão?

Podemos calcular:

```python
print(np.percentile(revenue, 90))
```

---

# 10. Quartis

Os quartis dividem os dados em quatro partes.

Os principais são:

```text
Q1 = 25º percentil
Q2 = 50º percentil
Q3 = 75º percentil
```

### Primeiro quartil — Q1

```python
q1 = np.percentile(revenue, 25)

print(q1)
```

O Q1 representa o 25º percentil.

---

### Segundo quartil — Q2

O segundo quartil corresponde à mediana:

```python
q2 = np.percentile(revenue, 50)

print(q2)
```

Também podemos utilizar:

```python
print(np.median(revenue))
```

Os resultados serão equivalentes.

---

### Terceiro quartil — Q3

```python
q3 = np.percentile(revenue, 75)

print(q3)
```

O Q3 corresponde ao 75º percentil.

---

# 11. Por que os percentis são úteis?

Imagine que temos os salários de milhares de funcionários.

Podemos descobrir:

```text
Percentil 25 → salários abaixo desse valor representam aproximadamente os 25% inferiores.

Percentil 50 → corresponde à mediana.

Percentil 75 → aproximadamente 75% dos salários estão abaixo desse valor.

Percentil 90 → aproximadamente 90% dos salários estão abaixo desse valor.
```

Também podemos utilizar percentis para identificar possíveis valores extremos.

Por exemplo:

```python
p90 = np.percentile(revenue, 90)

print("Percentil 90:", p90)
```

Isso pode ajudar em análises como:

* Identificação de clientes de alto valor;
* Identificação de vendas excepcionais;
* Análise de salários;
* Análise de desempenho;
* Identificação de possíveis outliers;
* Definição de limites.

---

# 12. Encontrando o maior valor — `np.max()`

Para encontrar o maior valor de um array:

```python
max_value = np.max(revenue)

print(max_value)
```

Resultado:

```text
3100
```

Isso nos informa **qual foi o maior valor**, mas ainda não sabemos onde ele está.

É aí que entra o `argmax()`.

---

# 13. Encontrando o índice do maior valor — `np.argmax()`

A função:

```python
np.argmax()
```

retorna o índice do maior valor.

Exemplo:

```python
best_month_index = np.argmax(revenue)

print(best_month_index)
```

Resultado:

```text
4
```

Por quê?

Porque os índices do array começam em `0`.

Temos:

```text
Índice    Mês    Receita

0         Jan    1200
1         Fev    1500
2         Mar     800
3         Abr    2200
4         Mai    3100
5         Jun    1500
6         Jul     950
```

O maior valor é:

```text
3100
```

E ele está no índice:

```text
4
```

---

# 14. Associando o índice ao mês

Podemos criar uma lista com os meses:

```python
months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul"]
```

Depois:

```python
best_month_index = np.argmax(revenue)

print(months[best_month_index])
```

Resultado:

```text
Mai
```

Podemos juntar tudo:

```python
max_value = np.max(revenue)
best_month_index = np.argmax(revenue)

print(f"A maior receita foi {max_value}.")
print(f"O melhor mês foi {months[best_month_index]}.")
```

Resultado:

```text
A maior receita foi 3100.
O melhor mês foi Mai.
```

---

# 15. Encontrando o menor valor — `np.min()`

Para descobrir o menor valor:

```python
min_value = np.min(revenue)

print(min_value)
```

Resultado:

```text
800
```

---

# 16. Encontrando o índice do menor valor — `np.argmin()`

Assim como `argmax()` encontra o índice do maior valor, `argmin()` encontra o índice do menor.

```python
worst_month_index = np.argmin(revenue)

print(worst_month_index)
```

Resultado:

```text
2
```

O índice `2` corresponde a:

```text
Mar
```

Podemos fazer:

```python
print(f"A menor receita foi {np.min(revenue)}.")
print(f"O pior mês foi {months[np.argmin(revenue)]}.")
```

Resultado:

```text
A menor receita foi 800.
O pior mês foi Mar.
```

---

# 17. Diferença entre `max` e `argmax`

Essa diferença é muito importante.

### `np.max()`

Retorna o **valor**:

```python
np.max(revenue)
```

Resultado:

```text
3100
```

### `np.argmax()`

Retorna o **índice**:

```python
np.argmax(revenue)
```

Resultado:

```text
4
```

Podemos pensar assim:

```text
max    → Qual é o maior valor?
argmax → Onde está o maior valor?
```

Da mesma forma:

```text
min    → Qual é o menor valor?
argmin → Onde está o menor valor?
```

---

# 18. O que é `NaN`?

Na análise de dados, é muito comum encontrarmos informações ausentes.

O NumPy representa um valor numérico ausente utilizando:

```python
np.nan
```

`NaN` significa:

```text
Not a Number
```

ou:

```text
Não é um número
```

Por exemplo:

```python
sensor_data = np.array([
    22.5,
    23.1,
    np.nan,
    22.8,
    np.nan,
    24.0
])
```

Temos:

```text
22.5
23.1
ausente
22.8
ausente
24.0
```

Os dois valores `np.nan` representam dados que não foram registrados ou estão ausentes.

---

# 19. O problema do `NaN`

Se utilizarmos uma função normal de estatística:

```python
print(np.mean(sensor_data))
```

O resultado será:

```text
nan
```

Isso acontece porque as funções estatísticas normais do NumPy consideram o `NaN` durante o cálculo.

Um único `NaN` pode fazer com que o resultado também seja `NaN`.

Por exemplo:

```python
data = np.array([10, 20, np.nan, 40])

print(np.mean(data))
```

Resultado:

```text
nan
```

Isso pode ser um problema quando estamos trabalhando com dados reais.

---

# 20. `np.nanmean()` — Média ignorando NaN

Para calcular a média ignorando valores `NaN`, podemos utilizar:

```python
np.nanmean()
```

Exemplo:

```python
data = np.array([10, 20, np.nan, 40])

print(np.nanmean(data))
```

O NumPy ignora o `NaN` e calcula a média utilizando:

```text
10
20
40
```

A média será:

```text
23.333...
```

Portanto:

```python
print(f"{np.nanmean(data):.2f}")
```

Resultado:

```text
23.33
```

---

# 21. `np.nansum()` — Soma ignorando NaN

Para realizar uma soma ignorando `NaN`:

```python
np.nansum()
```

Exemplo:

```python
data = np.array([10, 20, np.nan, 40])

print(np.nansum(data))
```

Resultado:

```text
70
```

O NumPy simplesmente ignora o valor ausente.

---

# 22. `np.nanmax()` — Maior valor ignorando NaN

Podemos encontrar o maior valor sem considerar os `NaN`:

```python
data = np.array([10, 20, np.nan, 40])

print(np.nanmax(data))
```

Resultado:

```text
40
```

---

# 23. Outras funções da família `nan`

O NumPy possui várias funções que começam com `nan`.

Algumas das principais são:

```text
np.nanmean()  → média ignorando NaN
np.nanmedian() → mediana ignorando NaN
np.nansum()   → soma ignorando NaN
np.nanmax()   → máximo ignorando NaN
np.nanmin()   → mínimo ignorando NaN
np.nanstd()   → desvio padrão ignorando NaN
np.nanvar()   → variância ignorando NaN
```

Exemplo:

```python
data = np.array([10, 20, np.nan, 40, 50])

print("Média:", np.nanmean(data))
print("Mediana:", np.nanmedian(data))
print("Soma:", np.nansum(data))
print("Máximo:", np.nanmax(data))
print("Mínimo:", np.nanmin(data))
print("Desvio padrão:", np.nanstd(data))
print("Variância:", np.nanvar(data))
```

---

# 24. Exemplo completo

Agora podemos juntar tudo o que aprendemos em um único programa:

````python
import numpy as np

print("--- ANÁLISE DE RECEITAS ---")

revenue = np.array([
    1200,
    1500,
    800,
    2200,
    3100,
    1500,
    950
])

months = [
    "Jan",
    "Fev",
    "Mar",
    "Abr",
    "Mai",
    "Jun",
    "Jul"
]

# Estatísticas básicas

print(f"Receita total: {np.sum(revenue)}")
print(f"Receita média: {np.mean(revenue):.2f}")
print(f"Mediana: {np.median(revenue)}")
print(f"Desvio padrão: {np.std(revenue):.2f}")
print(f"Variância: {np.var(revenue):.2f}")

# Percentis

print(f"Q1 (25%): {np.percentile(revenue, 25)}")
print(f"Q2 (50%): {np.percentile(revenue, 50)}")
print(f"Q3 (75%): {np.percentile(revenue, 75)}")
print(f"Percentil 90: {np.percentile(revenue, 90)}")

# Maior valor

max_value = np.max(revenue)
max_index = np.argmax(revenue)

print(f"Maior receita: {max_value}")
print(f"Mês da maior receita: {months[max_index]}")

# Menor valor

min_value = np.min(revenue)
min_index = np.argmin(revenue)

print(f"Menor receita: {min_value}")
print(f"Mês da menor receita: {months[min_index]}")

---

# 25. Exemplo com dados ausentes

Agora vamos analisar dados de um sensor.

```python
import numpy as np

sensor_data = np.array([
    22.5,
    23.1,
    np.nan,
    22.8,
    np.nan,
    24.0
])

print("--- ANÁLISE DO SENSOR ---")

print("Média normal:")
print(np.mean(sensor_data))

print("Média segura:")
print(np.nanmean(sensor_data))

print("Soma segura:")
print(np.nansum(sensor_data))

print("Menor valor:")
print(np.nanmin(sensor_data))

print("Maior valor:")
print(np.nanmax(sensor_data))

print("Desvio padrão:")
print(np.nanstd(sensor_data))
````

A diferença principal é que as funções `nan...` conseguem trabalhar com dados ausentes sem deixar o resultado inteiro como `NaN`.

---

# 26. Resumo das principais funções

| Função            | O que faz                        |
| ----------------- | -------------------------------- |
| `np.sum()`        | Soma os valores                  |
| `np.mean()`       | Calcula a média                  |
| `np.median()`     | Calcula a mediana                |
| `np.std()`        | Calcula o desvio padrão          |
| `np.var()`        | Calcula a variância              |
| `np.percentile()` | Calcula um percentil             |
| `np.max()`        | Encontra o maior valor           |
| `np.min()`        | Encontra o menor valor           |
| `np.argmax()`     | Encontra o índice do maior valor |
| `np.argmin()`     | Encontra o índice do menor valor |
| `np.nanmean()`    | Média ignorando `NaN`            |
| `np.nanmedian()`  | Mediana ignorando `NaN`          |
| `np.nansum()`     | Soma ignorando `NaN`             |
| `np.nanmax()`     | Maior valor ignorando `NaN`      |
| `np.nanmin()`     | Menor valor ignorando `NaN`      |
| `np.nanstd()`     | Desvio padrão ignorando `NaN`    |
| `np.nanvar()`     | Variância ignorando `NaN`        |

---

# 27. O que você precisa memorizar

Não é necessário decorar todas as fórmulas estatísticas. O mais importante inicialmente é entender a função de cada ferramenta.

### Estatísticas básicas

```python
np.sum(data)
np.mean(data)
np.median(data)
np.std(data)
np.var(data)
```

Pense:

```text
sum    → total
mean   → média
median → valor central
std    → dispersão
var    → dispersão ao quadrado
```

### Máximos e mínimos

```python
np.max(data)
np.min(data)

np.argmax(data)
np.argmin(data)
```

Pense:

```text
max    → maior valor
argmax → posição do maior

min    → menor valor
argmin → posição do menor
```

### Dados ausentes

Quando existem `NaN`:

```python
np.nanmean(data)
np.nansum(data)
np.nanmax(data)
np.nanmin(data)
```

Pense:

```text
nanmean → média ignorando NaN
nansum  → soma ignorando NaN
nanmax  → máximo ignorando NaN
nanmin  → mínimo ignorando NaN
```

---

# 28. Conclusão

As funções estatísticas do NumPy são fundamentais para transformar dados brutos em informações úteis.

Com poucas funções podemos responder perguntas como:

```text
Qual foi a receita total?
Qual foi a receita média?
Qual foi o valor típico?
Quanto os valores variam?
Qual foi o maior resultado?
Em qual posição ele aconteceu?
Qual foi o pior resultado?
Qual é o valor correspondente ao percentil 90?
Existem dados ausentes?
Como calcular estatísticas sem que os NaNs estraguem o resultado?
```

Um bom conjunto de funções para começar a memorizar é:

```python
np.sum()
np.mean()
np.median()
np.std()
np.var()

np.percentile()

np.max()
np.min()
np.argmax()
np.argmin()

np.nanmean()
np.nansum()
np.nanmax()
np.nanmin()
```

Essas ferramentas aparecem constantemente em projetos de **Python, análise de dados, NumPy, Pandas, ciência de dados e machine learning**.

```
```

'''