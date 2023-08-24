#pip install tkcalendar
import tkinter as tk
import tkcalendar
from tkinter import ttk
import requests
from datetime import datetime
import pandas as pd
from tkinter import filedialog
from tabulate import tabulate

lista_moedas = requests.get('http://economia.awesomeapi.com.br/json/all')
lista_moedas = lista_moedas.json()
lista_moedas = list(lista_moedas.keys())

def mostrarapp1():
    app2.grid_forget()
    app1.grid(row=0,column=0,columnspan=2)

def mostrarapp2():
    app1.grid_forget()
    app2.grid(row=0,column=0,columnspan=2)


def Buscar1():
    moeda = dropdownlista.get()
    if moeda:
        data = data1.get()
        if data:
            dia,mes,ano = data.split('/')
            requisicao1 = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}')
            requisicao1 = requisicao1.json()
            resposta['text'] = requisicao1[0]['bid']
        else:
            resposta['text'] = 'Escolha alguma Data!'
    else:
        resposta['text'] = 'Escolha alguma moeda'



def extrair_data(tupla):
    data_str, _ = tupla
    return data_str.strftime('%d/%m/%Y')

def Buscar2():
    dias = str(inpu2.get())
    moedas = input.get("1.0", tk.END)
    moedas = moedas[0:-1]
    listam = moedas.split(', ')
    listam = set(listam)
    intersecao = set(lista_moedas).intersection(listam)
    dataframe = pd.DataFrame()
    if list(intersecao) == list(listam):
        for moeda in listam:
            cotacoes2 = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda}/{dias}')
            cotacoes2 = cotacoes2.json()
            listavalores = []
            for c in cotacoes2:
                data = datetime.fromtimestamp(int(c['timestamp']))
                valor = c['bid']
                listavalores.append((data, valor))

            valores = sorted(listavalores, key=lambda x: x[0])
            dataf = [c[0].strftime('%d/%m/%Y') for c in valores]
            valor = [c[1] for c in valores]
            dataframe[moeda] = valor
            dataframe = dataframe.set_index(pd.Index(dataf))
        global salvar
        salvar = dataframe
        Texto23['text'] = 'Moedas Buscadas com Sucesso'
    else:
        Texto23['text'] = 'insira moedas validas'

def escolher_diretorio():
    try:
        diretorio_escolhido = filedialog.askdirectory()
        global salvar
        salvar.to_excel(diretorio_escolhido + '/' + 'Ultimascotacoes.xlsx')
        Texto23['text'] = 'Arquivo Salvo com Sucesso'
    except:
        Texto23['text'] = 'Selecione Primeiro as Moedas!!'

def exibir_df():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Resultados dataframe")
    nova_janela.geometry("900x600")
    texto24 = tk.Text(nova_janela)
    texto24.pack(fill=tk.BOTH,expand=True)
    try:
        global salvar
        df_str = tabulate(salvar, headers='keys', tablefmt='fancy_grid')

        # Limpa a área de texto existente (caso haja algo lá)
        texto24.delete(1.0, tk.END)

        # Insere a string formatada na área de texto
        texto24.insert(tk.END, df_str)
    except:
        Texto23['text'] = 'Selecione Primeiro as Moedas!!'

def AddText():
    moeda = dropdownlista21.get()
    input2 = input.get("1.0", tk.END)
    if len(input2) == 1 :
        input.insert("end", moeda)
    else:
        input.insert("end", ', ' + moeda)

janela = tk.Tk()
janela.title("Cotacao Moedas")
janela.rowconfigure(0, weight=1) #configurar ajuste automatico
janela.columnconfigure([0,1], weight=1) #colunas com ajuste automatico

app1 = tk.Frame(janela)
app2 = tk.Frame(janela)
#===============================================================================================================
titulo = tk.Label(app1,text="Ferramenta cotações moedas",bg='black',fg='white', relief='raised',borderwidth=2)#insira argumentos como texto tamanho, fundo e cor
texto1 = tk.Label(app1,text="Selecione a Moeda Desejada ",borderwidth=2)#insira argumentos como texto tamanho, fundo e cor
dropdownlista = ttk.Combobox(app1,values=lista_moedas)
texto2 = tk.Label(app1,text="Selecione a Data desejada ",borderwidth=2)#insira argumentos como texto tamanho, fundo e cor
resposta = tk.Label(app1,text=" aaaaaa",borderwidth=2,bg='white')#insira argumentos como texto tamanho, fundo e cor
data1 = tkcalendar.DateEntry(app1,year=2023, locale='pt_br')
botao1 = tk.Button(app1,text="Buscar Cotação", command=Buscar1, relief='raised')
titulo2 = tk.Label(text="Ferramenta",bg='black',fg='white', relief='raised',borderwidth=2)


titulo.grid(row=0, column=0,columnspan=2, sticky="NSEW",padx=10,pady=10) # insira posição da janela
texto1.grid(row=1, column=0, sticky="NS")
dropdownlista.grid(row=1, column=1, sticky="NSEW")
texto2.grid(row=2, column=0, sticky="NSEW")
resposta.grid(row=3, column=0, sticky="NSEW")
data1.grid(row=2, column=1, sticky="NSEW")
botao1.grid(row=3, column=1, sticky="NSEW") # insira posição da janela
titulo2.grid(row=4, column=0,columnspan=2, sticky="NSEW") # insira posição da janela
#===============================================================================================================

titulo21 = tk.Label(app2,text="cotações Multiplas moedas",bg='black',fg='white', relief='raised',borderwidth=2)#insira argumentos como texto tamanho, fundo e cor
texto22 = tk.Label(app2,text="Adicione Moeda desejada ",borderwidth=2)
input = tk.Text(app2,width=20, height=2)
dropdownlista21 = ttk.Combobox(app2,values=lista_moedas)
botao21 = tk.Button(app2,text='Adicionar Moeda',command=AddText,width=10, height=1)
texto22a = tk.Label(app2,text="Deseja Buscar Quantas cotações?",borderwidth=2)
inpu2 = tk.Entry(app2)
botao22 = tk.Button(app2,text='Buscar todas as cotações',command=Buscar2, width=10, height=1)
Texto23 = tk.Label(app2,text=" ",borderwidth=2)
botao23 = tk.Button(app2,text='Salvar Moedas',command=escolher_diretorio,width=10, height=1)
botao24 = tk.Button(app2,text='Exibir moedas',command=exibir_df,width=10, height=1)


titulo21.grid(row=0, column=0,columnspan=2, sticky="NSEW",padx=10,pady=10) # insira posição da janela
texto22.grid(row=1, column=1, sticky="NS")
texto22a.grid(row=2,column=0, sticky="NSEW")
inpu2.grid(row=2,column=1, sticky="NSEW")
dropdownlista21.grid(row=1, column=0, sticky="NSEW")
botao21.grid(row=1, column=1, sticky="NSEW")
input.grid(row=4, column=0,columnspan=2,sticky="NSEW")
botao22.grid(row=6, column=0,columnspan=2,sticky="NSEW",padx=10,pady=10)
Texto23.grid(row=7, column=0,columnspan=2,sticky="NSEW")
botao23.grid(row=8, column=0,sticky="NSEW")
botao24.grid(row=8, column=1,sticky="NSEW")
#================================================================================================================
botaoa= tk.Button(text=" ▶️ ", command=mostrarapp2, relief='raised',font=("Helvetica", 22))
botaov= tk.Button(text=" ◀️ ", command=mostrarapp1, relief='raised',font=("Helvetica", 22))
botaoa.grid(row=9, column=1, sticky="NSEW")
botaov.grid(row=9, column=0, sticky="NSEW")


mostrarapp1()
janela.mainloop()

