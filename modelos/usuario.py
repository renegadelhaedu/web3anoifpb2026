class Usuario:
    def __init__(self, nome, login, senha):
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def get_login(self):
        return self.__login

    def get_senha(self):
        return self.__senha

    def __repr__(self):
        return f'Usuario(Nome:{self.__nome},Login:{self.__login})'
