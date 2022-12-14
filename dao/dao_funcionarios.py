from dao.abstract_dao import Dao
from entidade.funcionario import Funcionario


class DaoFuncionarios(Dao):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (funcionario is not None and
            isinstance(funcionario, Funcionario) and
            isinstance(funcionario.cpf, str)):
            super().add(funcionario.cpf, funcionario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def get_all(self):
        return super().get_all()

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
