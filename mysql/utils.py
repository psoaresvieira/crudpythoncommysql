import MySQLdb


def conectar():

    # Função feita para conectar o servdior.

    try:
        conection = MySQLdb.connect(
            db='pythonmysql',
            host='localhost',
            user='pedro',
            password='1234'
        )
        return conection
    except MySQLdb.Error as e:
        print(f'Erro ao conectar com o MySQL Server: {e}')


def desconectar(conection):

    # Função que desconecta o servidor.

    if conection:
        conection.close()
    else:
        print('Você não está conectado! ')


def listar_tipos_produto():

    # Função para listar os tipos de produtos

    conection = conectar()
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM tipos_produto')
    tipos = cursor.fetchall()

    if len(tipos) > 0:
        print('Listando os tipos de produtos.')
        print('-------------------------------------')
        for tipo in tipos:
            print(f'ID: {tipo[0]} ')
            print(f'Descricao: {tipo[1]} ')
    else:
        print('Não existe nenhum tipo de produto cadastrado! ')
    desconectar(conection)


def listar_produtos():

    # Função para listar os produtos

    conection = conectar()
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos...')
        print('--------------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print(f'ID Tipo: {produto[4]}')
            print('--------------------------')
    else:
        print('Não existem produtos cadastrados! ')
        desconectar(conection)


def inserir_tipo_produto():

    # Função para inserir o tipo de um produto

    conection = conectar()
    cursor = conection.cursor()

    descricao = input('Informe o tipo: ')

    cursor.execute(f"INSERT INTO tipos_produto (descricao) VALUES ('{descricao}')")
    conection.commit()

    if cursor.rowcount == 1:
        print(f'O tipo {descricao} foi inserido com sucesso! ')
    else:
        print('Não foi possível inserir o tipo')
    desconectar(conection)


def inserir_produto():

    # Função para inserir um produto

    conection = conectar()
    cursor = conection.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade no estoque: '))
    tipo = int(input('Informe o id do tipo do produto: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque, id_tipo) VALUES ('{nome}', {preco}, {estoque}, {tipo})")
    conection.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso! ')
    else:
        print('Não foi possível inserir o produto! ')
    desconectar(conection)


def atualizar_tipo_produto():

    # Função para atualizar o tipo de um produto

    conection = conectar()
    cursor = conection.cursor()

    codigo = int(input('Informe o código do tipo: '))
    descricao = input('Informe o novo tipo: ')

    cursor.execute(f"UPDATE tipos_produto SET descricao='{descricao}' WHERE id={codigo}")
    conection.commit()

    if cursor.rowcount == 1:
        print(f'O tipo {descricao} foi atualizado com sucesso')
    else:
        print('Erro ao atualizar o tipo. ')
    desconectar(conection)


def atualizar_produto():

    # Função para atualizar um produto

    conection = conectar()
    cursor = conection.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int(input('Informe a nova quantidade no estoque: '))
    tipo = int(input('Informe o id do tipo: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque}, id_tipo={tipo} WHERE id={codigo}")
    conection.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso ')
    else:
        print('Erro ao atualizar o produto. ')
    desconectar(conection)


def deletar_tipo_prodito():

    # Função para deletar um tipo de produto

    conection = conectar()
    cursor = conection.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f"DELETE FROM tipos_produto WHERE id={codigo}")
    conection.commit()

    if cursor.rowcount == 1:
        print('Tipo excluído com sucesso! ')
    else:
        print(f'Erro ao excluir o tipo com id = {codigo}')


def deletar_produto():

    # Função para deletar um produto

    conection = conectar()
    cursor = conection.cursor()

    codigo = int(input('Informe o código do produto: '))

    cursor.execute(f"DELETE FROM produtos WHERE id={codigo}")
    conection.commit()

    if cursor.rowcount == 1:
        print('Produto excluído com sucesso. ')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')
    desconectar(conection)


def menu():

    # Função para gerar o menu inicial

    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar.')
    print('2 - Inserir.')
    print('3 - Atualizar.')
    print('4 - Deletar.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            print('Digite 1 para listar os produtos, Digite 2 para listar os tipos')
            op = int(input())
            if op in [1, 2]:
                if op == 1:
                    listar_produtos()
                elif op == 2:
                    listar_tipos_produto()
                else:
                    print('Opção inválida')
        elif opcao == 2:
            print('Digite 1 para inserir os produtos, Digite 2 para inserir os tipos')
            op2 = int(input())
            if op2 in [1, 2]:
                if op2 == 1:
                    inserir_produto()
                elif op2 == 2:
                    inserir_tipo_produto()
                else:
                    print('Opção inválida')
        elif opcao == 3:
            print('Digite 1 para atualizar os produtos, Digite 2 para atualizar os tipos')
            op3 = int(input())
            if op3 in [1, 2]:
                if op3 == 1:
                    atualizar_produto()
                elif op3 == 2:
                    atualizar_tipo_produto()
                else:
                    print('Opção inválida')
        elif opcao == 4:
            print('Digite 1 para apagar os produtos, Digite 2 para apagar os tipos')
            op4 = int(input())
            if op4 in [1, 2]:
                if op4 == 1:
                    deletar_produto()
                elif op4 == 2:
                    deletar_tipo_prodito()
                else:
                    print('Opção inválida')
    else:
        print('Opção inválida')
