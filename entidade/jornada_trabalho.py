class JornadaTrabalho():
    def __init__(self, jornada_segunda: list,
                 jornada_terca: list,
                 jornada_quarta: list,
                 jornada_quinta: list,
                 jornada_sexta: list,
                 jornada_sabado: list):
        self.__jornada_segunda = jornada_segunda
        self.__jornada_terca = jornada_terca
        self.__jornada_quarta = jornada_quarta
        self.__jornada_quinta = jornada_quinta
        self.__jornada_sexta = jornada_sexta
        self.__jornada_sabado = jornada_sabado

    @property
    def jornada_segunda(self):
        return self.__jornada_segunda

    @property
    def jornada_terca(self):
        return self.__jornada_terca

    @property
    def jornada_quarta(self):
        return self.__jornada_quarta

    @property
    def jornada_quinta(self):
        return self.__jornada_quinta

    @property
    def jornada_sexta(self):
        return self.__jornada_sexta

    @property
    def jornada_sabado(self):
        return self.__jornada_sabado
