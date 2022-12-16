class DadosBancarios():
    def __init__(self, banco: str = '', agencia: str = '',
                 conta_corrente: str = '', digito: str = ''):
        self.__banco = banco
        self.__agencia = agencia
        self.__conta_corrente = conta_corrente
        self.__digito = digito

    @property
    def banco(self):
        return self.__banco

    @banco.setter
    def banco(self, banco: str):
        if isinstance(banco, str):
            self.__banco = banco

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia: str):
        if isinstance(agencia, str):
            self.__agencia = agencia

    @property
    def conta_corrente(self):
        return self.__conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, conta_corrente: str):
        if isinstance(conta_corrente, str):
            self.__conta_corrente = conta_corrente

    @property
    def digito(self):
        return self.__digito

    @digito.setter
    def digito(self, digito: str):
        if isinstance(digito, str):
            self.__digito = digito
