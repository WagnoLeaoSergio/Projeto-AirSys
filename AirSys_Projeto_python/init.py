import controles

z = controles.Passagem()

lz = controles.ListaPassagens()

z.setCodigo("P0003")

print(lz.registrarPassagem("P0003", z))
print(lz.buscarPassagem(codigo="P0003").getDestino())

print(lz.listarPassagens())

#print(lz.alterarPassagem(codigo="P0001", campo="destino", valor="Beyond"))
