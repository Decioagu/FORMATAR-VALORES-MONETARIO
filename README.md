# Criação de pacote em Python

O objetivo deste projeto foi criar uma aplicação em Python utilizando pacotes para disponibilizar no repositório Pypi. Os pacotes criado consiste em personalizar as cores do texto no terminal e transformar valores numérico em anotação monetária. Ex:. "101" em "R$101,00".

***
## moeda, cor

Description. 
Package moeda and package cor is used to:
	- cor
		__init__.py
	- moeda:
		- formata_moeda.py

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cor
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install moeda

```bash
pip install cor
pip install moeda
```

## Usage

```python

import cor
from moeda.formata_moeda import titulo, teste_float, resposta
```

## Author
Décio Santana de Aguiar

## License
[MIT](https://choosealicense.com/licenses/mit/)
