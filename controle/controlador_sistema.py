from limite.tela_sistema import TelaSistema
import PySimpleGUI as sg
import requests
from controle.excecoes import *
import sys


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def abre_tela_inicial(self):
        self.__tela_sistema.tela_inicial()
        while True:
            event, values = self.__tela_sistema.abre()
            if event == sg.WIN_CLOSED:
                break
            if event == "-BUSCA-CEP-":
                dados = self.consulta_cep(values["-CEP-"])
                estado = dados['uf']
                cidade = dados['localidade']
                bairro = dados['bairro']
                logradouro = dados['logradouro']
                self.__tela_sistema.atualiza_dados_endereco(estado, cidade, bairro, logradouro)

    def consulta_cep(self, cep: str):
        if (cep is not None and
            isinstance(cep, str) and
            len(cep) == 8 and
            cep.isnumeric()):
            link = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()
            if len(dic_requisicao) != 10:
                raise CepInvalidoException
            return dic_requisicao
        raise CepInvalidoException
