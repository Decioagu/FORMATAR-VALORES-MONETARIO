import cor  # pacote para personalizar cores do texto
from moeda.formata_moeda import titulo, teste_float, resposta  # pacote para tratamento de valores numérico

titulo('Entrada de dados monetários'.upper())  # formata texto

print()
valor = input(f'Digite um valor numérico: {cor.verde_claro}R${cor.limpar}').strip()
valor = teste_float(valor)
print()
resposta(valor)
print(f'{cor.azul_claro}Décio Santana deAguiar{cor.limpar}')

'''
valor(
    name="moeda",
    version="0.0.1",
    author="Decio Santana de Aguiar",
    author_email="decioagu@gmail.com",
    description="Analisa valores numéricos e retorna em formato monetário",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
'''