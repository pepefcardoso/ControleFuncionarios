import PySimpleGUI as sg


class TelaFuncionarios():
    def __init__(self):
        self.__window = None

    def tela_inicial(self):
        headings = ["NOME", "SEXO", "RG", "CPF",
                    "DATA DE NASCIMENTO", "CEP",
                    "EMAIL", "CELULAR"]
        layout = [[sg.Table(values=[],
                            headings=headings,
                            key="-LISTA-",
                            enable_events=True)],
                  [sg.Button("VOLTAR"), sg.Button("NOVO FUNCIONÁRIO")]]
        self.__window = sg.Window("FUNCIONÁRIOS", layout, font="Lato")

    def tela_cadastro(self):
        sexos = ["Masculino", "Feminino"]
        layout_info_basico = [[sg.Text('Nome', s=(20,1)),
                               sg.Input(key="-NOME-", s=(35,1))],
                              [sg.Text('Data de Nascimento', s=(20,1)),
                               sg.Input(key="-NASCIMENTO-", s=(35,1)),
                               sg.CalendarButton("Calendário", target="-NASCIMENTO-", format="%d/%m/%Y")],
                              [sg.Text('Sexo', s=(20,1)),
                               sg.Combo(sexos,key="-SEXO-", s=(35,1))],
                              [sg.Text('Registro Geral', s=(20,1)),
                               sg.Input(key="-RG-", s=(35,1))],
                              [sg.Text('Cadastro de Pessoa Física', s=(20,1)),
                               sg.Input(key="-CPF-", s=(35,1))],
                              [sg.Button("Adicionar Colaborador"), sg.Button("Cancelar")]]
        
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

        layout_abas = [[sg.TabGroup([[sg.Tab("Informação Básica", layout_info_basico, element_justification="left"),
                                      sg.Tab("Endereço", layout_endereco, element_justification="left"),
                                      sg.Tab("Contatos", layout_contato, element_justification="left")]],
                                    tab_location="topleft",
                                    expand_x=True,
                                    expand_y=True)]]
        self.__window = sg.Window('Controle Funcionários', layout_abas, font="Lato")

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
