
from tkinter import *

def exibirmensagem(mensagem, cor="green"):
    label_mensagem.config(text=mensagem, fg=cor)

def salvarcliente():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    datadenascimento = entry_datadenascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome and cpf:
        with open("clientes.txt", "a") as arquivo:
            arquivo.write(f"CPF: {cpf}, Nome: {nome}, Endereço: {endereco}, Data de Nascimento: {datadenascimento}, Telefone: {telefone}, Email: {email}\n")
        limparcampos()
        exibirmensagem("Cliente cadastrado com sucesso!", "green")
    else:
        exibirmensagem("Nome e CPF são obrigatórios!", "red")

def excluircliente():
    cpf = entry_cpf.get()
    if not cpf:
        exibirmensagem("Digite o CPF do cliente a ser excluído.", "red")
        return

    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        
        with open("clientes.txt", "w") as arquivo:
            clienteexcluido = False
            for linha in linhas:
                if f"CPF: {cpf}" not in linha:
                    arquivo.write(linha)
                else:
                    clienteexcluido = True

        if clienteexcluido:
            exibirmensagem(f"Cliente com CPF {cpf} excluído com sucesso!", "green")
            limparcampos()
        else:
            exibirmensagem(f"Nenhum cliente com CPF {cpf} encontrado.", "red")
    except FileNotFoundError:
        exibirmensagem("Arquivo de clientes não encontrado.", "red")

def editarcliente():
    cpf = entry_cpf.get()
    if not cpf:
        exibirmensagem("Digite o CPF do cliente a ser editado.", "red")
        return
    
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        
        with open("clientes.txt", "w") as arquivo:
            cliente_editado = False
            for linha in linhas:
                if f"CPF: {cpf}" in linha:
                    novo_dado = f"CPF: {cpf}, Nome: {entry_nome.get()}, Endereço: {entry_endereco.get()}, Data de Nascimento: {entry_datadenascimento.get()}, Telefone: {entry_telefone.get()}, Email: {entry_email.get()}\n"
                    arquivo.write(novo_dado)
                    cliente_editado = True
                else:
                    arquivo.write(linha)

        if cliente_editado:
            exibirmensagem(f"Cliente com CPF {cpf} editado com sucesso!", "green")
            limparcampos()
        else:
            exibirmensagem(f"Nenhum cliente com CPF {cpf} encontrado.", "red")
    except FileNotFoundError:
        exibirmensagem("Arquivo de clientes não encontrado.", "red")

def limparcampos():
    entry_nome.delete(0, END)
    entry_cpf.delete(0, END)
    entry_endereco.delete(0, END)
    entry_datadenascimento.delete(0, END)
    entry_telefone.delete(0, END)
    entry_email.delete(0, END)

janela = Tk()
janela.title("Cadastro de Clientes")
janela.geometry("425x420")
janela.config(bg="#F0F8FF")
janela.maxsize(width=425, height=400)
janela.minsize(width=425, height=400)

texto1 = Label(janela, text="Digite os dados para Cadastrar os clientes:", font=("Arial", 12), bg="#F0F8FF")
texto1.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

label_cpf = Label(janela, text='CPF:', font=("Arial", 10), bg="#F0F8FF")
label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_cpf = Entry(janela, width=35, font=("Arial", 10))
entry_cpf.grid(row=1, column=1, padx=10, pady=5)

label_nome = Label(janela, text='Nome:', font=("Arial", 10), bg="#F0F8FF")
label_nome.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_nome = Entry(janela, width=35, font=("Arial", 10))
entry_nome.grid(row=2, column=1, padx=10, pady=5)

label_endereco = Label(janela, text='Endereço:', font=("Arial", 10), bg="#F0F8FF")
label_endereco.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_endereco = Entry(janela, width=35, font=("Arial", 10))
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

label_datadenascimento = Label(janela, text='Data de Nascimento:', font=("Arial", 10), bg="#F0F8FF")
label_datadenascimento.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_datadenascimento = Entry(janela, width=35, font=("Arial", 10))
entry_datadenascimento.grid(row=4, column=1, padx=10, pady=5)

label_telefone = Label(janela, text='Telefone:', font=("Arial", 10), bg="#F0F8FF")
label_telefone.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_telefone = Entry(janela, width=35, font=("Arial", 10))
entry_telefone.grid(row=5, column=1, padx=10, pady=5)

label_email = Label(janela, text='Email:', font=("Arial", 10), bg="#F0F8FF")
label_email.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_email = Entry(janela, width=35, font=("Arial", 10))
entry_email.grid(row=6, column=1, padx=10, pady=5)

botaonovocliente = Button(janela, text="Novo Cliente", font=("Arial", 10), bg="#E6E6FA", fg="#000000", relief="raised", command=salvarcliente)
botaonovocliente.grid(column=0, row=7, padx=10, pady=10)

botaoexcluirclientes = Button(janela, text="Excluir Cliente", font=("Arial", 10), bg="#E6E6FA", fg="#000000", relief="raised", command=excluircliente)
botaoexcluirclientes.grid(column=1, row=7, padx=10, pady=10)

botaoeditarclientes = Button(janela, text="Editar Cliente", font=("Arial", 10), bg="#E6E6FA", fg="#000000", relief="raised", command=editarcliente)
botaoeditarclientes.grid(column=1, row=8, padx=10, pady=10)

label_mensagem = Label(janela, text="", font=("Arial", 10, "bold"), bg="#F0F8FF", fg="green")
label_mensagem.grid(column=0, row=9, columnspan=2, pady=10)

janela.mainloop()