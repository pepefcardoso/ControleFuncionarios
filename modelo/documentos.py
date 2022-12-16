from modelo.ctps import Ctps
from modelo.rg import Rg


class Documentos():
    def __init__(self, cpf: str,
                 rg: Rg, ctps: Ctps):
        self.__cpf = cpf
        self.__rg = rg
        self.__ctps = ctps

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        if isinstance(rg, Rg):
            self.__rg = rg

    @property
    def ctps(self):
        return self.__ctps

    @ctps.setter
    def ctps(self, ctps):
        if isinstance(ctps, Ctps):
            self.__ctps = ctps
