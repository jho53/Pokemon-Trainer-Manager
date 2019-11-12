class AbstractTrainer:
    """ Abstract Trainer class """

    def __init__(self, name, pokemon_team, trainer_class, pokecoins, location):
        """ Constructor for AbstractTrainer """
        AbstractTrainer._int_validator(id)
        self._id = id
        AbstractTrainer._str_validator(name)
        self._name = name
        AbstractTrainer._pokemon_team_validator(pokemon_team)
        self._pokemon_team = pokemon_team
        AbstractTrainer._str_validator(trainer_class)
        self._trainer_class = trainer_class
        AbstractTrainer._int_validator(pokecoins)
        self._pokecoins = pokecoins
        AbstractTrainer._str_validator(location)
        self._location = location

    def get_type(self):
        """ Abstract method, returns error msg when called in abstract class """
        raise NotImplementedError("Child class must implement method.")

    def get_details(self):
        """ Abstract method, returns error msg when called in abstract class """
        raise NotImplementedError("Child class must implement method.")

    def get_name(self):
        """ Returns the trainer name """
        return self._name

    def get_trainer_class(self):
        """ Returns trainer class """
        return self._trainer_class

    def get_location(self):
        """ Returns location """
        return self._location

    def get_pokecoins(self):
        """ Returns total amount of pokecoins """
        return self._pokecoins

    def _set_id(self, id):
        """ Sets ID for current trainer """
        AbstractTrainer._int_validator(id)
        self._id = id

    def _get_id(self):
        """ Returns ID for current trainer """
        return self._id

    def get_pokemon_team(self):
        """ Returns pokemon team for current trainer """
        return self._pokemon_team

    def to_dict(self):
        """ Child class must implement method """
        raise NotImplementedError("Child class must implement method.")

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
        """ Validate pokemon team. Format [[Pokemon: Level]] eg. [['Diglett', 35]] """
        if type(arg) != dict:
            return ValueError('Incorrect value: input should be a dictionary. Format example: {"Zubat": 21, "Ekans": 23}')

    id = property(_get_id, _set_id)
