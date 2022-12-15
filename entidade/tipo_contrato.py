from enum import Enum


class TipoContrato(Enum):
    TEMPO_DETERMINADO = 1
    TEMPO_INDETERMINADO = 2
    TEMPORÁRIO = 3
    EVENTUAL = 4
    HOME_OFFICE = 5
    INTERMITENTE = 6
    PARCIAL = 7
    TERCEIRIZADO = 8
    AUTÔNOMO = 9
    ESTAGIÁRIO = 10
    TRAINEE = 11
    JOVEM_APRENDIZ = 12
