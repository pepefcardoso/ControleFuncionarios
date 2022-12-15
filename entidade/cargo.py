from entidade.pessoa import Pessoa


class Cargo(Pessoa):
    def __init__(self, nome: str, codigo: int, cbo: str):
        super().__init__(nome, codigo)
        self.__cbo = cbo

    @property
    def cbo(self):
        return self.__cbo

    @cbo.setter
    def cbo(self, cbo: str):
        if isinstance(cbo, str):
            self.__cbo = cbo
