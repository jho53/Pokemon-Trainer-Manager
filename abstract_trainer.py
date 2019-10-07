class AbstractTrainer:
    """ Abstract Trainer class """

    def __init__(self, id, pokemon_team, trainer_class, pokecoins, location):
        """ constructor for AbstractTrainer """
        self._id = id
        self._pokemon_team = pokemon_team
        self._trainer_class = trainer_class
        self._pokecoins = pokecoins
        self._location = location

    def get_type(self):
        """ """
        pass

    def get_trainer(self):
        """ """
        pass

    def get_location(self):
        """ """
        pass

    def get_pokcoins(self):
        """ """
        pass

    def set_id(self, id):
        """ """
        pass

    def _get_id(self):
        """ """
        pass

    def _set_pokemon_team(self, pokemon_team):
        """ """
        pass

    def _get_pokemon_team(self):
        """ """
        pass

    @staticmethod
    def _str_validator(arg):
        """ validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')

    @staticmethod
    def _int_validator(arg):
        """ validator for integer input """
        if arg is None or type(arg) != int:
            return ValueError('Incorrect value: input should an int')

    @staticmethod
    def _float_validator(arg):
        """ validator for float input """
        if arg is None or type(arg) != float:
            return ValueError('Incorrect value: input should be a float')

    @staticmethod
    def _boolean_validator(arg):
        """ validator for boolean input """
        if arg is None or type(arg) != bool:
            return ValueError('Incorrect value: input should be boolean')
