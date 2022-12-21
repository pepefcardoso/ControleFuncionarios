from limite.tela_sistema import TelaSistema
import PySimpleGUI as sg
from controle.excecoes import *
from controle.controlador_funcionarios import ControladorFuncionarios
from validacoes.validacoes import Validacoes


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__validacoes = Validacoes()
        self.__controlador_funcionarios = ControladorFuncionarios(self)

    @property
    def validacoes(self):
        return self.__validacoes

    @property
    def controlador_funcionarios(self):
        return self.__controlador_funcionarios

    def abre_tela_inicial(self):
        self.__tela_sistema.tela_inicial()
        while True:
            event, values = self.__tela_sistema.abre()
            if event == sg.WIN_CLOSED:
                break
            if event == "FUNCIONÁRIOS":
                self.__controlador_funcionarios.abre_tela_inicial()
