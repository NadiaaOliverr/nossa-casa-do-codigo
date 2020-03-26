class Category:

    def __init__(self, name):
        self.__set_name(name)

    def __str__(self):
        return f'Categoria: {self.name}'

    def __eq__(self, other_name):
        return self.name == other_name.name

    def __ne__(self, other_name):
        return not self.__eq__(other_name)

    def __set_name(self, name):
        name_is_empty = len(name) == 0
        if name_is_empty:
            raise Exception('Nome não pode ser vazio')
        self.__name = name

    @property
    def name(self):
        return self.__name