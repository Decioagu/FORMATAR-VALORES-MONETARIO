from package_name import cor  # pacote para personalizar cores do texto

def titulo(txt):
    """
    Formata texto em um padrão em caixa

    :param txt: Variável em texto para formatar
    :return: Retorna texto formatado em caixa
    """
    print(f'{cor.azul_claro}={cor.limpar}' * (len(txt) + 4))
    print(f'{cor.azul_claro}= {cor.roxo}{txt} {cor.azul_claro}={cor.limpar}')
    print(f'{cor.azul_claro}={cor.limpar}' * (len(txt) + 4))


def teste_float(num):
    """
    Testa caractere e permanece em loop infinito até usuário
    digitar um valor numérico valida. Variável numérica testada pode ser
    escrita por "." ou "," exemplo: "4.29" ou "4,29"

    :param num: Variável a ser testada
    :return: Retorna valores numéricos validos do tipo 'float'
    """
    while True:
        num = num.replace(',', '.')
        teste = num
        if num == '':
            num = input(f'Digite um valor numérico: {cor.verde_claro}R${cor.limpar}').strip()
        else:
            if teste.count('.') <= 1:
                teste = teste.replace('.', '')
                if teste.isnumeric() == True:
                    num = float(num)
                    break
                else:
                    print()
                    print(f'{cor.vermelho_claro}Erro...{cor.limpar}')
                    print(f'{cor.amarelo_claro}Caractere "{cor.vermelho_claro}{num}{cor.amarelo_claro}" não é valido.{cor.limpar}')
                    print()
                    num = input(f'Digite um valor numérico: {cor.verde_claro}R${cor.limpar}').strip()
            # caso pontuação seja maior que 1 retornar loop, Ex: "10,,0" ou "10...0"
            else:
                print()
                print(f'{cor.vermelho_claro}Erro...{cor.limpar}')
                print(f'{cor.amarelo_claro}Caractere "{cor.vermelho_claro}{num}{cor.amarelo_claro}" não é valido.{cor.limpar}')
                print()
                num = input(f'Digite um valor numérico: {cor.verde_claro}R${cor.limpar}').strip()
    return num


def moeda(valor, moeda='R$'):
    """
    Formata na impressão um Valor Numérico em Moeda
    Ex: Valor Numérico= 3.50 para Moeda= R$3,50

    :param valor: Valor Numérico a ser formatado
    :param moeda: Adiciona simbolo desejado=> Ex: R$
    :return: Retorna valor formatado em valores monetário, Ex: R$12,01
    """
    return f'{cor.verde_claro}{moeda}{valor:.2f}{cor.limpar}'.replace('.', ',')


def metade(valor):
  res = valor / 2
  return moeda(res)


def dobro(valor):
    res = valor * 2
    return moeda(res)


def aumento(valor, taxa):
    res = valor + (valor * taxa)/100
    return moeda(res)


def reducao(valor, taxa):
    res = valor - (valor * taxa)/100
    return moeda(res)

# Respostas
def resposta(valor, taxa_aumento=20, taxa_reducao=10):
    titulo('RESUMO DOS VALORES'.center(27))
    print(f'Valor inserido: {moeda(valor)}')
    print(f'{cor.azul_claro}-{cor.limpar}' * 31)
    print(f'{cor.roxo}Metade{cor.limpar} do valor: {metade(valor)}')
    print(f'{cor.roxo}Dobro{cor.limpar} do valor: {dobro(valor)}')
    print(f'{cor.roxo}Aumento{cor.limpar} de {cor.amarelo_claro}{taxa_aumento}%{cor.limpar}: {aumento(valor, taxa_aumento)}')
    print(f'{cor.roxo}Redução{cor.limpar} de {cor.amarelo_claro}{taxa_reducao}%{cor.limpar}: {reducao(valor, taxa_reducao)}')
    print(f'{cor.azul_claro}-{cor.limpar}' * 31)

