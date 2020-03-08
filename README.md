### Nossa Casa do Código :books:

#### Requisitos iniciais

- [Python3](https://www.python.org/downloads/)
- Gerenciador de pacotes do python(**PIP**)

#### Preparando o ambiente

- Clone este repositório
- Navegue até a branch `setup`: `git checkout setup`
- Crie o ambiente virtual
  `python -m venv .venv`
- Ative o ambiente virtual
  `source .venv/bin/activate`
- Instale as dependências
  `pip install -r requirements.txt`

Para testar este setup, entre na **pasta src** e execute o arquivo `main.py` com o comando:
`python3 main.py`

**Caso esteja no windows os passos para ativar o ambiente virtual é diferente, tente algo como:**

![Venv](https://user-images.githubusercontent.com/41811634/75418237-c2753a00-5911-11ea-982c-0ce8435c44bc.png)

**Obs:** para sair do ambiente virtual basta digitar:
`deactivate`

#### Executando o código

- Lembre-se de atualizar as dependências necessárias: `pip install -r requirements.txt`
- Caso esteja utilizando o pycharm é simples, basta instalar as bibliotecas que ele mostrar que estão ausentes e clicar em run
- Caso esteja utilizando o terminal, terá que fazer o seguinte:
  - **Ative o ambiente virtual**: `source .venv/bin/activate`
  - Para compilar a main dos autores, na pasta raiz do projeto digite: `python3 -m src.authors.main`
  - Para compilar os testes, também na pasta raiz, digite: `python3 -m pytest`
