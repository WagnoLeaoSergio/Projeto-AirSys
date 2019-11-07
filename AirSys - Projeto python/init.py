import controles

z = controles.Passagem()

lz = controles.ListaPassagens()

z.setCodigo("P0001")
z.setOrigem("Juiz de Fora")
z.setDestino("Niterói")

print(lz.buscarPassagem(codigo="P0001"))
print(lz.registrarPassagem(codigo="P0001", passagem=z))
print(lz.buscarPassagem(codigo="P0001"))
