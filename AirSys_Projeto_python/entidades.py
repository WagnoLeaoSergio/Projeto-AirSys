import sys


class Pessoa(object):
    """docstring for Pessoa"""

    def __init__(self):
        self.__codigo = "00000"
        self.__nome = "sem nome"
        self.__numIdentidade = "sem numero de indentidade"
        self.__cpf = None
        self.__email = "sem email"

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNome(self, nome):
        self.__nome = nome

    def setNumIdetidade(self, numIdentidade):
        self.__numIdentidade = numIdentidade

    def setCPF(self, cpf):
        self.__cpf = cpf

    def setEmail(self, email):
        self.__email = email

    def getCodigo(self):
        return self.__codigo

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
        self.__senha = 0

    def setTurno(self, turno):
        turnos = ["manha", "tarde", "noite", "sem turno"]
        if turno not in turnos:
            return "ERRO! turno nao reconhecido"
        else:
            self.__turno = turno

    def getTurno(self):
        return self.__turno

    def setSenha(self, senha):
        self.__senha = senha

    def getSenha(self):
        return self.__senha


class Funcionario(Pessoa):
    """docstring for Funcionario"""

    def __init__(self):
        Pessoa.__init__(self)
        self.__numDeVendas = 0
        self.__senha = 0

    def setNumDeVendas(self, numvendas):
        if numvendas < 0:
            return "ERRO! NUMERO INVALIDO"
        else:
            self.__numDeVendas = numvendas

    def getNumDeVendas(self):
        return self.__numDeVendas

    def setSenha(self, senha):
        self.__senha = senha

    def getSenha(self):
        return self.__senha


class Cliente(Pessoa):
    """docstring for Cliente"""

    def __init__(self):
        Pessoa.__init__(self)
        self.__banco = "sem banco"

    def setBanco(self, banco):
        self.__banco = banco

    def getBanco(self):
        return self.__banco


class Passagem():
    """docstring for Passagem"""

    def __init__(self):
        self.__codigo = "00000"
        self.__origem = "sem origem"
        self.__destino = "sem destino"
        self.__data = "sem data"
        self.__companhia = "sem companhia"
        self.__assento = "assento nao selecionado"
        self.__estado = " nulo "
        self.__preco = 0.0
        self.__dataCompra = "sem data de compra"

    def setCodigo(self, codigo):
        self.__codigo = codigo

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

    def getCodigo(self):
        return self.__codigo

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
