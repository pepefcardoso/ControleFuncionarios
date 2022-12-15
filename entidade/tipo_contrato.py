from entidade.pessoa import Pessoa


class TipoContrato(Pessoa):
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
