import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None

    def tela_inicial(self):
        font = ("SF Pro Display", 16)
        button_color = "#F28500"
        background_color = "#FFF5EE"
        layout = [[sg.Button('Opção_1', s=(11,1), button_color=button_color),
                   sg.Button('Opção_2', s=(11,1), button_color=button_color),
                   sg.Button('Opção_3', s=(11,1), button_color=button_color),
                   sg.Button('Opção_4', s=(11,1), button_color=button_color),
                   sg.Button('Opção_5', s=(11,1), button_color=button_color),
                   sg.Button('Opção_6', s=(11,1), button_color=button_color),
                   sg.Button('Opção_7', s=(11,1), button_color=button_color),
                   sg.Button('Opção_8', s=(11,1), button_color=button_color)]]
        self.__window = sg.Window('MENU INICIAL',
                                  layout,
                                  font=font,
                                  background_color=background_color,
                                  element_justification='center',
                                  enable_close_attempted_event=True,
                                  margins=(20,20),
                                  text_justification='center')

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
