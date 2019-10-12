class AbstractTrainer:
    """ Abstract Trainer class """

    def __init__(self, id, name, pokemon_team, trainer_class, pokecoins, location):
        """ Constructor for AbstractTrainer """
        self._id = id
        self.name = name
        self._pokemon_team = pokemon_team
        self._trainer_class = trainer_class
        self._pokecoins = pokecoins
        self._location = location

    def get_type(self):
        """ Abstract method, returns error msg when called in abstract class """
        pass

    def get_trainer_class(self):
        """ Returns trainer class """
        pass

    def get_location(self):
        """ Returns location """
        pass

    def get_pokecoins(self):
        """ Returns total amount of pokecoins """
        pass

    def set_id(self, id):
        """ Sets ID for current trainer """
        pass

    def _get_id(self):
        """ Returns ID for current trainer """
        pass

    def _set_pokemon_team(self, pokemon_team):
        """ Sets pokemon team for current trainer """
        pass

    def _get_pokemon_team(self):
        """ Returns pokemon team for current trainer """
        pass

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')

    @staticmethod
    def _int_validator(arg):
        """ Validator for integer input """
        if arg is None or type(arg) != int:
            return ValueError('Incorrect value: input should an int')

    @staticmethod
    def _pokemon_team_validator(arg):
        ''' Validator pokemon team '''
        pass
