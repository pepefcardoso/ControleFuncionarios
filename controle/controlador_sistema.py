from limite.tela_sistema import TelaSistema
import PySimpleGUI as sg
from controle.excecoes import *


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def abre_tela_inicial(self):
        self.__tela_sistema.tela_inicial()
        while True:
            event, values = self.__tela_sistema.abre()
            if event == sg.WIN_CLOSED:
                break
            print(values["-NASCIMENTO-"])
            print(type(values["-NASCIMENTO-"]))
