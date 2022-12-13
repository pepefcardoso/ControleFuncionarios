from limite.tela_funcionarios import TelaFuncionarios
import PySimpleGUI as sg
import requests
from datetime import datetime
from controle.excecoes import *



class TelaFuncionarios():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_funcionarios = TelaFuncionarios()



    def consulta_cep(self, cep: str):
        self.valida_cep(cep.strip())
        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        if len(dic_requisicao) != 10:
            raise CepInvalidoException
        return dic_requisicao

    def atualiza_dados_endereco(self, cep:str):
        if (cep is not None and isinstance(cep, str)):
            try:
                dados = self.consulta_cep(cep)
                estado = dados['uf']
                cidade = dados['localidade']
                bairro = dados['bairro']
                logradouro = dados['logradouro']
                self.__tela_sistema.atualiza_dados_endereco(estado, cidade, bairro, logradouro)
            except CepInvalidoException as e:
                self.__tela_sistema.mostra_mensagem('ERRO', e)

    def valida_info_cadastro(self, values: dict):
        if values is not None and isinstance(values, dict):
            self.valida_nome(values['-NOME-'].strip())
            self.valida_nascimento(values['-NASCIMENTO-'].strip())
            self.valida_sexo(values['-SEXO-'].strip())
            self.valida_rg(values['-RG-'].strip())
            self.valida_cpf(values['-CPF-'].strip())
            self.valida_cep(values['-CEP-'].strip())


    def valida_nome(self, nome:str):
        if (nome is None or
                not isinstance(nome, str) or
                (len(nome) < 1) or
                (not all(i.isalpha() or i.isspace() for i in nome))):
                raise NomeInvalidoException

    def valida_nascimento(self, nascimento:str):
        try:
            if (nascimento is None or
                not isinstance(nascimento, str) or
                (len(nascimento) != 10)):
                raise DataNascimentoInvalidaException
            datetime.strptime(nascimento, "%d/%m/%Y")
        except ValueError:
            raise DataNascimentoInvalidaException

    def valida_sexo(self, sexo: str):
        if (sexo is None or
            not isinstance(sexo, str) or
            sexo not in ("Masculino", "Feminino")):
            raise SexoInvalidoException

    def valida_rg(self, rg: str):
        if (rg is None or
            not isinstance(rg, str) or
            (len(rg) != 7) or
            not rg.isnumeric()):
            raise RgInvalidoException

    def valida_cpf(self, cpf: str):
        if (cpf is None or
            not isinstance(cpf, str) or
            (len(cpf) != 11) or
            not cpf.isnumeric()):
            raise CpfInvalidoException

    def valida_cep(self, cep: str):
        if (cep is None or
            not isinstance(cep, str) or
            len(cep) != 8 or
            not cep.isnumeric()):
            raise CepInvalidoException

    def adiciona_funcionario(self, values: dict):
        pass