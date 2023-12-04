from controller.mesaController import CadastrarMesa, ExcluirMesa, ListarMesa, BuscarMesa, AlterarMesa

print("======INSERIR======")
CadastrarMesa.post(10, 7)
CadastrarMesa.post(15, 7566)

BuscarMesa.get(2)
ListarMesa.get()

print("======EXCLUIR======")
ExcluirMesa.get(1)

BuscarMesa.get(2)
ListarMesa.get()