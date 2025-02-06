# Importa a biblioteca tkinter usada para criar interfaces gráficas.
from tkinter import *

# Atualiza o texto do label_mensagem, exibindo mensagens para o usuário em verde.
def exibirmensagem(mensagem, cor="green"):
    label_mensagem.config(text=mensagem, fg=cor)

# Busca os dados nos campos usados para ecrever e verifica se o cpf e nome foram preenchidos, se foram preenchidos salva os dados no arquivo clientes.txt
# e limpa os campos se não, ele mostra uma mensagem de erro.
def salvarcliente():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    datadenascimento = entry_datadenascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome and cpf:

# O arquivo clientes.txt é aberto no modo "append" ("a"), adicionando novos clientes sem gravar emcima dos dados antigos.

        with open("clientes.txt", "a") as arquivo:
            arquivo.write(f"CPF: {cpf}, Nome: {nome}, Endereço: {endereco}, Data de Nascimento: {datadenascimento}, Telefone: {telefone}, Email: {email}\n")
        limparcampos()

#Exibe uma mensagem de sucesso ou erro.

        exibirmensagem("Cliente cadastrado com sucesso!", "green")
    else:
        exibirmensagem("Nome e CPF são obrigatórios!", "red")

# Obtém o CPF digitado, se nenhum CPF for fornecido, exibe uma mensagem de erro pedindo pra digitar o cpf para exclusão. então ele lê todas as linhas do arquivo clientes.txt
# e escreve de volta apenas as linhas que não contêm o CPF informado.

def excluircliente():
    cpf = entry_cpf.get()
    if not cpf:
        exibirmensagem("Digite o CPF do cliente a ser excluído.", "red")
        return

    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        
#A variável clienteexcluido verifica se um cliente foi realmente removido e se foi removido mostra a mensagem excluido com sucesso ou não.

        with open("clientes.txt", "w") as arquivo:
            clienteexcluido = False
            for linha in linhas:
                if f"CPF: {cpf}" not in linha:
                    arquivo.write(linha)
                else:
                    clienteexcluido = True

#Mensagem se foi excluido ou não os dados.
        if clienteexcluido:
            exibirmensagem(f"Cliente com CPF {cpf} excluído com sucesso!", "green")
            limparcampos()
        else:
            exibirmensagem(f"Nenhum cliente com CPF {cpf} encontrado.", "red")
    except FileNotFoundError:
        exibirmensagem("Arquivo de clientes não encontrado.", "red")

# ferifica se o cpf foi digitado se não foi ele exibe uma mensagem pedindo pra digitar o cpf para atualização.
def editarcliente():
    cpf = entry_cpf.get()
    if not cpf:
        exibirmensagem("Digite o CPF do cliente a ser editado.", "red")
        return
    

# Tenta abrir o arquivo clientes.txt no modo leitura e tenta ler os dados.
    try:
        with open("clientes.txt", "r") as arquivo:
            linhas = arquivo.readlines()

#Abre o arquivo clientes.txt no modo de escrita apaga um arquivo e escreve outro.
        with open("clientes.txt", "w") as arquivo:
            cliente_editado = False
            for linha in linhas:
                if f"CPF: {cpf}" in linha:
                    novo_dado = f"CPF: {cpf}, Nome: {entry_nome.get()}, Endereço: {entry_endereco.get()}, Data de Nascimento: {entry_datadenascimento.get()}, Telefone: {entry_telefone.get()}, Email: {entry_email.get()}\n"
                    arquivo.write(novo_dado)
                    cliente_editado = True
                else:
                    arquivo.write(linha)

# Exibe a mensagem se foi editado com sucesso ou não.
        if cliente_editado:
            exibirmensagem(f"Cliente com CPF {cpf} editado com sucesso!", "green")
            limparcampos()
        else:
            exibirmensagem(f"Nenhum cliente com CPF {cpf} encontrado.", "red")
    except FileNotFoundError:
        exibirmensagem("Arquivo de clientes não encontrado.", "red")

#Limpa o campos de entrada de dados quando inseridos os dados.
def limparcampos():
    entry_nome.delete(0, END)
    entry_cpf.delete(0, END)
    entry_endereco.delete(0, END)
    entry_datadenascimento.delete(0, END)
    entry_telefone.delete(0, END)
    entry_email.delete(0, END)

# Cria uma janela.

janela = Tk() 
janela.title("Cadastro de Clientes")
janela.geometry("425x420")
janela.config(bg="#F0F8FF")
janela.maxsize(width=425, height=400)
janela.minsize(width=425, height=400)

# Adiciona um rótulo.
texto1 = Label(janela, text="Digite os dados para Cadastrar os clientes:", font=("Arial", 12), bg="#F0F8FF")
texto1.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

# Esse código cria um rótulo Label.
label_cpf = Label(janela, text='CPF:', font=("Arial", 10), bg="#F0F8FF")
label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# Cria um campo de entrada Entry para o CPF dentro de uma janela.
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



# Adiciona um botão com comandos na janela.
botaonovocliente = Button(janela, text="Novo Cliente", font=("Arial", 10), bg="#E6E6FA", fg="#000000", relief="raised", command=salvarcliente)
botaonovocliente.grid(column=0, row=7, padx=10, pady=10)

botaoexcluirclientes = Button(janela, text="Excluir Cliente", font=("Arial", 10), bg="#E6E6FA", fg="#000000", relief="raised", command=excluircliente)
botaoexcluirclientes.grid(column=1, row=7, padx=10, pady=10)

botaoeditarclientes = Button(janela, text="Editar Cliente", font=("Arial", 10), bg="#E6E6FA", fg="#000000", relief="raised", command=editarcliente)
botaoeditarclientes.grid(column=1, row=8, padx=10, pady=10)

label_mensagem = Label(janela, text="", font=("Arial", 10, "bold"), bg="#F0F8FF", fg="green")
label_mensagem.grid(column=0, row=9, columnspan=2, pady=10)

# Executa o loop principal da janela fazendo a interação.
janela.mainloop()