from abstract_trainer import AbstractTrainer


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Gym Leader'
    TRAINER_CLASS = 'Gym Leader'

    def __init__(self, name, pokemon_team, trainer_class, pokecoins, location, badge, element, prize):
        """ Constructor - Initializes the main attributes of GymLeader """
        super().__init__(name, pokemon_team, GymLeader.TRAINER_CLASS, pokecoins, location)
        GymLeader._str_validator(badge)
        self._badge = badge
        GymLeader._str_validator(element)
        self._element = element
        GymLeader._str_validator(prize)
        self._prize = prize

    def get_type(self):
        """ Returns the trainer type """
        return GymLeader.TRAINER_TYPE

    # FIXME: add abstract method to UML
    def get_details(self):
        """ Return the trainer details """
        raise NotImplementedError("Child class must implement method.")

    def get_badge(self):
        """ Returns the badge """
        return self._badge

    def get_element(self):
        """ Returns the trainer element """
        return self._element

    def get_prize(self):
        """ Returns the prize """
        return self._prize

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or arg == '' or type(arg) != str:
            raise ValueError('Incorrect value: input should be a string')
