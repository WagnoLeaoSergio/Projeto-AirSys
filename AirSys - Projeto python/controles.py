import sys
from entidades import Gerente, Funcionario, Cliente, Passagem


""" Os métodos destas classes deverão se conectar com o banco de dados,
não apenas gerenciar as listas"""


class ListaGerentes:
    """ docstring for ListaGerentes """

    def __init__(self):
        self.__gerentes = []

    def registrarGerente(self, gerente):
        if gerente in self.__gerentes:
            print("Gerente ja incluido na lista")
            return 0
        else:
            self.__gerentes.append(gerente)
            print("Gerente {0} registrado!".format(gerente.getNome()))

    def removerGerente(self, gerente):
        if gerente not in self.__gerentes:
            print("Gerente não encotrado na lista")
            return 0
        else:
            self.__gerentes.remove(gerente)
            print("Gerente {0} removido!".format(gerente.getNome()))

    def buscarGerente(self, gerente):
        if gerente in self.__gerentes:
            return self.__gerentes[self.__gerentes.index(gerente)]
        else:
            print("Gerente não encotrado na lista")
            return 0


class ListaFuncionarios:
    """ docstring for ListaFuncionarios """

    def __init__(self):
        self.__funcionarios = []

    def registrarFuncionario(self, funcionario):
        if funcionario in self.__funcionarios:
            print("Funcionario ja incluido na lista")
            return 0
        else:
            self.__funcionarios.append(funcionario)
            print("Funcionario {0} registrado!".format(funcionario.getNome()))

    def removerFuncionario(self, funcionario):
        if funcionario not in self.__funcionarios:
            print("Funcionario não encotrado na lista")
            return 0
        else:
            self.__funcionarios.remove(funcionario)
            print("Funcionario {0} removido!".format(funcionario.getNome()))

    def buscarFuncionario(self, funcionario):
        if funcionario in self.__funcionarios:
            return self.__funcionarios[self.__funcionarios.index(funcionario)]
        else:
            print("Funcionario não encotrado na lista")
            return 0


class ListaClientes:
    """ docstring for ListaClientes """

    def __init__(self):
        self.__clientes = []

    def registrarCliente(self, cliente):
        if cliente in self.__clientes:
            print("Cliente ja incluido na lista")
            return 0
        else:
            self.__clientes.append(cliente)
            print("Cliente {0} registrado!".format(cliente.getNome()))

    def removerCliente(self, cliente):
        if cliente not in self.__clientes:
            print("Cliente não encotrado na lista")
            return 0
        else:
            self.__clientes.remove(cliente)
            print("Cliente {0} removido!".format(cliente.getNome()))

    def buscarCliente(self, cliente):
        if cliente in self.__clientes:
            return self.__clientes[self.__clientes.index(cliente)]
        else:
            print("Cliente não encotrado na lista")
            return 0


class ListaPassagens:
    """ docstring for ListaPassagens """

    def __init__(self):
        self.__passagens = []

    def registrarPassagem(self, passagem):
        if passagem in self.__passagens:
            print("Passagem ja incluida na lista")
            return 0
        else:
            self.__passagens.append(passagem)
            print("Passagem {0} registrada!".format(passagem.getCod()))

    def removerPassagem(self, passagem):
        if passagem not in self.__passagens:
            print("Passagem não encotrada na lista")
            return 0
        else:
            self.__passagens.remove(passagem)
            print("Passagem {0} removida!".format(passagem.getCod()))

    def buscarPassagem(self, passagem):
        if passagem in self.__passagens:
            return self.__passagens[self.__passagens.index(passagem)]
        else:
            print("Passagem nao encontrada")
            return 0
