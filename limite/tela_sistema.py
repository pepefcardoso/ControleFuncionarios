import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None

    def tela_inicial(self):
        sg.theme('LightGreen')
        layout = [[]]
        self.__window = sg.Window('Controle Funcionários',
                           layout,
                           default_element_size=(12, 1),
                           default_button_element_size=(12, 1))

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
