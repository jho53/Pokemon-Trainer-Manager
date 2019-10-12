from abstract_trainer import AbstractTrainer


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Gym Leader'

    def __init___(self, id, pokemon_team, trainer_class, pokecoins, location,
                  badge, element, prize):
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
        """ Validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')