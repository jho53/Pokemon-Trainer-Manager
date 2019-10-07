from abstract_trainer import AbstractTrainer


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Gym Leader'

    def __init___(self, id, pokemon_team, trainer_class, pokecoins, location, badge, element, prize):
        """ Constructor for GymLeader """
        self._id = id
        self._pokemon_team = pokemon_team
        self._trainer_class = trainer_class
        self._pokecoins = pokecoins
        self._location = location
        self._badge = badge
        self._element = element
        self._prize = prize

    def get_type(self):
        """ """
        pass

    def get_badge(self):
        """ """
        pass

    def get_element(self):
        """ """
        pass

    def get_prize(self):
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
