from model.mesaModel import Mesa

class CadastrarMesa:
    @staticmethod
    def post(codigoGarcom, capacidade):
        mesa = Mesa(codigoGarcom, capacidade)
        mesa.inserir()

class AlterarMesa:
    @staticmethod
    def get(id, codigoGarcom):
        mesa = Mesa.buscar_por_id(id)
        mesa.setCodigoGarcom(codigoGarcom)
        mesa.alterar()

class ExcluirMesa:
    @staticmethod
    def get(id):
        mesa = Mesa.buscar_por_id(id)
        mesa.excluir()

class ListarMesa:
    @staticmethod
    def get():
        mesa = Mesa.listar()
        for mesa_info in mesa:
            print(f'ID_MESA: {mesa_info[0]}, CAPACIDADE: {mesa_info[1]}, GARÇOM_RESPONSÁVEL: {mesa_info[2]}')

class BuscarMesa:
    @staticmethod
    def get(id):
        mesa = Mesa.buscar_por_id(id)
        print(mesa)
