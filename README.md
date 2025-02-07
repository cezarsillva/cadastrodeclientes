Programa de cadastro de clientes em Python que salva os dados em .txt.

1. Importa a biblioteca tkinter usada para criar interfaces gráficas.
2. Atualiza o texto do label_mensagem, exibindo mensagens padrão para o usuário em verde.
3. Busca os dados nos campos usados para ecrever e verifica se o cpf e nome foram preenchidos, se foram preenchidos salva os dados no arquivo clientes.txt e limpa os campos se não, ele mostra uma mensagem de erro.
4. O arquivo clientes.txt é aberto no modo "append" ("a"), adicionando novos clientes sem gravar emcima dos dados antigos.
5. Exibe uma mensagem de sucesso ou erro.
6. Obtém o CPF digitado, se nenhum CPF for fornecido, exibe uma mensagem de erro pedindo pra digitar o cpf para exclusão, então ele lê todas as linhas do arquivo clientes.txt e escreve de volta apenas as linhas que não contêm o CPF informado.
7. A variável clienteexcluido verifica se um cliente foi realmente removido e se foi removido mostra a mensagem excluido com sucesso ou não.
8. Mensagem se foi excluido ou não os dados.
9. Verifica se o cpf foi digitado se não foi ele exibe uma mensagem pedindo pra digitar o cpf para atualização.
10. Tenta abrir o arquivo clientes.txt no modo leitura e tenta ler os dados.
11. Abre o arquivo clientes.txt no modo de escrita apaga um arquivo e escreve outro.
12. Exibe a mensagem se foi editado com sucesso ou não.
13. Limpa o campos de entrada de dados quando inseridos os dados.
14. Cria uma janela.
15. Adiciona um rótulo.
16. Esse código cria um rótulo Label.
17. Cria um campo de entrada Entry para o CPF dentro de uma janela.
18. Adiciona um botão com comandos na janela.
19. Executa o loop principal da janela fazendo a interação.
