class Contatos():
    def __init__(self, email: str,
                 telefone_fixo: str,
                 telefone_celular: str,
                 contato_emergencial: str,
                 telefone_emergencial: str):
        self.__email = email
        self.__telefone_fixo = telefone_fixo
        self.__telefone_celular = telefone_celular
        self.__contato_emergencial = contato_emergencial
        self.__telefone_emergencial = telefone_emergencial

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        if isinstance(email,str):
            self.__email = email

    @property
    def telefone_fixo(self):
        return self.__telefone_fixo

    @telefone_fixo.setter
    def telefone_fixo(self,telefone_fixo):
        if isinstance(telefone_fixo,str):
            self.__telefone_fixo = telefone_fixo

    @property
    def telefone_celular(self):
        return self.__telefone_celular

    @telefone_celular.setter
    def telefone_celular(self,telefone_celular):
        if isinstance(telefone_celular,str):
            self.__telefone_celular = telefone_celular

    @property
    def contato_emergencial(self):
        return self.__contato_emergencial

    @contato_emergencial.setter
    def contato_emergencial(self,contato_emergencial):
        if isinstance(contato_emergencial,str):
            self.__contato_emergencial = contato_emergencial

    @property
    def telefone_emergencial(self):
        return self.__telefone_emergencial

    @telefone_emergencial.setter
    def telefone_emergencial(self,telefone_emergencial):
        if isinstance(telefone_emergencial,str):
            self.__telefone_emergencial = telefone_emergencial
