# Desenvolvimento do projeto

O meu objetivo principal ao desenvolver este código é aplicar e demonstrar os meus conhecimentos atuais sobre a utilização de APIs e a criação de interfaces gráficas.

- **Etapa 1: Elaboração do Projeto**
  Na primeira etapa, comecei por conceber o design visual da aplicação e identificar as bibliotecas necessárias para a sua construção.

- **Etapa 2: Construção**
  Nesta fase, concentrei-me na construção da estrutura gráfica da aplicação utilizando a linguagem Python. Posicionei os elementos da interface, como botões, de forma a permitir a interação do utilizador.

- **Etapa 3: Implementação de Funcionalidades**
  Na terceira etapa, atribuí funcionalidades a todos os botões e integrei a aplicação com uma API de consulta de taxas de câmbio.

- **Etapa 4: Compilação**
  A última etapa envolveu a compilação de todo o código, gerando um executável (.exe) para facilitar a utilização da aplicação.

Vamos analisar as principais partes do código:

### Importação de Bibliotecas
```python
import tkinter as tk
import tkcalendar
from tkinter import ttk
import requests
from datetime import datetime
import pandas as pd
from tkinter import filedialog
from tabulate import tabulate
```
Nesta seção, são importadas as bibliotecas necessárias para criar a interface gráfica (usando tkinter), manipular datas (com tkcalendar), fazer requisições HTTP (com requests), trabalhar com dados tabulares (usando pandas e tabulate) e realizar operações de sistema de arquivos (com filedialog).

### Coleta de Dados Iniciais
```python
lista_moedas = requests.get('http://economia.awesomeapi.com.br/json/all')
lista_moedas = lista_moedas.json()
lista_moedas = list(lista_moedas.keys())
```
Essas linhas de código obtêm uma lista de moedas disponíveis a partir de uma API externa e armazenam-na em `lista_moedas`.

### Definição de Funções
O código define várias funções que são usadas para diferentes tarefas. Algumas delas incluem:
- `mostrarapp1` e `mostrarapp2`: Alternam entre duas telas na interface.
- `Buscar1`: Realiza a busca de cotação para uma moeda e data específica e exibe o resultado na interface.
- `Buscar2`: Busca cotações para várias moedas em um período de tempo definido, armazena os dados em um DataFrame e oferece a opção de salvar ou exibir os resultados.
- `escolher_diretorio` e `exibir_df`: Lidam com a escolha do diretório de salvamento e exibição dos resultados tabulares, respectivamente.

### Interface Gráfica
O código define duas telas na interface: `app1` e `app2`. Cada tela contém elementos como rótulos, caixas de seleção, botões e campos de entrada, que permitem ao usuário interagir com a aplicação.

### Funcionalidade de Alternar Telas
Dois botões com ícones (`▶️` e `◀️`) permitem ao usuário alternar entre as telas `app1` e `app2`.

Claro, aqui está uma versão melhorada das descrições para as telas "app1" e "app2":

### app1 - Consulta de Cotação Simples
Na tela "app1", você encontra uma funcionalidade simplificada que permite escolher uma única moeda e uma data específica. A aplicação retorna a cotação da moeda para a data selecionada, tornando o processo rápido e direto.

### app2 - Consulta de Múltiplas Moedas
Em contraste, a tela "app2" oferece uma ferramenta mais robusta. Nesta tela, você pode selecionar várias moedas de uma só vez e escolher o número de dias anteriores a partir da data atual para as consultas. Além disso, você tem a flexibilidade de optar por exibir os resultados na tela ou salvá-los em um local específico. Essa funcionalidade é particularmente útil para consultas envolvendo diversas moedas, tornando a aplicação versátil e poderosa para análises cambiais abrangentes.
