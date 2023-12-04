from bd import _executar

class Mesa():
    def __init__(self, capacidade, codigoGarcom, id=None):
        self.__capacidade = capacidade
        self.__codigoGarcom = codigoGarcom
        self.__id = id

        query="CREATE TABLE IF NOT EXISTS mesa(id INTEGER PRIMARY KEY AUTOINCREMENT, capacidade NUMERIC, status NUMERIC, codigoGarcom NUMERIC)" #se a tabela produtos ainda não existir, crio uma
        _executar(query)

    def getId(self):
        return self.__id
    def setId(self, valor):
        self.__id = valor

    def getCodigoGarcom(self):
        return self.__codigoGarcom
    def setCodigoGarcom(self, valor):
        self.__codigoGarcom = valor

    def getCapacidade(self):
        return self.__capacidade
    def setCapacidade(self, valor):
        self.__capacidade = valor

    def inserir(self):
        query = f"INSERT INTO mesa (codigoGarcom, capacidade) VALUES ('{int(self.getCodigoGarcom())}', '{int(self.getCapacidade())}')"
        _executar(query)

    def alterar(self):
        query = f"UPDATE mesa SET capacidade='{int(self.getCapacidade())}', codigoGarcom='{int(self.getCodigoGarcom())}' WHERE id={self.getId()}"
        _executar(query)

    def excluir(self):
        query = f"DELETE FROM mesa WHERE id={self.getId()}"
        _executar(query)

    @staticmethod
    def listar():
        query = "SELECT * FROM mesa"
        mesa = _executar(query)
        return mesa

    @staticmethod
    def buscar_por_id(id):
        query = f"SELECT * FROM mesa WHERE id={int(id)}"
        mesa = _executar(query)[0]
        mesa = Mesa(id=mesa[0], capacidade=mesa[1], codigoGarcom=mesa[2])
        return mesa


    # Função para verificar o status do livro
    def verificar_status(self):
        if self.getStatus() == 1:  # Verifica se o status é disponível para empréstimo
            return True
        else:
            return False

    #to string
    def __str__(self):
        return f"'{self.__id}', '{self.__capacidade}', '{self.__codigoGarcom}'"