import controles

z = controles.Passagem()

lz = controles.ListaPassagens()

#z.setCodigo("G0001")

#print(lz.registrarGerente("G0001", z))
print(lz.buscarPassagem(codigo="P0001").getDestino())

print(lz.listarPassagens())

print(lz.alterarPassagem(codigo="P0001", campo="destino", valor="Beyond"))