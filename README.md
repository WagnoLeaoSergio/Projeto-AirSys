Projeto final da disciplina de Modelagem de Sistemas turma 2019-3.

![Version 0.1](https://img.shields.io/badge/version-1.0.0-brightgreen.svg?style=for-the-badge)

# Sobre o projeto

- O projeto tem como objetivo criar um sistema de gerenciameto de passagens a矇reas para um aeroporto.

- Dentro da branch master terao dois diretorios:
  1. AirSys_Projeto python: codigo-fonte em python3 do sistema.
  2. AirSys_executavel: Projeto compilado como executavel para windows.

# Pre requisitos (para executar o codigo-fonte)

- Python3

- PyMongo

`sudo python3 -m pip install pymongo[srv]`

- pyQt5 + QtDesigner

`sudo sudo apt-get install python3-pyqt5 `

`sudo apt-get install pyqt5-dev-tools `

`sudo apt-get install qttools5-dev-tools`

`designer`


# Observação

- Para configurar a conexão com o banco de dados MongoDB é necessário criar arquivo configuraçoes.py e implementar a função  getMongoDbURL() que retorna o URL do banco de dados para o sistema

- Depois de instaladas as dependencias basta executar o arquivo init.py