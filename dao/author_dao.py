class AuthorDatabase:

    def __init__(self):
        self.__list = []

    def add(self, author):
        if author in self.__list:
            raise Exception('Já existe um e-mail como este')
        self.__list.append(author)

    @property
    def list(self):
        return self.__list.copy()
