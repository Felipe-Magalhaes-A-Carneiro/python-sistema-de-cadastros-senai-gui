import tkinter as tk
from tkinter import messagebox
import csv

# Cria a janela:
janela = tk.Tk()
janela.title("Biblioteca - Cadastro Empréstimos")
# Proporções da janela:
janela.geometry("400x300") 

# Criação das labels (rótulos):
tk.Label(janela, text = "Nome do Usuário:").pack(pady = 5)
nome_usuario = tk.Entry(janela)
nome_usuario.pack(pady = 5)

tk.Label(janela, text="Nome do Livro: ").pack(pady = 5)
nome_livro = tk.Entry(janela)
nome_livro.pack(pady = 5) 

# Criação da lista responsavel pelo armazenamento
emprestimos = []

# Função para o cadastramento de um novo empréstimo:
def cadastrar_emprestimo():
    usuario = nome_usuario.get()
    livro = nome_livro.get()

    if usuario and livro:
        emprestimos.append({"usuario": usuario, "livro": livro})
        messagebox.showinfo("Sucesso", f"Empréstrimos registrados: {livro} para {usuario}")
        nome_usuario.delete(0, tk.END)
        nome_livro.delete(0, tk.END)
        atualizar_emprestimos()
    else:
        messagebox.showerror("Erro. Por favor, preencha todos os campos!")

# Função para salvar os dados no arquivo CSV
def salvar_dados():
    with open("emprestimos.csv", mode= "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["usuario", "livro"])
        for e in emprestimos:
            writer.writerow([ e["usuario"], e["livro"] ])

def carregar_dados():
    try:
        with open("emprestimos.csv", mode= "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                emprestimos.append(row)
    except FileNotFoundError:
        pass # Arquivo ainda não existe

# Criação do botão para cadastrar o empréstimo:
tk.Button(janela, text= "Cadastrar Empréstimo", command = cadastrar_emprestimo).pack(pady = 20)

# Label para exibir a lista de empréstimos registrados
emprestimos_label = tk.Label(janela, text= "")
emprestimos_label.pack(pady= 10)

# Função para atualizar a exibição dos empréstimos
def atualizar_emprestimos():
    texto = "\n".join([f"""Usuário: {e['usuario']} - Livro: '{e['livro']}'""" for e in emprestimos]) # cria uma string que retorna os registros, separando-os por quebras de linha
    emprestimos_label.config(text = texto)


# INICIALIZANDO - Loop principal
janela.mainloop()