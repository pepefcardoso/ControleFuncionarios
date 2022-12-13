class Endereco():
    def __init__(self, cep: str, estado: str,
                 municipio: str, bairro: str,logradouro: str,
                 numero: str, complemento: str):
        self.__cep = cep
        self.__estado = estado
        self.__municipio = municipio
        self.__bairro = bairro
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self,cep):
        if isinstance(cep, str):
            self.__cep = cep

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self,estado):
        if isinstance(estado, str):
            self.__estado = estado

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self,municipio):
        if isinstance(municipio, str):
            self.__municipio = municipio

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self,bairro):
        if isinstance(bairro, str):
            self.__bairro = bairro

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self,logradouro):
        if isinstance(logradouro, str):
            self.__logradouro = logradouro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self,numero):
        if isinstance(numero, str):
            self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self,complemento):
        if isinstance(complemento, str):
            self.__complemento = complemento
