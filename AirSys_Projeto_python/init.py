import controles

z = controles.Cliente()

lz = controles.ListaClientes()

z.setCodigo("C0002")
z.setNome("Pedro")

# print(lz.registrarCliente("C0002", z))
print(lz.buscarCliente(codigo="C0003"))

print(lz.listarClientes())