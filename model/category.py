class Category:
    __attributes = ('_name')

    def __init__(self, name: str) -> None:
        self.__set_name(name)

    '''
        __setattr__ é para evitar a criação de atributos fora da classe.
    '''

    def __setattr__(self, key, value):
        if key not in self.__attributes:
            raise AttributeError(f'Não foi possível '
                                 f'adicionar o atributo {key}')
        object.__setattr__(self, key, value)

    def __str__(self) -> str:
        return f'Categoria: {self.name}'

    def __eq__(self, other_name: 'Category') -> bool:
        return self.name == other_name.name

    def __ne__(self, other_name: 'Category') -> bool:
        return not self.__eq__(other_name)

    def __set_name(self, name: str) -> None:
        name_is_empty = len(name) == 0
        if name_is_empty:
            raise Exception('Nome não pode ser vazio')
        self._name = name

    @property
    def name(self) -> str:
        return self._name
