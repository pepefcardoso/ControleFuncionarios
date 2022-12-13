import requests
from controle.excecoes import CepInvalidoException


def consulta_cep(cep: str):
    if (cep is not None and
        isinstance(cep, str) and
        len(cep) == 8 and
        cep.isnumeric()):
        link = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        if len(dic_requisicao) != 10:
            raise CepInvalidoException
        return dic_requisicao
    raise CepInvalidoException
