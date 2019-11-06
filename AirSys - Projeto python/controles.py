import sys
import pymongo
from configuracoes import getMongoDbURL
from entidades import Gerente, Funcionario, Cliente, Passagem


""" Os métodos destas classes deverão se conectar com o banco de dados,
não apenas gerenciar as listas"""

dbURI = getMongoDbURL()
mainDB = pymongo.MongoClient(dbURI)


class InterfaceListaEntidade:
    def registrarEntidade(nomeEntidade, listaEntidades,
                          dbEntidades, objEntidade, dictNewEntidade):

        checkEntidade = dbEntidades.find_one(
            {'nome': objEntidade.getNome()}
        )

        if objEntidade in listaEntidades:
            if checkEntidade is None:
                dbEntidades.insert_one(dictNewEntidade)
            return "{0} {1} ja registrado(a)".format(
                nomeEntidade, objEntidade.getNome()
            )
        else:
            if checkEntidade is not None:
                return "{0} {1} ja registrado(a)!".format(
                    nomeEntidade, objEntidade.getNome()
                )
            else:
                listaEntidades.append(objEntidade)
                dbEntidades.insert_one(dictNewEntidade)
                return "{0} {1} registrado(a)!".format(
                    nomeEntidade, objEntidade.getNome()
                )

    def removerEntidade(nomeEntidade, listaEntidades,
                        dbEntidades, objEntidade):

        checkEntidade = dbEntidades.find_one(
            {'nome': objEntidade.getNome()}
        )

        if objEntidade in listaEntidades:
            if checkEntidade is not None:
                dbEntidades.delete_one(
                    {'nome': objEntidade.getNome()}
                )
            listaEntidades.remove(objEntidade)
            return "{0} {1} removido(a)!".format(
                nomeEntidade, objEntidade.getNome()
            )
        else:
            if checkEntidade is not None:
                dbEntidades.delete_one(
                    {'nome': objEntidade.getNome()}
                )
                return "{0} {1} removido(a)!".format(
                    nomeEntidade, objEntidade.getNome()
                )
            return "{0} {1} nao encontrado(a)".format(
                nomeEntidade, objEntidade.getNome())


class ListaGerentes:
    """ docstring for ListaGerentes """

    def __init__(self):
        self.__gerentes = []
        self.dbGerentes = mainDB.airsys.gerentes

    def registrarGerente(self, gerente):
        newGerente = {
            'nome': gerente.getNome(),
            'numIdentidade': gerente.getNumIdentidade(),
            'cpf': gerente.getCPF(),
            'email': gerente.getEmail(),
            'turno': gerente.getTurno()
        }
        result = InterfaceListaEntidade.registrarEntidade(
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente,
            dictNewEntidade=newGerente
        )

        return result

    def removerGerente(self, gerente):

        result = InterfaceListaEntidade.removerEntidade(
            nomeEntidade="Gerente",
            listaEntidades=self.__gerentes,
            dbEntidades=self.dbGerentes,
            objEntidade=gerente
        )

        return result

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
        result = InterfaceListaEntidade.registrarEntidade(
            nomeEntidade="Funcionario",
            listaEntidades=self.__funcionarios,
            dbEntidades=self.dbFuncionarios,
            objEntidade=funcionario,
            dictNewEntidade=newFuncionario
        )

        return result

    def removerFuncionario(self, funcionario):
        checkFuncionario = self.dbFuncionarios.find_one(
            {'nome': funcionario.getNome()}
        )

        if funcionario in self.__funcionarios:

            if checkFuncionario is not None:
                self.dbFuncionarios.delete_one({'nome': funcionario.getNome()})
                return "Funcionario {0} removido!".format(
                    funcionario.getNome())

            else:
                self.__funcionarios.remove(funcionario)
                return "Funcionario {0} removido!".format(
                    funcionario.getNome())

            self.__funcionarios.remove(funcionario)

        else:

            if checkFuncionario is not None:
                self.dbFuncionarios.delete_one({'nome': funcionario.getNome()})
                return "Funcionario {0} removido!".format(
                    funcionario.getNome())

            else:
                return "Funcionario nao encontrado"

    def buscarFuncionario(self, funcionario):
        checkFuncionario = self.dbFuncionarios.find_one(
            {'nome': funcionario.getNome()}
        )

        if funcionario in self.__funcionarios:

            if checkFuncionario is not None:
                return self.__funcionarios[
                    self.__funcionarios.index(funcionario)
                ]
            else:

                newFuncionario = {
                    'codigo': funcionario.getCodigo(),
                    'nome': funcionario.getNome(),
                    'numIdentidade': funcionario.getNumIdentidade(),
                    'cpf': funcionario.getCPF(),
                    'email': funcionario.getEmail(),
                    'numeroDeVendas': funcionario.getNumDeVendas()
                }

                self.dbFuncionarios.insert_one(newFuncionario)
                return self.__funcionarios[
                    self.__funcionarios.index(funcionario)
                ]

        else:

            if checkFuncionario is not None:
                newFuncionario = Funcionario()

                newFuncionario.setNome(
                    checkFuncionario['nome']
                )

                newFuncionario.setNumIdetidade(
                    checkFuncionario['numIdentidade']
                )

                newFuncionario.setCPF(
                    checkFuncionario['cpf']
                )

                newFuncionario.setCodigo(
                    checkFuncionario['codigo']
                )

                newFuncionario.setEmail(
                    checkFuncionario['email']
                )

                newFuncionario.setNumDeVendas(
                    checkFuncionario['numeroDeVendas']
                )

                self.__funcionarios.append(newFuncionario)
                return newFuncionario

            else:
                return "Funcionario nao encontrado"


class ListaClientes:
    """ docstring for ListaClientes """

    def __init__(self):
        self.__clientes = []
        self.dbClientes = mainDB.airsys.clientes

    def registrarCliente(self, cliente):

        newCliente = {
            'key': cliente.getKey(),
            'nome': cliente.getNome(),
            'numIdentidade': cliente.getNumIdentidade(),
            'cpf': cliente.getCPF(),
            'email': cliente.getEmail(),
            'banco': cliente.getBanco()
        }

        result = InterfaceListaEntidade.registrarEntidade(
            nomeEntidade="Cliente",
            listaEntidades=self.__clientes,
            dbEntidades=self.dbClientes,
            objEntidade=cliente,
            dictNewEntidade=newCliente
        )

        return result

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
