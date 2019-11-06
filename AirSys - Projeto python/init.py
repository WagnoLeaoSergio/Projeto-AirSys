import controles

x = controles.Funcionario()
lx = controles.ListaFuncionarios()

x.setNome("joao")

print(x.getNome())
print(x.getEmail())

y = lx.buscarFuncionario(x)
print (y)

print(lx.registrarFuncionario(x))

#y = lx.buscarFuncionario(x)
print (y)

print(lx.removerFuncionario(x))


#lx.removerFuncionario(x)ss