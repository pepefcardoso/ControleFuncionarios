from datetime import datetime
from modelo.endereco import Endereco
from modelo.documentos import Documentos
from modelo.contatos import Contatos
from modelo.cadastro_basico import CadastroBasico
from modelo.setor import Setor
from modelo.centro_custo import CentroCusto
'''from modelo.contrato import Contrato'''


class Funcionario():
    def __init__(self,
                 cadastro_basico: CadastroBasico,
                 documentos: Documentos,
                 endereco: Endereco,
                 contatos: Contatos):
        self.__status = False
        self.codigo = None
        self.__cadastro_basico = cadastro_basico
        self.__documentos = documentos
        self.__endereco = endereco
        self.__contatos = contatos
        self.__contrato = None
        self.__setor = None
        self.__centro_custo = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: bool):
        if isinstance(status, bool):
            self.__status = status

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

    '''@property
    def contrato(self):
        return self.__contrato

    @property
    def contrato(self, contrato: Contrato):
        if isinstance(contrato, Contrato):
            self.__contrato = contrato'''

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor: Setor):
        if isinstance(setor, Setor):
            self.__setor = setor

    @property
    def centro_custo(self):
        return self.__centro_custo

    @centro_custo.setter
    def centro_custo(self, centro_custo: CentroCusto):
        if isinstance(centro_custo, CentroCusto):
            self.__centro_custo = centro_custo
