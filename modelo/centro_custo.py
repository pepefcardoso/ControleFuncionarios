from modelo.pessoa import Pessoa


class CentroCusto(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
