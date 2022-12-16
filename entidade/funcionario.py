from datetime import datetime
from entidade.endereco import Endereco
from entidade.documentos import Documentos
from entidade.contatos import Contatos
from entidade.cadastro_basico import CadastroBasico


class Funcionario():
    def __init__(self,
                 cadastro_basico: CadastroBasico,
                 documentos: Documentos,
                 endereco: Endereco,
                 contatos: Contatos):
        self.codigo = None
        self.__cadastro_basico = cadastro_basico
        self.__documentos = documentos
        self.__endereco = endereco
        self.__contatos = contatos
        self.__contratos = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def cadastro_basico(self):
        return self.__cadastro_basico

    @cadastro_basico.setter
    def cadastro_basico(self, cadastro_basico: int):
        if isinstance(cadastro_basico, int):
            self.__cadastro_basico = cadastro_basico

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
