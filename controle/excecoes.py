class CepInvalidoException(Exception):
    def __init__(self):
        super().__init__("CEP INVÁLIDO!")
