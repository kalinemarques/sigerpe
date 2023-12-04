from model.mesaModel import Mesa

class CadastrarMesa:
    @staticmethod
    def post(codigoGarcom, capacidade):
        mesa = Mesa(codigoGarcom, capacidade)
        mesa.inserir()

class AlterarMesa:
    @staticmethod
    def get(id):
        mesa = Mesa(id)
        mesa.alterar()

class ExcluirMesa:
    @staticmethod
    def get(id):
        mesa = Mesa.buscar_por_id(id)
        mesa.excluir()

class ListarMesa:
    @staticmethod
    def get():
        print(Mesa.listar())

class BuscarMesa:
    @staticmethod
    def get(id):
        mesa = Mesa.buscar_por_id(id)
        print(mesa)