import controles

x = controles.Funcionario()
lx = controles.ListaFuncionarios()

x.setNome("joao")

print(x.getNome())
print(x.getEmail())

#lx.buscarFuncionario(x)

lx.registrarFuncionario(x)

lx.registrarFuncionario(x)

#lx.buscarFuncionario(x)

#lx.removerFuncionario(x)ss