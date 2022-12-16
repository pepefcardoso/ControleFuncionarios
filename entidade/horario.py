from datetime import datetime


class Horario():
    def __init__(self, entrada: datetime, saida:datetime):
        self.__entrada = entrada
        self.__saida = saida

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, entrada: datetime):
        if isinstance(entrada, datetime):
            self.__entrada = entrada

    @property
    def saida(self):
        return self.__saida

    @saida.setter
    def saida(self, saida: datetime):
        if isinstance(saida, datetime):
            self.__entrada = saida
