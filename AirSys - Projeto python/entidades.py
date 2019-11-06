import sys


class Pessoa(object):
    def __init__(self):
        self.__nome = "sem nome"
        self.__numIdentidade = "sem numero de indentidade"
        self.__cpf = None
        self.__email = "sem email"

    def setNome(self, nome):
        self.__nome = nome

    def setNumIdetidade(self, numIdentidade):
        self.__numIdentidade = numIdentidade

    def setCPF(self, cpf):
        self.__cpf = cpf

    def setEmail(self, email):
        self.__email = email

    def getNome(self):
        return self.__nome

    def getNumIdentidade(self):
        return self.__numIdentidade

    def getCPF(self):
        return self.__cpf

    def getEmail(self):
        return self.__email


class Gerente(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__turno = "sem turno"

    def setTurno(self, turno):
        if turno != "manha" and turno != "tarde" and turno != "noite":
            print("ERRO! turno nao reconhecido")
            sys.exit(0)
        else:
            self.__turno = turno

    def getTurno(self):
        return self.__turno


class Funcionario(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__numDeVendas = 0
        self.__codigo = 0

    def setNumDeVendas(self, numvendas):
        if numvendas <= 0:
            print("ERRO! NUMERO INVALIDO")
            sys.exit(0)
        else:
            self.__numDeVendas = numvendas

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNumDeVendas(self):
        return self.__numDeVendas

    def getCodigo(self):
        return self.__codigo


class Cliente(Pessoa):
    """docstring for Cliente"""

    def __init__(self):
        Pessoa.__init__(self)
        self.__banco = "sem banco"
        self.__key = "0000"

    def setBanco(self, banco):
        self.__banco = banco

    def setKey(self, key):
        self.__key = key

    def getBanco(self):
        return self.__banco

    def getKey(self):
        return self.__key
