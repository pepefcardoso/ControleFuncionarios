import datetime as date
from entidade.endereco import Endereco


class Funcionario():
    def __init__(self, matricula: str,nome: str,
                 sexo: str, rg: str, cpf: str,
                 pis: str, nascimento: date,
                 endereco: Endereco, email: str,
                 telefone: str, contato_emergencial: str,
                 telefone_emergencial: str):
        self.__matricula = matricula
        self.__local = local
        self.__