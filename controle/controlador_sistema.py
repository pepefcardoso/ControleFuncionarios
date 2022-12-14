from limite.tela_sistema import TelaSistema
import PySimpleGUI as sg
from controle.excecoes import *
from controle.controlador_funcionarios import ControladorFuncionarios


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_funcionarios = ControladorFuncionarios(self)

    @property
    def controlador_funcionarios(self):
        return self.__controlador_funcionarios

    def abre_tela_inicial(self):
        self.__tela_sistema.tela_inicial()
        while True:
            event, values = self.__tela_sistema.abre()
            if event == sg.WIN_CLOSED:
                break
            if event == "-FUNCIONARIOS-":
                self.__tela_sistema.window.disappear()
                self.__controlador_funcionarios.adiciona_funcionario()
                self.__tela_sistema.window.reappear()