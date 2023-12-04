from model.mesaModel import Mesa

mesa1 = Mesa(10, 7)
mesa2 = Mesa(15, 7566)
print("======INSERIR======")
mesa1.inserir()
mesa2.inserir()

print(Mesa.buscar_por_id(2))
print(Mesa.listar())

print("======EXCLUIR======")
mesa1.setId(Mesa.buscar_por_id(1).getId())
mesa1.excluir()

print(Mesa.buscar_por_id(2))
print(Mesa.listar())