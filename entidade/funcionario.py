from datetime import datetime
from entidade.endereco import Endereco
from entidade.documentos import Documentos
from entidade.contatos import Contatos



class Funcionario():
    def __init__(self,
                 nome: str,
                 sexo: str,
                 data_nascimento: datetime,
                 documentos: Documentos,
                 endereco: Endereco,
                 contatos: Contatos):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__documentos = documentos
        self.__endereco = endereco
        self.__contatos = contatos
        self.__contratos = []

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
    def documentos(self):
        return self.__documentos

    @documentos.setter
    def documentos(self, documentos: Documentos):
        if isinstance(documentos, Documentos):
            self.__documentos = documentos

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,endereco):
        if isinstance(endereco,Endereco):
            self.__endereco = endereco

    @property
    def contatos(self):
        return self.__contatos

    @contatos.setter
    def contatos(self, contatos: Contatos):
        if isinstance(contatos, Contatos):
            self.__contatos = contatos

    @property
    def contratos(self):
        return self.__contratos
