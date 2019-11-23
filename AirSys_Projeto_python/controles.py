import pymongo
from configuracoes import getMongoDbURL
from entidades import Gerente, Funcionario, Cliente, Passagem

dbURI = getMongoDbURL()
mainDB = pymongo.MongoClient(dbURI)


class InterfaceListaEntidade:

    @staticmethod
    def _registrarEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                           dbEntidades, objEntidade, dictNewEntidade):

        if objEntidade is not None and codigoEntidade != objEntidade.getCodigo():
            return "ERRO! Codigo recebido e codigo do objeto diferentes"

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

    @staticmethod
    def _removerEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                         dbEntidades, objEntidade):
        if objEntidade is not None and codigoEntidade != objEntidade.getCodigo():
            return "ERRO! Codigo recebido e codigo do objeto diferentes"

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

    @staticmethod
    def _buscarEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                        dbEntidades, objEntidade, flag="normal"):
        if objEntidade is not None and codigoEntidade != objEntidade.getCodigo():
            return "ERRO! Codigo recebido e codigo do objeto diferentes"

        checkEntidade = dbEntidades.find_one(
            {'codigo': codigoEntidade}
        )

        if objEntidade is not None and objEntidade in listaEntidades:
            return listaEntidades[listaEntidades.index(objEntidade)]
        else:
            if checkEntidade is not None:
                if nomeEntidade == "Gerente":
                    newObjEntidade = Gerente()
                    newObjEntidade.setCodigo(checkEntidade["codigo"])
                    newObjEntidade.setNome(checkEntidade["nome"])
                    newObjEntidade.setNumIdetidade(
                        checkEntidade["numIdentidade"]
                    )
                    newObjEntidade.setCPF(checkEntidade["cpf"])
                    newObjEntidade.setEmail(checkEntidade["email"])
                    newObjEntidade.setTurno(checkEntidade["turno"])
                    newObjEntidade.setSenha(checkEntidade["senha"])
                elif nomeEntidade == "Funcionario":
                    newObjEntidade = Funcionario()
                    newObjEntidade.setCodigo(checkEntidade["codigo"])
                    newObjEntidade.setNome(checkEntidade["nome"])
                    newObjEntidade.setNumIdetidade(
                        checkEntidade["numIdentidade"]
                    )
                    newObjEntidade.setCPF(checkEntidade["cpf"])
                    newObjEntidade.setEmail(checkEntidade["email"])
                    newObjEntidade.setNumDeVendas(
                        checkEntidade["numeroDeVendas"]
                    )
                    newObjEntidade.setSenha(checkEntidade["senha"])

                elif nomeEntidade == "Cliente":
                    newObjEntidade = Cliente()
                    newObjEntidade.setCodigo(checkEntidade["codigo"])
                    newObjEntidade.setNome(checkEntidade["nome"])
                    newObjEntidade.setNumIdetidade(
                        checkEntidade["numIdentidade"]
                    )
                    newObjEntidade.setCPF(checkEntidade["cpf"])
                    newObjEntidade.setEmail(checkEntidade["email"])
                    newObjEntidade.setBanco(checkEntidade["banco"])
                elif nomeEntidade == "Passagem":
                    newObjEntidade = Passagem()
                    newObjEntidade.setCodigo(checkEntidade["codigo"])
                    newObjEntidade.setOrigem(checkEntidade["origem"])
                    newObjEntidade.setDestino(checkEntidade["destino"])
                    newObjEntidade.setCodigo(checkEntidade["codigo"])
                    newObjEntidade.setData(checkEntidade["data"])
                    newObjEntidade.setCompanhia(checkEntidade["companhia"])
                    newObjEntidade.setAssento(checkEntidade["assento"])
                    newObjEntidade.setEstado(checkEntidade["estado"])
                    newObjEntidade.setPreco(checkEntidade["preco"])
                    newObjEntidade.setDataCompra(checkEntidade["dataCompra"])

                listaEntidades.append(newObjEntidade)
                return listaEntidades[listaEntidades.index(newObjEntidade)]
            else:
                return None

    @staticmethod
    def _alterarEntidade(codigoEntidade, nomeEntidade, listaEntidades,
                         dbEntidades, campo, valor):
        entidade = InterfaceListaEntidade._buscarEntidade(
            codigoEntidade,
            nomeEntidade, listaEntidades,
            dbEntidades, None
        )
        if entidade is None:
            return "{0} nao encontrado".format(nomeEntidade)
        else:
            bibliotec = {"codigo": entidade.setCodigo}

            if nomeEntidade == "Gerente":
                bibliotec["nome"] = entidade.setNome
                bibliotec["numIdentidade"] = entidade.setNumIdetidade
                bibliotec["cpf"] = entidade.setCPF
                bibliotec["email"] = entidade.setEmail
                bibliotec["senha"] = entidade.setSenha
                bibliotec["turno"] = entidade.setTurno
            elif nomeEntidade == "Funcionario":
                bibliotec["nome"] = entidade.setNome
                bibliotec["numIdentidade"] = entidade.setNumIdetidade
                bibliotec["cpf"] = entidade.setCPF
                bibliotec["email"] = entidade.setEmail
                bibliotec["numeroDeVendas"] = entidade.setNumDeVendas
            elif nomeEntidade == "Cliente":
                bibliotec["nome"] = entidade.setNome
                bibliotec["numIdentidade"] = entidade.setNumIdetidade
                bibliotec["cpf"] = entidade.setCPF
                bibliotec["email"] = entidade.setEmail
                bibliotec["banco"] = entidade.setBanco
            elif nomeEntidade == "Passagem":
                bibliotec["origem"] = entidade.setOrigem
                bibliotec["destino"] = entidade.setDestino
                bibliotec["data"] = entidade.setData
                bibliotec["companhia"] = entidade.setCompanhia
                bibliotec["assento"] = entidade.setAssento
                bibliotec["estado"] = entidade.setEstado
                bibliotec["preco"] = entidade.setPreco
                bibliotec["dataCompra"] = entidade.setDataCompra

            checkEntidade = dbEntidades.find_one(
                {'codigo': codigoEntidade}
            )

            checkEntidade[campo] = valor

            InterfaceListaEntidade._removerEntidade(
                codigoEntidade,
                nomeEntidade,
                listaEntidades,
                dbEntidades,
                entidade
            )

            bibliotec[campo](valor)

            dictEntidade = checkEntidade

            InterfaceListaEntidade._registrarEntidade(
                codigoEntidade,
                nomeEntidade,
                listaEntidades,
                dbEntidades,
                entidade,
                dictEntidade
            )

            return 1

    @staticmethod
    def _listarTodos(nomeEntidade, dbEntidades):
        todos = []
        i = 0
        cursor = dbEntidades.find({})
        for document in cursor:
            todos.append({"element{0}".format(i): document})
            i = i + 1
        return todos


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
            'turno': gerente.getTurno(),
            'senha': gerente.getSenha()
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
            objEntidade=gerente,
        )
        return result

    def alterarGerente(self, codigo, campo, valor):
        result = InterfaceListaEntidade._alterarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            campo=campo,
            valor=valor
        )
        return result

    def listarGerentes(self):
        result = InterfaceListaEntidade._listarTodos(
            nomeEntidade="Gerente",
            dbEntidades=self.dbGerentes
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
            'numeroDeVendas': funcionario.getNumDeVendas(),
            'senha': funcionario.getSenha()
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

    def alterarFuncionario(self, codigo, campo, valor):
        result = InterfaceListaEntidade._alterarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            campo=campo,
            valor=valor
        )

        return result

    def listarFuncionarios(self):
        result = InterfaceListaEntidade._listarTodos(
            nomeEntidade="Funcionario",
            dbEntidades=self.dbFuncionarios
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

    def alterarCliente(self, codigo, campo, valor):
        result = InterfaceListaEntidade._alterarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            campo=campo,
            valor=valor
        )

        return result

    def listarClientes(self):
        result = InterfaceListaEntidade._listarTodos(
            nomeEntidade="Cliente",
            dbEntidades=self.dbClientes
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

    def alterarPassagem(self, codigo, campo, valor):
        result = InterfaceListaEntidade._alterarEntidade(
            codigoEntidade=codigo,
            nomeEntidade="Passagem",
            listaEntidades=self.__passagens,
            dbEntidades=self.dbPassagens,
            campo=campo,
            valor=valor
        )

        return result

    def listarPassagens(self):
        result = InterfaceListaEntidade._listarTodos(
            nomeEntidade="Passagem",
            dbEntidades=self.dbPassagens
        )
        return result
