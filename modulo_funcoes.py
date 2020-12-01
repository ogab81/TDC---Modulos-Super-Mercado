from datetime import date


def cabecalho(titulo):

    titulo_format = '=' * 10 + titulo + '=' * 10
    return titulo_format


def calculo_idade_usuario(nascimento):

    hoje = date.today()
    return hoje.year - nascimento[2] - ((hoje.month, hoje.day) < (nascimento[1], nascimento[0]))


def check_formato_input_data_nascimento(data):

    if len(data) == 10 and data[2] == '-' and data[5] == '-' and \
            data[:2].isdigit() and data[3:5].isdigit() and data[6:].isdigit():
        return True
    return False


def converter_data_nascimento_de_string_para_int(data):

    while True:
        dia_mes_ano = []
        if check_formato_input_data_nascimento(data):
            dia_mes_ano = data.split('-')
            dia_mes_ano[0] = int(dia_mes_ano[0])
            dia_mes_ano[1] = int(dia_mes_ano[1])
            dia_mes_ano[2] = int(dia_mes_ano[2])
            break
        else:
            print(f"Formato inválido\n")
            data = input(f"Data de nascimento (dd-mm-aaaa): ")
            continue
    return dia_mes_ano


def listar_opcoes(lista):

    if not lista:
        return ''
    while True:
        for i in range(len(lista)):
            print(f"{i + 1} - {lista[i]}", end='')

        escolha = int(input(f"Selecione uma das opções ou 0 se não houver a opção desejada:\n"))

        if len(lista) >= escolha > 0:
            return lista[escolha - 1]

        elif escolha == 0:
            break
        else:
            print(f"Código inválido.\n")
        break


def abrir_arquivo_leitura(arquivo):

    arquivo_leitura = open(arquivo, 'r', encoding='utf8')
    texto_arquivo_leitura = arquivo_leitura.readlines()
    arquivo_leitura.close()
    return texto_arquivo_leitura


def append_em_arquivo(arquivo, dados):

    arquivo_open = open(arquivo, 'a', encoding='utf8')
    arquivo_open.write(dados)
    arquivo_open.close()


def escrita_arquivo(arquivo, texto_arquivo):

    arquivo_escrita = open(arquivo, 'w', encoding='utf8')
    arquivo_escrita.writelines(texto_arquivo)
    arquivo_escrita.close()

