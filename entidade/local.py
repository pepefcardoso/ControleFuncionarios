from entidade.pessoa import Pessoa


class Local(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
