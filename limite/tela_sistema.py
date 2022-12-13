import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None

    def tela_inicial(self):
        sexos = ["Masculino", "Feminino"]
        layout_info_basico = [[sg.Text('Nome', s=(20,1)),
                               sg.Input('',key="-NOME-", s=(20,1))],
                              [sg.Text('Data de Nascimento', s=(20,1)),
                               sg.Input('',key="-NASCIMENTO-", s=(20,1)),
                               sg.CalendarButton("Calendário", target="-NASCIMENTO-", locale="pt-BR", format="%d/%m/%Y")],
                              [sg.Text('Sexo', s=(20,1)),
                               sg.Combo(sexos,key="-SEXO-", s=(20,1))],
                              [sg.Text('Registro Geral', s=(20,1)),
                               sg.Input('',key="-RG-", s=(20,1))],
                              [sg.Text('Cadastro de Pessoa Física', s=(20,1)),
                               sg.Input('',key="-CPF-", s=(20,1))],
                              [sg.Text('PIS', s=(20,1)),
                               sg.Input('',key="-PIS-", s=(20,1))]]
        
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        layout_endereco = [[sg.Text('CEP', s=(20,1)), sg.Input('',key="-CEP-", s=(20,1)), sg.Button('Buscar CEP', key="-BUSCA-CEP-")],
                           [sg.Text('Estado', s=(20,1)), sg.Combo(estados,key="-UF-", s=(20,1))],
                           [sg.Text('Município', s=(20,1)), sg.Input('',key="-CIDADE-", s=(20,1))],
                           [sg.Text('Bairro', s=(20,1)), sg.Input('',key="-BAIRRO-", s=(20,1))],
                           [sg.Text('Logradouro', s=(20,1)), sg.Input('',key="-LOGRADOURO-", s=(20,1))],
                           [sg.Text('Número', s=(20,1)), sg.Input('',key="-NUMERO-", s=(20,1))],
                           [sg.Text('Complemento', s=(20,1)), sg.Input('',key="-COMPLEMENTO-", s=(20,1))],]
        
        layout_contato = [[sg.Text('E-mail', s=(20,1)), sg.Input('',key="-EMAIL-", s=(20,1))],
                          [sg.Text('Telefone Fixo', s=(20,1)), sg.Input('',key="-TELEFONE-FIXO-", s=(20,1))],
                          [sg.Text('Telefone Celular', s=(20,1)), sg.Input('',key="-TELEFONE-CELULAR-", s=(20,1))],
                          [sg.Text('Contato Emergencial', s=(20,1)), sg.Input('',key="-CONTATO-EMERGENCIAL-", s=(20,1))],
                          [sg.Text('Telefone Emergencial', s=(20,1)), sg.Input('',key="-TELEFONE-EMERGENCIAL-", s=(20,1))]]

        layout_abas = [[sg.TabGroup([[sg.Tab("Informação Básica", layout_info_basico, element_justification="center"),
                                      sg.Tab("Endereço", layout_endereco, element_justification="center"),
                                      sg.Tab("Contatos", layout_contato, element_justification="center")]],
                                    tab_location="lefttop")]]
        self.__window = sg.Window('Controle Funcionários', layout_abas)

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
