# crudpythoncommysql
CRUD criado em Python fazendo conexão com SGBD MySQL, com objetivos de aprendizagem.

O CRUD feito tem como objetivo inserir, listar, atualizar e apagar os produtos e seus tipos do banco de dados chamado pythonmysql. 
Foram criados dois arquivos Python o primeiro chamado programa.py e o segundo chamado utils.py

O arquivo programa.py recebeu o menu do CRUD, conseguimos isso após importar a função menu do arquivo utils.py e chamamos essa função logo após. O programa.py é essencial, pois é nele que iremos rodar o nosso CRUD.

Já no arquivo utils.py foi importado a biblioteca MySQLdb através do comando no terminal pip install MySQLclient, essa biblioteca nos forece a possibilidade de conectar o CRUD com nosso servidor MySQL, além disso o utils.py também recebeu todas as funções que foram usadas para conectar, desconectar, listar, inserir, atualizar, apagar os produtos e os tipos, e exibir o menu. 

Vamos começar com a primeira função encontrada = conectar():

A função conectar tem como responsabilidade conectar o CRUD com o servidor MySQL. Isso foi possível através de um try except, onde, no escopo no try, foi criado uma variável chamada conection que recebeu a função do MySQLdb chamada 'connect', dentro dela passamos os parâmetros db que recebeu o nome(pythonmysql) do nosso banco de dados(database), host que recebeu o local do nosso host(localhost), user que recebeu o nome do usuário do servidor(pedro) e o password que recebeu a senha(1234) do user. Ainda no try usou-se um return para retornar a variável conection. Já no except foi usado para tratar de um possível erro de conexão, chamando a função 'Error' do MySQLdb e printando uma mensagem de erro.

Função desconectar():

A função desconectar tem como responsabilidade desconectar o CRUD com o servidor MySQL. Seu funcionamento é simples, dentro da função encontramos um if que verifica se o CRUD está conectado, se ele estiver conectado passamos a função 'close()', que irá fechar a conexão(desconectar), se não estiver conectado irá printar uma mensagem dizendo: 'O servidor não está conectado!'.

Função listar_tipos_produtos():

A função listar_tipos_produtos tem como responsabiliadade listar os tipos de produtos cadastrados no CRUD. Seu funcionamento ocorre da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermis executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação das duas variáveis, foi chamado a função execute do cursor, que executou o comando SELECT * FROM tipos_produto, selecionando todas as linhas e colunas da tabela tipos_produto. Após executar o comando, foi criado a variável tipos que irá armazenar o comando usado na função execute anteriormente. Depois de tudo isso foi feito um if, o if irá verificar se o tamanho da variável tipos é maior que 0, ou seja, se há algum registro armazenado, se for maior que 0 irá printar: 'Listando os tipos de produtos', em seguida foi feito um for dentro desse if que vai percorrer cada tipo da variável tipos que armazenou uma tupla com os tipos cadastrados. Nesse for irá printar o id e a descrição de cada tipo cadastrado. Se o tamanho não for maior que 0, então quer dizer que nenhum tipo foi cadastrado ainda, logo irá printar uma mensagem de erro. Depois de tudo isso, fora do escopo do if else, foi chamada a função desconectar que irá desconectar o servidor.

Função listar_produtos():

A função listar_produtos tem como responsabiliadade listar os produtos cadastrados no CRUD. Seu funcionamento ocorre da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação das duas variáveis, foi chamado a função execute do cursor, que executou o comando SELECT * FROM produtos, selecionando todas as linhas e colunas da tabela produtos. Após executar o comando, foi criado a variável produtos que irá armazenar o comando usado na função execute anteriormente. Depois de tudo isso foi feito um if, o if irá verificar se o tamanho da variável produtos é maior que 0, ou seja, se há algum registro armazenado, se for maior que 0 irá printar: 'Listando os produtos', em seguida foi feito um for dentro desse if que vai percorrer cada produto da variável produtos que armazenou uma tupla com os produtos cadastrados. Nesse for irá printar o id, nome, preço, a quantidade no estoque e o id do tipo de cada produto cadastrado. Se o tamanho não for maior que 0, então quer dizer que nenhum produto foi cadastrado ainda, logo irá printar uma mensagem de erro. Depois de tudo isso, fora do escopo do if else, foi chamada a função desconectar, que irá desconectar o servidor.

Função inserir_tipo_produto():

A função inserir_tipo_produto tem como responsabilidade inserir os tipos de produtos no CRUD. Seu funcionamento se dá da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação dessas duas variáveis, foi criada uma nova variável (descricao) que irá pedir ao usuário que digite o tipo que ele gostaria de inserir. Depois essa variável, foi chamada a função execute do cursor, que executou o comando INSERT INTO tipos_produto (descricao) VALUES ('{descricao}'), inserindo o tipo na tabela tipos_produto. Após executar o comando, foi chamada a função commit() da variável conection que irá confirmar o comando SQL. Posteriormente foi incluído um if, que verifica se o total de linhas armazenada no cursor é igual a 1, ou seja, se o comando foi executado com sucesso, se sim irá printar uma mensagem confirmando a inserção, se não irá printar uma mensagem de erro. Após tudo isso será chamada a função desconectar, que irá desconectar o servidor.

Função inserir_produto():

A função inserir_produto tem como responsabilidade inserir os produtos no CRUD. Seu funcionamento se dá da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação dessas duas variáveis, foram criadas quatro novas variáveis (nome, preco, estoque, tipo) cada uma irá pedir ao usuário que digite a informação que ele gostaria de inserir. Depois essa variável, foi chamada a função execute do cursor, que executou o comando INSERT INTO produtos (nome, preco, estoque, id_tipo) VALUES ('{nome}', {preco}, {estoque}, {tipo}), inserindo cada informação do produto na tabela produtos. Após executar o comando, foi chamada a função commit() da variável conection que irá confirmar o comando SQL. Posteriormente foi incluído um if, que verifica se o total de linhas armazenada no cursor é igual a 1, ou seja, se o comando foi executado com sucesso, se sim irá printar uma mensagem confirmando a inserção, se não irá printar uma mensagem de erro. Após tudo isso será chamada a função desconectar, que irá desconectar o servidor.

Função atualizar_tipo_produto():

A função atualzar_tipo_produto tem como responsabilidade atualizar os tipos dos produtos já inseridos no CRUD. Seu funcionamento se dá da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação dessas duas variáveis, foram criadas duas novas variáveis (codigo, descricao) cada uma irá pedir ao usuário que digite a informação que ele gostaria de inserir. Depois essa variável, foi chamada a função execute do cursor, que executou o comando UPDATE tipos_produto SET descricao='{descricao}' WHERE id={codigo}, atualizando o tipo do produto na tabela tipos_produto. Após executar o comando, foi chamada a função commit() da variável conection que irá confirmar o comando SQL. Posteriormente foi incluído um if, que verifica se o total de linhas armazenada no cursor é igual a 1, ou seja, se o comando foi executado com sucesso, se sim irá printar uma mensagem confirmando a inserção, se não irá printar uma mensagem de erro. Após tudo isso será chamada a função desconectar, que irá desconectar o servidor.

Função atualizar_produto():

A função atualzar_produto tem como responsabilidade atualizar os produtos já inseridos no CRUD. Seu funcionamento se dá da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação dessas duas variáveis, foram criadas cinco novas variáveis (codigo, nome, preco, estoque, tipo) cada uma irá pedir ao usuário que digite a informação que ele gostaria de inserir. Depois essa variável, foi chamada a função execute do cursor, que executou o comando UPDATE produtos SET nome='{nome}, preco={preco}, estoque={estoque}, id_tipo={tipo} WHERE id={codigo}, atualizando o os dados do produto na tabela produtos. Após executar o comando, foi chamada a função commit() da variável conection que irá confirmar o comando SQL. Posteriormente foi incluído um if, que verifica se o total de linhas armazenada no cursor é igual a 1, ou seja, se o comando foi executado com sucesso, se sim irá printar uma mensagem confirmando a inserção, se não irá printar uma mensagem de erro. Após tudo isso será chamada a função desconectar, que irá desconectar o servidor.

Função deletar_tipo_produto():

A função deletar_tipo_produto tem como responsabilidade deletar os tipos dos produtos já inseridos no CRUD. Seu funcionamento se dá da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação dessas duas variáveis, foi criada uma nova variável (codigo) ela irá pedir ao usuário que digite a informação que ele gostaria de inserir. Depois essa variável, foi chamada a função execute do cursor, que executou o comando DELETE FROM tipos_produto WHERE id={codigo}, deletando o tipo do produto na tabela tipos_produto. Após executar o comando, foi chamada a função commit() da variável conection que irá confirmar o comando SQL. Posteriormente foi incluído um if, que verifica se o total de linhas armazenada no cursor é igual a 1, ou seja, se o comando foi executado com sucesso, se sim irá printar uma mensagem confirmando a inserção, se não irá printar uma mensagem de erro. Após tudo isso será chamada a função desconectar, que irá desconectar o servidor.

Função deletar_produto():

A função deletar_produto tem como responsabilidade deletar os produtos já inseridos no CRUD. Seu funcionamento se dá da seguinte forma: primeiro criamos a variável conection que recebeu a função conectar, fazendo assim o CRUD se conectar com o servidor MySQL. Logo após criamos a variável cursor, que será de extrema importância para podermos executar os comandos SQL no python, cursor recebeu a função cursor da variável conection. Após a criação dessas duas variáveis, foi criada uma nova variável (codigo) ela irá pedir ao usuário que digite a informação que ele gostaria de inserir. Depois essa variável, foi chamada a função execute do cursor, que executou o comando DELETE FROM produtos WHERE id={codigo}, deletando os dados do produto na tabela produtos. Após executar o comando, foi chamada a função commit() da variável conection que irá confirmar o comando SQL. Posteriormente foi incluído um if, que verifica se o total de linhas armazenada no cursor é igual a 1, ou seja, se o comando foi executado com sucesso, se sim irá printar uma mensagem confirmando a inserção, se não irá printar uma mensagem de erro. Após tudo isso será chamada a função desconectar, que irá desconectar o servidor.

Função menu():

Essa função menu() tem como responsabilidade ser um menu interativo para gerenciamento de produtos. Explicando linha por linha:
print('=========Gerenciamento de Produtos=============='): Isso imprime um título para o menu, indicando que é um sistema de gerenciamento de produtos.

print('Selecione uma opção: '): Esta linha solicita ao usuário que selecione uma opção do menu.

print('1 - Listar.'): Isso exibe a opção 1 do menu, que é listar produtos.

print('2 - Inserir.'): Isso exibe a opção 2 do menu, que é inserir produtos.

print('3 - Atualizar.'): Isso exibe a opção 3 do menu, que é atualizar produtos.

print('4 - Deletar.'): Isso exibe a opção 4 do menu, que é deletar produtos.

opcao = int(input()): Aqui o programa lê a entrada do usuário, presumivelmente a opção do menu. Converte a entrada para um inteiro.

if opcao in [1, 2, 3, 4]:: Verifica se a opção selecionada está entre 1 e 4.

Se a opção for válida, o programa avança para verificar qual opção específica foi selecionada (listar, inserir, atualizar ou deletar).

Dependendo da opção selecionada, o programa solicitará uma sub-opção para a ação selecionada.

Após receber a sub-opção, o programa chama a função correspondente à opção selecionada.

Se a opção selecionada ou a sub-opção não estiverem dentro das opções válidas, o programa exibirá "Opção inválida".

Em resumo, esta função é um menu interativo que permite ao usuário selecionar entre listar, inserir, atualizar ou deletar produtos em um sistema de gerenciamento de produtos.







