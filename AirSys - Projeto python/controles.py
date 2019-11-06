import sys
import pymongo
from configuracoes import getMongoDbURL
from entidades import Gerente, Funcionario, Cliente, Passagem


""" Os métodos destas classes deverão se conectar com o banco de dados,
não apenas gerenciar as listas"""

dbURI = getMongoDbURL()
mainDB = pymongo.MongoClient(dbURI)


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
        self.dbFuncionarios = mainDB.airsys.funcionarios

    def registrarFuncionario(self, funcionario):

        checkFuncionario = self.dbFuncionarios.find_one(
            {'nome': funcionario.getNome()}
        )

        if funcionario in self.__funcionarios:

            if checkFuncionario is not None:
                return "Funcionario ja registrado"

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
                return "Funcionario ja registrado"

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
                return "Funcionario ja registrado"

            else:
                self.__funcionarios.append(funcionario)

                newDBFuncionario = {
                    'codigo': funcionario.getCodigo(),
                    'nome': funcionario.getNome(),
                    'numIdentidade': funcionario.getNumIdentidade(),
                    'cpf': funcionario.getCPF(),
                    'email': funcionario.getEmail(),
                    'numeroDeVendas': funcionario.getNumDeVendas()
                }

                self.dbFuncionarios.insert_one(newDBFuncionario)
                return "Funcionario {0} registrado!".format(
                    funcionario.getNome())

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
        checkClientes = self.dbClientes.find_one(
            {'nome': cliente.getNome()}
        )

        if cliente in self.__clientes:

            if checkCliente is not None:
                return "cliente ja registrado"

            else:

                newCliente = {
                    'codigo': cliente.getCodigo(),
                    'nome': cliente.getNome(),
                    'numIdentidade': cliente.getNumIdentidade(),
                    'cpf': cliente.getCPF(),
                    'email': cliente.getEmail(),
                    'numeroDeVendas': cliente.getNumDeVendas()
                }

                self.dbClientes.insert_one(newCliente)
                return "Cliente ja registrado"

        else:

            if checkCliente is not None:
                newCliente = Cliente()

                newCliente.setNome(
                    checkFCliente['nome']
                )

                newCliente.setNumIdetidade(
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
                return "Funcionario ja registrado"

            else:
                self.__funcionarios.append(funcionario)

                newDBFuncionario = {
                    'codigo': funcionario.getCodigo(),
                    'nome': funcionario.getNome(),
                    'numIdentidade': funcionario.getNumIdentidade(),
                    'cpf': funcionario.getCPF(),
                    'email': funcionario.getEmail(),
                    'numeroDeVendas': funcionario.getNumDeVendas()
                }

                self.dbFuncionarios.insert_one(newDBFuncionario)
                return "Funcionario {0} registrado!".format(
                    funcionario.getNome())

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
