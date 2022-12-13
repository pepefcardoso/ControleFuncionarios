import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None

    def tela_inicial(self):
        
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        
        layout = [[sg.Text('CEP', s=(20,1)), sg.Input('',key="-CEP-", s=(20,1)), sg.Button('Buscar CEP', key="-BUSCA-CEP-")],
                           [sg.Text('Estado', s=(20,1)), sg.Combo(estados,key="-UF-", s=(20,1))],
                           [sg.Text('Município', s=(20,1)), sg.Input('',key="-CIDADE-", s=(20,1))],
                           [sg.Text('Bairro', s=(20,1)), sg.Input('',key="-BAIRRO-", s=(20,1))],
                           [sg.Text('Logradouro', s=(20,1)), sg.Input('',key="-LOGRADOURO-", s=(20,1))],
                           [sg.Text('Número', s=(20,1)), sg.Input('',key="-NUMERO-", s=(20,1))],
                           [sg.Text('Complemento', s=(20,1)), sg.Input('',key="-COMPLEMENTO-", s=(20,1))],]
        
        self.__window = sg.Window('Controle Funcionários', layout)

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def atualiza_dados_endereco(self, estado, cidade, bairro, logradouro):
        self.__window["-UF-"].Update(estado)
        self.__window["-CIDADE-"].Update(cidade)
        self.__window["-BAIRRO-"].Update(bairro)
        self.__window["-LOGRADOURO-"].Update(logradouro)
        self.__window.Refresh()
