import controles

z = controles.Passagem()

lz = controles.ListaPassagens()

z.setCodigo("P0001")
z.setOrigem("Juiz de Fora")
z.setDestino("Niterói")

print(lz.buscarPassagem(z))
print(lz.registrarPassagem(z))
