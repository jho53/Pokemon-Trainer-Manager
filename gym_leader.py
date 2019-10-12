from abstract_trainer import AbstractTrainer


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Gym Leader'

    def __init___(self, id, pokemon_team, trainer_class, pokecoins, location, badge, element, prize):
        """ Constructor - Initializes the main attributes of GymLeader """
        self._id = id
        self._pokemon_team = pokemon_team
        self._trainer_class = trainer_class
        self._pokecoins = pokecoins
        self._location = location
        self._badge = badge
        self._element = element
        self._prize = prize

    def get_type(self):
        """ Returns the type """
        return GymLeader.TRAINER_TYPE

    def get_badge(self):
        """ Returns the badge """
        return self._badge

    def get_element(self):
        """ Returns the element """
        return self._element

    def get_prize(self):
        """ Returns the prize """
        return self._prize

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
