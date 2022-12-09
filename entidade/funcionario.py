import datetime as date
from entidade.endereco import Endereco


class Funcionario():
    def __init__(self, matricula: str,nome: str,
                 sexo: str, rg: str, cpf: str,
                 pis: str, data_nascimento: date,
                 endereco: Endereco, email: str,
                 telefone: str, nome_contato_emergencial: str,
                 telefone_contato_emergencial: str):
        self.__matricula = matricula
        self.__nome = nome
        self.__sexo = sexo
        self.__rg = rg
        self.__cpf = cpf
        self.__pis = pis
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
        self.__email = email
        self.__telefone = telefone
        self.__nome_contato_emergencial = nome_contato_emergencial
        self.__telefone_contato_emergencial = telefone_contato_emergencial

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self,matricula):
        if isinstance(matricula,str):
            self.__matricula = matricula

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
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self,rg):
        if isinstance(rg,str):
            self.__rg = rg

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        if isinstance(cpf,str):
            self.__cpf = cpf

    @property
    def pis(self):
        return self.__pis

    @pis.setter
    def pis(self,pis):
        if isinstance(pis,str):
            self.__pis = pis

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self,data_nascimento):
        if isinstance(data_nascimento,date):
            self.__data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,endereco):
        if isinstance(endereco,Endereco):
            self.__endereco = endereco

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        if isinstance(email,str):
            self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self,telefone):
        if isinstance(telefone,str):
            self.__telefone = telefone

    @property
    def nome_contato_emergencial(self):
        return self.__nome_contato_emergencial

    @nome_contato_emergencial.setter
    def nome_contato_emergencial(self,nome_contato_emergencial):
        if isinstance(nome_contato_emergencial,str):
            self.__nome_contato_emergencial = nome_contato_emergencial

    @property
    def telefone_contato_emergencial(self):
        return self.__telefone_contato_emergencial

    @telefone_contato_emergencial.setter
    def telefone_contato_emergencial(self,telefone_contato_emergencial):
        if isinstance(telefone_contato_emergencial,str):
            self.__telefone_contato_emergencial = telefone_contato_emergencial