from modulo_funcoes import *

# ========================== INICIO PROGRAMA ================================================= #
op_sistema = ''
print(f'Bem-vindo ao Sistema de Cadastro do Supermercado Super!\n')
while op_sistema != '-1':

    op_sistema = input(
        f'Selecione uma das opções:\n'
        f'1 - Clientes\n'
        f'2 - Funcionários\n'
        f'3 - Produtos\n'
        f'-1 - Finalizar\n')

    # ========================== INICIO CRUD CLIENTES ================================================= #
    if op_sistema == '1':
        print(cabecalho('CLIENTE'))

        op_cliente = ''
        while op_cliente != '-1':
            op_cliente = input(
                f'Selecione uma das opções:\n'
                f'1 - Cadastrar Cliente\n'
                f'2 - Editar Cliente\n'
                f'3 - Remover Cliente\n'
                f'4 - Buscar Cliente\n'
                f'5 - Listar Clientes\n'
                f'-1 - Voltar Menu Principal\n')
            # ========================== CADASTRO CLIENTE ================================================= #
            if op_cliente == '1':
                print(cabecalho('CADASTRO CLIENTE'))
                cpf = ''

                nome = input('Digite o nome: ').title()
                while len(cpf) != 11:
                    cpf = input('Digite o CPF(apenas números): ')
                    if len(cpf) != 11:
                        print('CPF inválido, digite novamente')

                data_nascimento = input(f'Data de nascimento (dd-mm-aaaa): ')
                data_format = converter_data_nascimento_de_string_para_int(data_nascimento)
                idade = calculo_idade_usuario(data_format)

                dados_cliente = (f'{nome}\n '
                                 f'CPF: {cpf}\n '
                                 f'Data_Nascimento: {data_nascimento}\n '
                                 f'Idade: {idade}\n')

                append_em_arquivo('clientes.txt', dados_cliente)

                print('Cliente cadastrado com sucesso!\n')

            # ========================== EDITAR CLIENTE ================================================= #
            elif op_cliente == '2':
                print(cabecalho('EDITAR CLIENTE'))

                try:
                    texto_arquivo = abrir_arquivo_leitura('clientes.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado')

                busca_cliente = input('Digite o CPF do cliente que deseja editar: ').title()
                encontrado = False
                op_editar = ''

                while op_editar != '-1':
                    for i in range(len(texto_arquivo)):
                        if busca_cliente in texto_arquivo[i]:
                            encontrado = True
                            op_editar = input(f'Selecione a opção desejada para alterar o cadastro: \n'
                                              f'1 - CPF\n'
                                              f'2 - Nome\n'
                                              f'3 - Data Nascimento\n'
                                              f'-1 - Sair\n')
                            if op_editar == '1':
                                novo_cpf = ''
                                while len(novo_cpf) != 11:
                                    novo_cpf = input('Digite o novo CPF(apenas números): ')
                                    if len(novo_cpf) != 11:
                                        print('CPF inválido, digite novamente')
                                    else:
                                        texto_arquivo[i] = ' CPF:' + novo_cpf + '\n'

                                print('CPF alterado com sucesso!\n')

                            elif op_editar == '2':
                                novo_nome = input('Digite o nome: ').title()
                                texto_arquivo[i - 1] = novo_nome + '\n'
                                busca_cliente = texto_arquivo[i - 1]
                                print('Nome alterado com sucesso!')

                            elif op_editar == '3':
                                nova_data = input('Digite a data de nascimento:')
                                data_format = converter_data_nascimento_de_string_para_int(nova_data)
                                idade = calculo_idade_usuario(data_format)
                                texto_arquivo[i + 1] = ' Data_Nascimento:' + nova_data + '\n'
                                texto_arquivo[i + 2] = ' Idade:' + str(idade) + '\n'
                                print('Data de nascimento alterada com sucesso!')

                            elif op_editar == '-1':
                                print('Informações Salvas!')

                    if encontrado:
                        escrita_arquivo('clientes.txt', texto_arquivo)
                    else:
                        print('Cliente não encontrado\n')
                        break

            # ========================== REMOVER CLIENTE ================================================= #
            elif op_cliente == '3':
                print(cabecalho('REMOVER CLIENTE'))

                try:
                    texto_arquivo = abrir_arquivo_leitura('clientes.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_cliente = input('Digite o CPF do cliente que deseja remover: ').title()
                encontrado = False
                for i in range(len(texto_arquivo)):
                    if busca_cliente in texto_arquivo[i]:
                        encontrado = True
                        del_op = input(f'Realmente deseja deletar o cliente {texto_arquivo[i - 1].strip()}?\n'
                                       f'Digite "s" para SIM e "n" para NÃO: ').upper()
                        if del_op == 'S':
                            texto_arquivo[i - 1] = ''
                            for j in range(3):
                                texto_arquivo[i + j] = ''
                            print('Cliente deletado!')
                        elif del_op == 'N':
                            print('Operação cancelada!')

                while '' in texto_arquivo:
                    texto_arquivo.remove('')

                if encontrado:
                    escrita_arquivo('clientes.txt', texto_arquivo)
                else:
                    print('Cliente não encontrado\n')

            # ========================== BUSCAR CLIENTE ============================== #
            elif op_cliente == '4':
                print(cabecalho('BUSCAR CLIENTE'))
                try:
                    texto_arquivo = abrir_arquivo_leitura('clientes.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                op_busca = ''
                encontrado = False
                while op_busca != '-1':
                    op_busca = input(f'Gostaria de buscar por CPF ou Nome: \n'
                                     f'1 - CPF\n'
                                     f'2 - Nome\n'
                                     f'-1 - Sair\n')

                    if op_busca == '1':
                        busca_cpf = ''
                        while len(busca_cpf) != 11:
                            busca_cpf = input('Digite o CPF: ')
                            if len(busca_cpf) != 11:
                                print('CPF invalido, tente novamente')
                            else:
                                for i in range(len(texto_arquivo)):
                                    if busca_cpf in texto_arquivo[i]:
                                        encontrado = True
                                        print(texto_arquivo[i - 1].strip())
                                        for j in range(3):
                                            print(texto_arquivo[i + j].strip())
                                if not encontrado:
                                    print('CPF não encontrado')

                    elif op_busca == '2':
                        busca_nome = input('Digite o nome: ').title()
                        for i in range(len(texto_arquivo)):
                            if busca_nome in texto_arquivo[i]:
                                encontrado = True
                                for j in range(4):
                                    print(texto_arquivo[i + j].strip())
                        if not encontrado:
                            print('Cliente não encontrado')

            # ========================== LISTAR CLIENTE ================================================= #
            elif op_cliente == '5':
                print(cabecalho('LISTAR CLIENTE'))

                try:
                    arquivo_leitura = open('clientes.txt', 'r', encoding='utf8')
                    print(arquivo_leitura.read())
                    arquivo_leitura.close()
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

    # ========================== INICIO CRUD FUNCIONÁRIOS ================================================= #
    elif op_sistema == '2':
        print(cabecalho('FUNCIONÁRIOS') + '\n')
        op_funcionario = ''

        while op_funcionario != '-1':
            op_funcionario = input('Escolha uma das opções:\n'
                                   f'1 - Cadastrar Funcionário\n'
                                   f'2 - Editar Funcionário\n'
                                   f'3 - Remover Funcionário\n'
                                   f'4 - Buscar Funcionário\n'
                                   f'5 - Listar Funcionários\n'
                                   f'-1  Voltar ao menu principal\n')

            # ========================== CADASTRO FUNCIONÁRIO ================================================= #
            if op_funcionario == '1':
                print(cabecalho('CADASTRO FUNCIONÁRIO'))

                nome = input('Nome do Funcionário: ').title()
                matricula = input('Matrícula do funcionário: ')
                data_admissao = input('Data Admissão: ')
                data_format_admissao = converter_data_nascimento_de_string_para_int(data_admissao)
                data_nascimento_func = input(f'Data de nascimento (dd-mm-aaaa): ')
                data_format = converter_data_nascimento_de_string_para_int(data_nascimento_func)
                idade = calculo_idade_usuario(data_format)

                dados_funcionarios = (f'{nome}\n '
                                      f'Matrícula: {matricula}\n '
                                      f'Data admissão: {data_admissao}\n '
                                      f'Data_Nascimento: {data_nascimento_func}\n '
                                      f'Idade: {idade}\n')

                append_em_arquivo('funcionarios.txt', dados_funcionarios)

                print('Funcionário cadastrado com sucesso!\n')

            # ========================== EDITAR FUNCIONÁRIO ================================================= #
            elif op_funcionario == '2':
                print(cabecalho('EDITAR FUNCIONÁRIO'))

                try:
                    texto_arquivo_func = abrir_arquivo_leitura('funcionarios.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_func = input('Digite a matrícula de um funcionário para editar:')
                encontrado = False
                op_editar = ''
                while op_editar != '-1':

                    for i in range(len(texto_arquivo_func)):
                        if busca_func in texto_arquivo_func[i]:
                            encontrado = True
                            op_editar = input(f'Selecione a opção desejada para alterar o cadastro de funcionário: \n'
                                              f'\n'
                                              f'1 - Nome\n'
                                              f'2 - Matrícula\n'
                                              f'3 - Data Admissão\n'
                                              f'4 - Data Nascimento\n'
                                              f'-1 - Sair\n')
                            if op_editar == '1':
                                novo_nome = input('Digite novo nome:').title()
                                texto_arquivo_func[i - 1] = novo_nome + '\n'
                                print('Novo nome alterado com sucesso!')

                            elif op_editar == '2':
                                nova_matricula = input('Digite nova matrícula: ')
                                texto_arquivo_func[i] = ' Matrícula: ' + nova_matricula + '\n'
                                busca_func = texto_arquivo_func[i]
                                print('Matrícula alterada com sucesso!\n')

                            elif op_editar == '3':
                                nova_data = input('Digite nova data de admissão:')
                                data_format_admi = converter_data_nascimento_de_string_para_int(nova_data)
                                texto_arquivo_func[i + 1] = ' Data de Admissão: ' + nova_data + '\n'
                                print('Data de admissão alterada com sucesso!')

                            elif op_editar == '4':
                                nova_data = input('Digite a data de nascimento:')
                                data_format = converter_data_nascimento_de_string_para_int(nova_data)
                                idade = calculo_idade_usuario(data_format)
                                texto_arquivo_func[i + 2] = ' Data_Nascimento: ' + nova_data + '\n'
                                texto_arquivo_func[i + 3] = ' Idade: ' + str(idade) + '\n'
                                print('Data de nascimento alterada com sucesso!')

                            elif op_editar == '-1':
                                print('Informações salvas')

                    if encontrado:
                        escrita_arquivo('funcionarios.txt', texto_arquivo_func)
                    else:
                        print('Funcionário não encontrado\n')
                        break

            # ========================== REMOVER FUNCIONÁRIO ================================================= #
            elif op_funcionario == '3':
                print(cabecalho('REMOVER FUNCIONÁRIO'))

                try:
                    texto_arquivo_func = abrir_arquivo_leitura('funcionarios.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_func = input('Digite a matrícula do funcionário que deseja remover: ').title()
                encontrado = False
                for i in range(len(texto_arquivo_func)):
                    if busca_func in texto_arquivo_func[i]:
                        encontrado = True
                        del_op = input(f'Realmente deseja deletar o funcionário {texto_arquivo_func[i - 1].strip()}?\n'
                                       f'Digite "s" para SIM e "n" para NÃO: ').upper()
                        if del_op == 'S':
                            texto_arquivo_func[i - 1] = ''
                            for j in range(4):
                                texto_arquivo_func[i + j] = ''
                            print('Funcinário deletado!')
                        elif del_op == 'N':
                            print('Operação cancelada!')

                while '' in texto_arquivo_func:
                    texto_arquivo_func.remove('')

                if encontrado:
                    escrita_arquivo('funcionarios.txt', texto_arquivo_func)
                else:
                    print('Funcionário não encontrado\n')

            # ========================== BUSCAR FUNCIONÁRIO ================================================= #
            elif op_funcionario == '4':
                print(cabecalho('BUSCAR FUNCIONÁRIO'))

                try:
                    texto_arquivo_func = abrir_arquivo_leitura('funcionarios.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                encontrado = False
                op_busca = ''
                while op_busca != '-1':
                    op_busca = input(f'Gostaria de buscar por Matrícula ou Nome: \n'
                                     f'1 - Matrícula\n'
                                     f'2 - Nome\n'
                                     f'-1 - Sair\n')

                    if op_busca == '1':
                        busca_matricula = input('Digite a matricula: ')

                        for i in range(len(texto_arquivo_func)):
                            if busca_matricula in texto_arquivo_func[i]:
                                encontrado = True
                                print(texto_arquivo_func[i - 1].strip())
                                for j in range(4):
                                    print(texto_arquivo_func[i + j].strip())
                        if not encontrado:
                            print('Funcionário não encontrado')

                    elif op_busca == '2':
                        busca_nome = input('Digite o nome: ').title()
                        for i in range(len(texto_arquivo_func)):
                            if busca_nome in texto_arquivo_func[i]:
                                encontrado = True
                                for j in range(5):
                                    print(texto_arquivo_func[i + j].strip())
                        if not encontrado:
                            print('Funcionário não encontrado')

            # ========================== LISTAR FUNCIONÁRIO ================================================= #
            elif op_funcionario == '5':
                print(cabecalho('LISTAR FUNCIONÁRIO'))

                try:
                    arquivo_leitura_func = open('funcionarios.txt', 'r', encoding='utf8')
                    print(arquivo_leitura_func.read())
                    arquivo_leitura_func.close()
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

    # ========================== INICIO CRUD PRODUTOS ================================================= #
    elif op_sistema == '3':
        print(cabecalho('PRODUTOS') + '\n')
        categorias = ['Mercearia\n', 'Limpeza\n', 'Higiene Pessoal\n', 'Perecíveis\n', 'Outros\n']
        op_produtos = ''

        while op_produtos != '-1':
            op_produtos = input('\nEscolha uma das opções:\n'
                                f'1 - Cadastrar Produtos\n'
                                f'2 - Editar Produtos\n'
                                f'3 - Remover Produtos\n'
                                f'4 - Buscar Produtos\n'
                                f'5 - Listar Produtos\n'
                                f'6 - Listar Produtos por Categoria\n'
                                f'-1  Voltar ao menu principal\n')

            # ========================== CADASTRO PRODUTO ================================================= #
            if op_produtos == '1':
                print(cabecalho('CADASTRO PRODUTO'))

                nome = input('Nome do Produto: ').title()
                valor = input('Digite o valor: ')
                produto_categoria = listar_opcoes(categorias)
                if not produto_categoria:
                    print('Selecione a opção "Outros" caso não encontre a desejada!')
                    produto_categoria = listar_opcoes(categorias)

                quantidade = input('Digite a quantidade: ')
                dados_produtos = (f'{nome}\n '
                                  f'Categoria: {produto_categoria} '
                                  f'Valor: {valor}\n '
                                  f'Quantidade: {quantidade}\n')

                append_em_arquivo('produtos.txt', dados_produtos)

                print('Produto cadastrado com sucesso!\n')

            # ========================== EDITAR PRODUTO ================================================= #
            elif op_produtos == '2':
                print(cabecalho('EDITAR PRODUTO'))

                try:
                    texto_arquivo_produto = abrir_arquivo_leitura('produtos.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_produto = input('Busque um produto para editar: ').title()
                encontrado = False
                op_editar = ''
                while op_editar != '-1':
                    for i in range(len(texto_arquivo_produto)):
                        if busca_produto in texto_arquivo_produto[i]:
                            encontrado = True
                            op_editar = input(f'Selecione a opção desejada para alterar o cadastro de produtos: \n'
                                              f'1 - Nome\n'
                                              f'2 - Categoria\n'
                                              f'3 - Valor\n'
                                              f'4 - Quantidade\n'
                                              f'-1 - Sair\n')
                            if op_editar == '1':
                                novo_nome = input('Digite o nome: ').title()
                                texto_arquivo_produto[i] = novo_nome + '\n'
                                busca_produto = texto_arquivo_produto[i]
                                print('Nome alterado com sucesso!')

                            elif op_editar == '2':
                                nova_categoria = listar_opcoes(categorias)
                                if not nova_categoria:
                                    print('Selecione a opção "Outros" caso não encontre a desejada!')
                                    nova_categoria = listar_opcoes(categorias)
                                texto_arquivo_produto[i + 1] = ' Categoria: ' + nova_categoria
                                print('Categoria alterada com sucesso!\n')

                            elif op_editar == '3':
                                novo_valor = input('Digite o novo valor: ')
                                texto_arquivo_produto[i + 2] = ' Valor: ' + novo_valor + '\n'
                                print('Valor alterado com sucesso!\n')

                            elif op_editar == '4':
                                nova_quantidade = input('Digite a quantidade: ')
                                texto_arquivo_produto[i + 3] = ' Quantidade: ' + nova_quantidade + '\n'
                                print('Quantidade alterada com sucesso!\n')

                            elif op_editar == '-1':
                                print('Informações salvas')
                    if encontrado:
                        escrita_arquivo('produtos.txt', texto_arquivo_produto)
                    else:
                        print('Produto não encontrado\n')
                        break

            # ========================== REMOVER PRODUTO ================================================= #
            elif op_produtos == '3':
                print(cabecalho('REMOVER PRODUTO'))
                try:
                    texto_arquivo_produto = abrir_arquivo_leitura('produtos.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_produto = input('Busque um produto para remover: ').title()
                encontrado = False

                for i in range(len(texto_arquivo_produto)):
                    if busca_produto in texto_arquivo_produto[i]:
                        encontrado = True
                        del_op = input(f'Deseja realmente deletar?\n'
                                       f'Digite "s" para SIM e "n" para NÃO: ').upper()
                        if del_op == 'S':
                            for j in range(4):
                                texto_arquivo_produto[i + j] = ''

                            print('Produto deletado!\n')

                        elif del_op == 'N':
                            print('Operação cancelada!\n')

                while '' in texto_arquivo_produto:
                    texto_arquivo_produto.remove('')
                if encontrado:
                    escrita_arquivo('produtos.txt', texto_arquivo_produto)
                else:
                    print('Produto não encontrado\n')

            # ========================== BUSCAR PRODUTO ================================================= #
            elif op_produtos == '4':
                print(cabecalho('BUSCAR PRODUTOS'))

                try:
                    texto_arquivo_produto = abrir_arquivo_leitura('produtos.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_produto = input('Busque um produto: ').title()
                encontrado = False

                for i in range(len(texto_arquivo_produto)):
                    if busca_produto in texto_arquivo_produto[i]:
                        encontrado = True
                        for j in range(4):
                            print(texto_arquivo_produto[i + j].strip())

                if not encontrado:
                    print('Produto não encontrado \n')

            # ========================== LISTAR PRODUTOS ================================================= #
            elif op_produtos == '5':
                print(cabecalho('LISTAR PRODUTOS'))

                try:
                    arquivo_leitura_produto = open('produtos.txt', 'r', encoding='utf8')
                    print(arquivo_leitura_produto.read())
                    arquivo_leitura_produto.close()
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

            # ========================== LISTAR PRODUTOS ================================================= #
            elif op_produtos == '6':
                print(cabecalho('LISTAR PRODUTOS POR CATEGORIA'))

                try:
                    texto_arquivo_produto = abrir_arquivo_leitura('produtos.txt')
                except FileNotFoundError:
                    print('Arquivo não encontrado!')

                busca_categoria = listar_opcoes(categorias)
                if not busca_categoria:
                    print('Selecione a opção "Outros" caso não encontre a desejada!')
                    busca_categoria = listar_opcoes(categorias)

                encontrado = False
                for i in range(len(texto_arquivo_produto)):
                    if busca_categoria in texto_arquivo_produto[i]:
                        encontrado = True
                        print(texto_arquivo_produto[i - 1].strip())
                if not encontrado:
                    print('Não há produto cadastrado nesta categoria!')


