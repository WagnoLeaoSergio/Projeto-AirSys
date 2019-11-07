import pymongo
from configuracoes import getMongoDbURL
from entidades import Gerente, Funcionario, Cliente, Passagem

dbURI = getMongoDbURL()
mainDB = pymongo.MongoClient(dbURI)


class InterfaceListaEntidade:
    def _registrarEntidade(nomeEntidade, listaEntidades,
                            dbEntidades, objEntidade, dictNewEntidade):

        checkEntidade = dbEntidades.find_one(
            {'codigo': objEntidade.getCodigo()}
        )

        if objEntidade in listaEntidades:
            if checkEntidade is None:
                dbEntidades.insert_one(dictNewEntidade)
            return "{0} {1} ja registrado(a)".format(
                nomeEntidade, objEntidade.getCodigo()
            )
        else:
            if checkEntidade is not None:
                return "{0} {1} ja registrado(a)!".format(
                    nomeEntidade, objEntidade.getCodigo()
                )
            else:
                listaEntidades.append(objEntidade)
                dbEntidades.insert_one(dictNewEntidade)
                return "{0} {1} registrado(a)!".format(
                    nomeEntidade, objEntidade.getCodigo()
                )

    def _removerEntidade(nomeEntidade, listaEntidades,
                          dbEntidades, objEntidade):

        checkEntidade = dbEntidades.find_one(
            {'codigo': objEntidade.getCodigo()}
        )

        if objEntidade in listaEntidades:
            if checkEntidade is not None:
                dbEntidades.delete_one(
                    {'codigo': objEntidade.getCodigo()}
                )
            listaEntidades.remove(objEntidade)
            return "{0} {1} removido(a)!".format(
                nomeEntidade, objEntidade.getCodigo()
            )
        else:
            if checkEntidade is not None:
                dbEntidades.delete_one(
                    {'codigo': objEntidade.getCodigo()}
                )
                return "{0} {1} removido(a)!".format(
                    nomeEntidade, objEntidade.getCodigo()
                )
            return "{0} {1} nao encontrado(a)".format(
                nomeEntidade, objEntidade.getCodigo())

    def _buscarEntidade(nomeEntidade, listaEntidades,
                         dbEntidades, objEntidade):

        checkEntidade = dbEntidades.find_one(
            {'codigo': objEntidade.getCodigo()}
        )

        if objEntidade in listaEntidades:
            return listaEntidades[listaEntidades.index(objEntidade)]
        else:
            if checkEntidade is not None:
                listaEntidades.append(objEntidade)
                return listaEntidades[listaEntidades.index(objEntidade)]
            else:
                return None


class ListaGerentes:
    """ docstring for ListaGerentes """

    def __init__(self):
        self.__gerentes = []
        self.dbGerentes = mainDB.airsys.gerentes

    def registrarGerente(self, gerente):
        newGerente = {
            'codigo': gerente.getCodigo(),
            'nome': gerente.getNome(),
            'numIdentidade': gerente.getNumIdentidade(),
            'cpf': gerente.getCPF(),
            'email': gerente.getEmail(),
            'turno': gerente.getTurno()
        }
        result = InterfaceListaEntidade._registrarEntidade(
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente,
            dictNewEntidade=newGerente
        )

        return result

    def removerGerente(self, gerente):

        result = InterfaceListaEntidade._removerEntidade(
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente
        )

        return result

    def buscarGerente(self, gerente):

        result = InterfaceListaEntidade._buscarEntidade(
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente
        )

        return result


class ListaFuncionarios:
    """ docstring for ListaFuncionarios """

    def __init__(self):
        self.__funcionarios = []
        self.dbFuncionarios = mainDB.airsys.funcionarios

    def registrarFuncionario(self, funcionario):
        newFuncionario = {
            'codigo': funcionario.getCodigo(),
            'nome': funcionario.getNome(),
            'numIdentidade': funcionario.getNumIdentidade(),
            'cpf': funcionario.getCPF(),
            'email': funcionario.getEmail(),
            'numeroDeVendas': funcionario.getNumDeVendas()
        }
        result = InterfaceListaEntidade._registrarEntidade(
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            objEntidade=funcionario,
            dictNewEntidade=newFuncionario
        )

        return result

    def removerFuncionario(self, funcionario):
        result = InterfaceListaEntidade._removerEntidade(
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            objEntidade=funcionario
        )

        return result

    def buscarFuncionario(self, funcionario):
        result = InterfaceListaEntidade._buscarEntidade(
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            objEntidade=funcionario
        )

        return result


class ListaClientes:
    """ docstring for ListaClientes """

    def __init__(self):
        self.__clientes = []
        self.dbClientes = mainDB.airsys.clientes

    def registrarCliente(self, cliente):

        newCliente = {
            'codigo': cliente.getCodigo(),
            'nome': cliente.getNome(),
            'numIdentidade': cliente.getNumIdentidade(),
            'cpf': cliente.getCPF(),
            'email': cliente.getEmail(),
            'banco': cliente.getBanco()
        }

        result = InterfaceListaEntidade._registrarEntidade(
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            objEntidade=cliente,
            dictNewEntidade=newCliente
        )

        return result

    def removerCliente(self, cliente):
        result = InterfaceListaEntidade._removerEntidade(
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            objEntidade=cliente
        )

        return result

    def buscarCliente(self, cliente):
        result = InterfaceListaEntidade._buscarEntidade(
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            objEntidade=cliente
        )

        return result


class ListaPassagens:
    """ docstring for ListaPassagens """

    def __init__(self):
        self.__passagens = []
        self.dbPassagens = mainDB.airsys.passagens

    def registrarPassagem(self, passagem):
        newPassagem = {
            'codigo': passagem.getCodigo(),
            'origem': passagem.getOrigem(),
            'destino': passagem.getDestino(),
            'data': passagem.getData(),
            'companhia': passagem.getCompanhia(),
            'assento': passagem.getAssento(),
            'estado': passagem.getEstado(),
            'preco': passagem.getPreco(),
            'dataCompra': passagem.getDataCompra()
        }

        result = InterfaceListaEntidade._registrarEntidade(
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            objEntidade=passagem,
            dictNewEntidade=newPassagem
        )

        return result

    def removerPassagem(self, passagem):
        result = InterfaceListaEntidade._removerEntidade(
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            objEntidade=passagem
        )

        return result

    def buscarPassagem(self, passagem):
        result = InterfaceListaEntidade._buscarEntidade(
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            objEntidade=passagem
        )

        return result
