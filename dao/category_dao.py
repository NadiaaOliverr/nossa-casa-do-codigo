class CategoryDatabase:

    def __init__(self):
        self.__list = []

    def add(self, category):
        if category in self.__list:
            raise Exception('Já existe uma categoria com este nome')
        self.__list.append(category)

    @property
    def list(self):
        return self.__list.copy()