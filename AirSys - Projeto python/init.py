import controles

x = controles.Gerente()
lx = controles.ListaGerentes()

x.setNome("joao")

print(x.getNome())
print(x.getTurno())

# y = lx.buscarFuncionario(x)

# print(lx.registrarGerente(x))

print(lx.removerGerente(x))


# lx.removerFuncionario(x)

"""

y = controles.Cliente()
ly = controles.ListaClientes()

y.setNome("lisa")

print(y.getNome())
print(y.getBanco())

z = ly.registrarCliente(y)

print(z)

z = ly.registrarCliente(y)

print(z)

"""