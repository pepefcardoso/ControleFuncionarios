from controle.excecoes import *
from datetime import datetime as date


class Validacoes():

    def valida_nome(self, nome:str):
        if (nome is None or
                not isinstance(nome, str) or
                (len(nome) < 1) or
                (not all(i.isalpha() or i.isspace() for i in nome))):
            raise NomeInvalidoException
        return nome

    def valida_nascimento(self, nascimento:str):
        try:
            if (nascimento is None or
                not isinstance(nascimento, str) or
                (len(nascimento) != 10)):
                raise DataNascimentoInvalidaException
            nascimento = date.strptime(nascimento, "%d/%m/%Y")
            return nascimento
        except ValueError:
            raise DataNascimentoInvalidaException

    def valida_sexo(self, sexo: str):
        if (sexo is None or
            not isinstance(sexo, str) or
            sexo not in ("Masculino", "Feminino")):
            raise SexoInvalidoException
        return sexo

    def valida_rg(self, rg: str):
        if (rg is None or
            not isinstance(rg, str) or
            (len(rg) != 7) or
            not rg.isnumeric()):
            raise RgInvalidoException
        return rg

    def valida_cpf(self, cpf: str):
        if (cpf is None or
            not isinstance(cpf, str) or
            (len(cpf) != 11) or
            not cpf.isnumeric()):
            raise CpfInvalidoException
        return cpf

    def valida_cep(self, cep: str):
        if (cep is None or
            not isinstance(cep, str) or
            len(cep) != 8 or
            not cep.isnumeric()):
            raise CepInvalidoException
        return cep

    def valida_estado(self, estado: str):
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
                   "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
                   "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        if (estado is None or
            not isinstance(estado, str) or
            estado not in estados):
            raise EstadoInvalidoException
        return estado

    def valida_municipio(self, municipio: str):
        if (municipio is None or
            not isinstance(municipio, str) or
            len(municipio) < 1):
            raise MunicipioInvalidoException
        return municipio

    def valida_bairro(self, bairro: str):
        if (bairro is None or
            not isinstance(bairro, str) or
            len(bairro) < 1):
            raise BairroInvalidoException
        return bairro

    def valida_logradouro(self, logradouro: str):
        if (logradouro is None or
            not isinstance(logradouro, str) or
            len(logradouro) < 1):
            raise LogradouroInvalidoException
        return logradouro

    def valida_numero(self, numero: str):
        if (numero is None or
            not isinstance(numero, str) or
            (len(numero) < 1) or
            not numero.isnumeric()):
            raise NumeroInvalidoException
        return numero

    def valida_complemento(self, complemento: str):
        if (complemento is None or
            not isinstance(complemento, str)):
            raise ComplementoInvalidoException
        return complemento

    def valida_email(self, email:str):
        if (email is None or
            not isinstance(email, str) or
            len(email) < 1):
            raise EmailInvalidoException
        return email

    def valida_telefone_fixo(self, telefone_fixo: str):
        if (telefone_fixo is None or
            not isinstance(telefone_fixo, str) or
            (len(telefone_fixo) not in range(10,12)) or
            not telefone_fixo.isnumeric()):
            raise TelefoneFixoInvalidoException
        return telefone_fixo

    def valida_telefone_celular(self, telefone_celular: str):
        if (telefone_celular is None or
            not isinstance(telefone_celular, str) or
            (len(telefone_celular) not in range(10,12)) or
            not telefone_celular.isnumeric()):
            raise TelefoneCelularInvalidoException
        return telefone_celular

    def valida_contato_emergencial(self, contato_emergencial: str):
        if (contato_emergencial is None or
            not isinstance(contato_emergencial, str) or
            (len(contato_emergencial) < 1) or
            (not all(i.isalpha() or i.isspace() for i in contato_emergencial))):
            raise ContatoEmergencialInvalidoException
        return contato_emergencial

    def valida_telefone_emergencial(self, telefone_emergencial: str):
        if (telefone_emergencial is None or
            not isinstance(telefone_emergencial, str) or
            (len(telefone_emergencial) not in range(10,12)) or
            not telefone_emergencial.isnumeric()):
            raise TelefoneEmergencialInvalidoException
        return telefone_emergencial

    '''def valida_info_cadastro(self, values: dict):
            if values is not None and isinstance(values, dict):
                values['-NOME-'] = self.valida_nome(values['-NOME-'].strip())
                values['-NASCIMENTO-'] = self.valida_nascimento(values['-NASCIMENTO-'].strip())
                values['-SEXO-'] = self.valida_sexo(values['-SEXO-'].strip())
                values['-RG-'] = self.valida_rg(values['-RG-'].strip())
                values['-CPF-'] = self.valida_cpf(values['-CPF-'].strip())
                values['-CEP-'] = self.valida_cep(values['-CEP-'].strip())
                values['-UF-'] = self.valida_estado(values['-UF-'].strip())
                values['-CIDADE-'] = self.valida_municipio(values['-CIDADE-'].strip())
                values['-BAIRRO-'] = self.valida_bairro(values['-BAIRRO-'].strip())
                values['-LOGRADOURO-'] = self.valida_logradouro(values['-LOGRADOURO-'].strip())
                values['-NUMERO-'] = self.valida_numero(values['-NUMERO-'].strip())
                values['-COMPLEMENTO-'] = self.valida_complemento(values['-COMPLEMENTO-'].strip())
                values['-EMAIL-'] = self.valida_email(values['-EMAIL-'].strip())
                values['-TELEFONE-FIXO-'] = self.valida_telefone_fixo(values['-TELEFONE-FIXO-'].strip())
                values['-TELEFONE-CELULAR-'] = self.valida_telefone_celular(values['-TELEFONE-CELULAR-'].strip())
                values['-CONTATO-EMERGENCIAL-'] = self.valida_contato_emergencial(values['-CONTATO-EMERGENCIAL-'].strip())
                values['-TELEFONE-EMERGENCIAL-'] = self.valida_telefone_emergencial(values['-TELEFONE-EMERGENCIAL-'].strip())
                return values'''
