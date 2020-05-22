class Address:

    __attributes = ('_city', '_state', '_CEP')
    
    def __init__(self, city: str, state: str, CEP: str) -> None:
        self.__set_city(city)
        self.__set_state(state)
        self.__set_CEP(CEP)
        
    def __setattr__(self, key, value):
        if key not in self.__attributes:
            raise AttributeError(f'Não foi possível adicionar o atributo {key}')
        object.__setattr__(self, key, value)
        
    def __str__(self):
        return f'Cidade: {self.city} - Estado: {self.city} - CEP: {self.cep}'

    def __set_city(self, city: str) -> None:
        city_is_empty = len(city) == 0 or len(city.split()) == 0
        if city_is_empty:
            raise Exception('Cidade não pode ficar em branco')
        self._city = city

    def __set_state(self, state: str) -> None:
        state_is_empty = len(state) == 0 or len(state.split()) == 0
        if state_is_empty:
            raise Exception('Estado não pode ficar em branco')
        self._state = state

    def __set_CEP(self, CEP: str) -> None:
        CEP_is_empty = len(CEP) == 0 or len(CEP.split()) == 0
        if CEP_is_empty:
            raise Exception('CEP não pode ficar em branco')
        self._CEP = CEP
        
    @property
    def cep(self):
        return self._CEP
    
    @property
    def state(self):
        return self._state

    @property
    def city(self):
        return self._city
