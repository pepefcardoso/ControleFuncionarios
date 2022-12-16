from datetime import datetime
from modelo.estado import Estado


class Rg():
    def __init__(self, numero: str, orgao: str,
                 estado: Estado, data_emissao: datetime):
        self.__numero = numero
        self.__orgao = orgao
        self.__estado = estado
        self.__data_emissao = data_emissao

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: str):
        if isinstance(numero, str):
            self.__numero = numero

    @property
    def orgao(self):
        return self.__orgao

    @orgao.setter
    def orgao(self, orgao: str):
        if isinstance(orgao, str):
            self.__orgao = orgao

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado: Estado):
        if isinstance(estado, Estado):
            self.__estado = estado

    @property
    def data_emissao(self):
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao: datetime):
        if isinstance(data_emissao, datetime):
            self.__data_emissao = data_emissao
