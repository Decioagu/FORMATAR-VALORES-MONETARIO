from package_name import cor  # pacote para personalizar cores do texto
from package_name.moeda.formatar_moeda import titulo, teste_float, resposta  # pacote para tratamento de valores numérico

titulo('Entrada de dados monetários'.upper())  # formata texto

print()
valor = input(f'Digite um valor numérico: {cor.verde_claro}R${cor.limpar}').strip()
valor = teste_float(valor)
print()
resposta(valor)
print(f'{cor.azul_claro}Décio Santana deAguiar{cor.limpar}')
