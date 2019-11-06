import sys


class Pessoa(object):
    """docstring for Pessoa"""
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
    """docstring for Gerente"""
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
    """docstring for Funcionario"""

    def __init__(self):
        Pessoa.__init__(self)
        self.__numDeVendas = 0
        self.__codigo = 0

    def setNumDeVendas(self, numvendas):
        if numvendas < 0:
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


class Passagem():
    """docstring for Passagem"""

    def __init__(self):
        self.__origem = "sem origem"
        self.__destino = "sem destino"
        self.__data = "sem data"
        self.__companhia = "sem companhia"
        self.__assento = "assento nao selecionado"
        self.__estado = " nulo "
        self.__preco = 0.0
        self.__dataCompra = "sem data de compra"

    def setOrigem(self, origem):
        self.__origem = origem

    def setDestino(self, destino):
        self.__destino = destino

    def setData(self, data):
        self.__data = data

    def setCompanhia(self, companhia):
        self.__companhia = companhia

    def setAssento(self, assento):
        self.__assento = assento

    def setEstado(self, estado):
        self.__estado = estado

    def setPreco(self, preco):
        self.__preco = preco

    def setDataCompra(self, dataCompra):
        self.__dataCompra = dataCompra

    def getOrigem(self):
        return self.__origem

    def getDestino(self):
        return self.__destino

    def getData(self):
        return self.__data

    def getCompanhia(self):
        return self.__companhia

    def getAssento(self):
        return self.__assento

    def getEstado(self):
        return self.__estado

    def getPreco(self):
        return self.__preco

    def getDataCompra(self):
        return self.__dataCompra
