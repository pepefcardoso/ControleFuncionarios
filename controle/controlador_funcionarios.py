from limite.tela_funcionarios import TelaFuncionarios
import PySimpleGUI as sg
import requests
from datetime import datetime
from controle.excecoes import *
from modelo.funcionario import Funcionario
from modelo.endereco import Endereco


class ControladorFuncionarios():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_funcionarios = TelaFuncionarios()
        

    def abre_tela_inicial(self):
        self.__tela_funcionarios.tela_inicial()
        while True:
            self.lista_tabela_funcionarios()
            event, values = self.__tela_funcionarios.abre()
            if event in (sg.WIN_CLOSED, "VOLTAR"):
                self.__tela_funcionarios.fecha()
                return
            if event == "NOVO FUNCIONÁRIO":
                self.__tela_funcionarios.fecha()
                return self.adiciona_funcionario()

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
                self.__tela_funcionarios.atualiza_dados_endereco(estado, cidade, bairro, logradouro)
            except CepInvalidoException as e:
                self.__tela_funcionarios.mostra_mensagem('ERRO', e)


    def adiciona_funcionario(self):
        self.__tela_funcionarios.tela_cadastro()
        while True:
            event, values = self.__tela_funcionarios.abre()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                self.__tela_funcionarios.fecha()
                return self.abre_tela_inicial()
            if event == "-BUSCA-CEP-":
                self.atualiza_dados_endereco(values["-CEP-"])
            if event == "Adicionar Colaborador":
                try:
                    self.valida_info_cadastro(values)
                    endereco = Endereco(values["-CEP-"], values["-UF-"], values["-CIDADE-"],
                                        values["-BAIRRO-"], values["-LOGRADOURO-"],
                                        values["-NUMERO-"], values["-COMPLEMENTO-"])
                    funcionario = Funcionario(values["-NOME-"], values["-SEXO-"], values["-RG-"],
                                              values["-CPF-"], values["-NASCIMENTO-"], endereco,
                                              values["-EMAIL-"], values["-TELEFONE-FIXO-"],
                                              values["-TELEFONE-CELULAR-"], values["-CONTATO-EMERGENCIAL-"],
                                              values["-TELEFONE-EMERGENCIAL-"])
                    self.__dao_funcionarios.add(funcionario)
                    self.__tela_funcionarios.fecha()
                    return self.abre_tela_inicial()
                except Exception as e:
                    self.__tela_funcionarios.mostra_mensagem("ERRO", e)

    def lista_tabela_funcionarios(self):
        for i in self.__dao_funcionarios.cache:
            print(i.cpf)




