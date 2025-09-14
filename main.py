import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import os

# Criar tela principal
tela = tk.Tk()
tela.title("Minha carteiraaa")
tela.geometry("600x400")

"""
tk.label  cria um texto fixo na tela
tk.Entry cria  caixa de texto onde da p digitar
.pack(pady=5)  poe elemento na tela e adiciona um espaçamento vertical (5px).
"""

# 1. Criar Campos para Descrição
legenda_desc = tk.Label(tela, text="Descrição: ")   # texto fixo
legenda_desc.pack(pady=5) # pack = posiciona o elemento na janela
entrada_desc = tk.Entry(tela, width=40)
entrada_desc.pack(pady=5)

# 2. Criar campos p valor
legenda_valor = tk.Label(tela, text="Valor: ")
legenda_valor.pack(pady=5)
entrada_valor = tk.Entry(tela, width=40)
entrada_valor.pack(pady=5)

# Lista que vai guardar os registros
registros = []

# 3. Função que vai ser chamada quando apertar o botão (Passo 4)
def adicionar_registro():
    descricao = entrada_desc.get() # pega a desc digitada
    valor = entrada_valor.get() # pega o valor digitado

    if descricao == "" or valor == "":
        messagebox.showwarning("Preencher tudo né rapa! ")
        return
    
    try:
        valor = float(valor)
    except:
        messagebox.showerror("Q numero é esse po??")
        return
    
    #salva o registro na lista
    registros.append({"descricao": descricao, "valor": valor})

    print(f'Registros atuais: {registros}')

    # Limpa os campos depois de adicionar
    entrada_desc.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)

    
# 4. Criar botão p adicionar um registro de valor
btn_adc = tk.Button(tela, text="Adicionar", command=adicionar_registro)
btn_adc.pack(pady=10)

tela.mainloop()