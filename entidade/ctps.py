from entidade.estado import Estado
from datetime import datetime


class Ctps():
    def __init__(self, numero: str, serie: str,
                 estado: Estado, data_emissao: datetime):
        self.__numero = numero
        self.__serie = serie
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
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, serie: str):
        if isinstance(serie, str):
            self.__serie = serie

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
