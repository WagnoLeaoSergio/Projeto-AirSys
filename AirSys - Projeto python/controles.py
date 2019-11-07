import pymongo
from configuracoes import getMongoDbURL
from entidades import Gerente, Funcionario, Cliente, Passagem

dbURI = getMongoDbURL()
mainDB = pymongo.MongoClient(dbURI)


class InterfaceListaEntidade:
    def _registrarEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                           dbEntidades, objEntidade, dictNewEntidade):

        checkEntidade = dbEntidades.find_one(
            {'codigo': codigoEntidade}
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

    def _removerEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                         dbEntidades, objEntidade):

        checkEntidade = dbEntidades.find_one(
            {'codigo': codigoEntidade}
        )

        if objEntidade in listaEntidades:
            if checkEntidade is not None:
                dbEntidades.delete_one(
                    {'codigo': codigoEntidade}
                )
            listaEntidades.remove(objEntidade)
            return "{0} {1} removido(a)!".format(
                nomeEntidade, objEntidade.getCodigo()
            )
        else:
            if checkEntidade is not None:
                dbEntidades.delete_one(
                    {'codigo': codigoEntidade}
                )
                return "{0} {1} removido(a)!".format(
                    nomeEntidade, objEntidade.getCodigo()
                )
            return "{0} {1} nao encontrado(a)".format(
                nomeEntidade, objEntidade.getCodigo())

    def _buscarEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                        dbEntidades, objEntidade):

        checkEntidade = dbEntidades.find_one(
            {'codigo': codigoEntidade}
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

    def registrarGerente(self, codigo, gerente=None):
        newGerente = {
            'codigo': gerente.getCodigo(),
            'nome': gerente.getNome(),
            'numIdentidade': gerente.getNumIdentidade(),
            'cpf': gerente.getCPF(),
            'email': gerente.getEmail(),
            'turno': gerente.getTurno()
        }
        result = InterfaceListaEntidade._registrarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente,
            dictNewEntidade=newGerente
        )

        return result

    def removerGerente(self, codigo, gerente=None):

        result = InterfaceListaEntidade._removerEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente
        )

        return result

    def buscarGerente(self, codigo, gerente=None):

        result = InterfaceListaEntidade._buscarEntidade(
            codigoEntidade=codigo,
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

    def registrarFuncionario(self, codigo, funcionario=None):
        newFuncionario = {
            'codigo': funcionario.getCodigo(),
            'nome': funcionario.getNome(),
            'numIdentidade': funcionario.getNumIdentidade(),
            'cpf': funcionario.getCPF(),
            'email': funcionario.getEmail(),
            'numeroDeVendas': funcionario.getNumDeVendas()
        }
        result = InterfaceListaEntidade._registrarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            objEntidade=funcionario,
            dictNewEntidade=newFuncionario
        )

        return result

    def removerFuncionario(self, codigo, funcionario=None):
        result = InterfaceListaEntidade._removerEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            objEntidade=funcionario
        )

        return result

    def buscarFuncionario(self, codigo, funcionario=None):
        result = InterfaceListaEntidade._buscarEntidade(
            codigoEntidade=codigo,
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

    def registrarCliente(self, codigo, cliente=None):

        newCliente = {
            'codigo': cliente.getCodigo(),
            'nome': cliente.getNome(),
            'numIdentidade': cliente.getNumIdentidade(),
            'cpf': cliente.getCPF(),
            'email': cliente.getEmail(),
            'banco': cliente.getBanco()
        }

        result = InterfaceListaEntidade._registrarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            objEntidade=cliente,
            dictNewEntidade=newCliente
        )

        return result

    def removerCliente(self, codigo, cliente=None):
        result = InterfaceListaEntidade._removerEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            objEntidade=cliente
        )

        return result

    def buscarCliente(self, codigo, cliente=None):
        result = InterfaceListaEntidade._buscarEntidade(
            codigoEntidade=codigo,
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

    def registrarPassagem(self, codigo, passagem=None):
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
            codigoEntidade=codigo,
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            objEntidade=passagem,
            dictNewEntidade=newPassagem
        )

        return result

    def removerPassagem(self, codigo, passagem=None):
        result = InterfaceListaEntidade._removerEntidade(
            codigo=codigo,
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            objEntidade=passagem
        )

        return result

    def buscarPassagem(self, codigo, passagem=None):
        result = InterfaceListaEntidade._buscarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            objEntidade=passagem
        )

        return result
