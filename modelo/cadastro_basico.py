from datetime import datetime


class CadastroBasico():
    def __init__(self,
                 nome: str,
                 sexo: str,
                 data_nascimento: datetime,
                 nome_pai: str,
                 nome_mae: str,
                 estado_civil: str):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__nome_pai = nome_pai
        self.__nome_mae = nome_mae
        self.__estado_civil = estado_civil

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        if isinstance(nome,str):
            self.__nome = nome

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self,sexo):
        if isinstance(sexo,str):
            self.__sexo = sexo

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self,data_nascimento):
        if isinstance(data_nascimento,datetime):
            self.__data_nascimento = data_nascimento

    @property
    def nome_pai(self):
        return self.__nome_pai

    @nome_pai.setter
    def nome_pai(self, nome_pai: str):
        if isinstance(nome_pai, str):
            self.__nome_pai = nome_pai

    @property
    def nome_mae(self):
        return self.__nome_mae

    @nome_mae.setter
    def nome_mae(self, nome_mae: str):
        if isinstance(nome_mae, str):
            self.__nome_mae = nome_mae

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil: str):
        if isinstance(estado_civil, str):
            self.__estado_civil = estado_civil
