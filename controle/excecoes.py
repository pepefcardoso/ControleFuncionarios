class CepInvalidoException(Exception):
    def __init__(self):
        super().__init__("CEP INVÁLIDO!")

class MatriculaInvalidaException(Exception):
    def __init__(self):
        super().__init__("MATRÍCULA INVÁLIDA!")

class NomeInvalidoException(Exception):
    def __init__(self):
        super().__init__("NOME INVÁLIDO!")

class SexoInvalidoException(Exception):
    def __init__(self):
        super().__init__("SEXO INVÁLIDO!")

class RgInvalidoException(Exception):
    def __init__(self):
        super().__init__("RG INVÁLIDO!")

class CpfInvalidoException(Exception):
    def __init__(self):
        super().__init__("CPF INVÁLIDO!")

class PisInvalidoException(Exception):
    def __init__(self):
        super().__init__("PIS INVÁLIDO!")

class DataNascimentoInvalidaException(Exception):
    def __init__(self):
        super().__init__("DATA DE NASCIMENTO INVÁLIDA!")

class EstadoInvalidoException(Exception):
    def __init__(self):
        super().__init__("ESTADO INVÁLIDO!")

class MunicipioInvalidoException(Exception):
    def __init__(self):
        super().__init__("MUNICÍPIO INVÁLIDO!")

class BairroInvalidoException(Exception):
    def __init__(self):
        super().__init__("BAIRRO INVÁLIDO!")

class LogradouroInvalidoException(Exception):
    def __init__(self):
        super().__init__("LOGRADOURO INVÁLIDO!")

class NumeroInvalidoException(Exception):
    def __init__(self):
        super().__init__("NÚMERO INVÁLIDO!")

class ComplementoInvalidoException(Exception):
    def __init__(self):
        super().__init__("COMPLEMENTO INVÁLIDO!")

class EmailInvalidoException(Exception):
    def __init__(self):
        super().__init__("EMAIL INVÁLIDO!")

class TelefoneFixoInvalidoException(Exception):
    def __init__(self):
        super().__init__("TELEFONE FIXO INVÁLIDO!")

class TelefoneCelularInvalidoException(Exception):
    def __init__(self):
        super().__init__("TELEFONE CELULAR INVÁLIDO!")

class ContatoEmergencialInvalidoException(Exception):
    def __init__(self):
        super().__init__("CONTATO EMERGENCIAL INVÁLIDO!")

class TelefoneEmergencialInvalidoException(Exception):
    def __init__(self):
        super().__init__("TELEFONE EMERGENCIAL INVÁLIDO!")
