from modulo_funcoes import *

metodos_pagamento = ['Á Vista\n', 'Débito\n', 'Credito\n']
op_sistema, nota_individual = '', ''
texto_arquivo_clientes = abrir_arquivo_leitura('clientes.txt')
texto_arquivo_produtos = abrir_arquivo_leitura('produtos.txt')

# ========================== INICIO PROGRAMA ================================================= #
print(f'Bem-vindo ao Sistema de Vendas do Supermercado Super!\n')
while op_sistema != '-1':

    print(cabecalho('VENDAS'))
    op_sistema = input(
        f'1 - Iniciar Venda\n'
        f'-1 - Finalizar\n')

    # ========================== INICIO VENDA ================================================= #
    if op_sistema == '1':
        data_hoje = date.today()
        print(cabecalho(f'{data_hoje.day}-{data_hoje.month}-{data_hoje.year}') + '\n')
        data_formatada = str(data_hoje.day) + '-' + str(data_hoje.month) + '-' + str(data_hoje.year)

        texto_arquivo_func = abrir_arquivo_leitura('funcionarios.txt')
        print('Para iniciar a venda selecione sua matrícula, caso não encontre confira seu cadastro.\n')

        lista_matriculas = []
        for i in range(len(texto_arquivo_func)):
            if 'Matrícula' in texto_arquivo_func[i]:
                lista_matriculas.append(texto_arquivo_func[i])
        matricula_func = listar_opcoes(lista_matriculas)

        encontrado = False

        if matricula_func in texto_arquivo_func:
            cpf_cliente = ''
            nome_completo = ''
            while len(cpf_cliente) != 11:
                cpf_cliente = input('CPF do cliente: ')
                if len(cpf_cliente) != 11:
                    print('CPF invalido, tente novamente')
                else:
                    for i in range(len(texto_arquivo_clientes)):
                        if cpf_cliente in texto_arquivo_clientes[i]:
                            encontrado = True
                            print(f'Cliente: {texto_arquivo_clientes[i - 1]}')
                            # nome arquivo nota
                            nome_completo = texto_arquivo_clientes[i - 1]
                            nome_completo_split = texto_arquivo_clientes[i - 1].split()
                            nota_individual = '_'.join(nome_completo_split) + '_' + data_formatada + '.txt'

                    if not encontrado:
                        print('CPF não encontrado, verifique seu cadastro ou tente novamente')
                    else:
                        arquivo_nota_individual = open(nota_individual, 'w', encoding='utf8')
                        arquivo_venda = open('vendas.txt', 'a', encoding='utf8')
                        arquivo_venda.write(f'CLIENTE: {nome_completo}')

                        print('Para finalizar o registro dos produtos digite -1 no campo "Nome do Produto"')

                        nome_produto = ''
                        valor_total = 0.0
                        while nome_produto != '-1':

                            nome_produto = input('Digite o produto:').title()
                            if nome_produto == '-1':
                                break

                            quantidade = []
                            encontrado = False
                            for i in range(len(texto_arquivo_produtos)):
                                if nome_produto in texto_arquivo_produtos[i]:
                                    encontrado = True
                                    quantidade = texto_arquivo_produtos[i + 3].split()
                                    valor = texto_arquivo_produtos[i + 2].split()
                                    quantidade[1] = int(quantidade[1])
                                    valor[1] = float(valor[1])

                                    if quantidade[1] >= 1:
                                        unidades_produto = int(input('Unidades: '))
                                        if unidades_produto > quantidade[1]:
                                            print(f'Quantidade indisponível, temos {quantidade[1]} unidades em estoque!')
                                        else:
                                            quantidade[1] -= unidades_produto
                                            valor_por_produto = unidades_produto * valor[1]
                                            print(f'Total: R${valor_por_produto}')
                                            valor_total = valor_total + valor_por_produto

                                            texto_arquivo_produtos[i + 3] = ' Quantidade: ' + str(quantidade[1]) + '\n'
                                            arquivo_nota_individual.write(f'PRODUTO: {nome_produto} - '
                                                                          f'UNIDADES: {unidades_produto} - '
                                                                          f'VALOR UNIT:{valor[1]} - '
                                                                          f'TOTAL: {valor_por_produto}\n')
                                    else:
                                        print('Produto não disponível')
                            if encontrado:
                                escrita_arquivo('produtos.txt', texto_arquivo_produtos)
                            else:
                                print('Produto não cadastrado')

                        print('\nValor total da compra é de' + ' R${0:.2f}\n'.format(valor_total))
                        if valor_total == 0:
                            break
                        print('Escolha um meio de pagamento:')

                        escolha_pagamento = listar_opcoes(metodos_pagamento)

                        arquivo_nota_individual.write(f'Valor total: {valor_total}\n'
                                                      f'Pagamento: {escolha_pagamento}\n')
                        arquivo_nota_individual.close()

                        texto_arquivo_nota_individual = abrir_arquivo_leitura(nota_individual)
                        arquivo_venda.writelines(texto_arquivo_nota_individual)
                        arquivo_venda.close()
                        print('Compra finalizada!')
