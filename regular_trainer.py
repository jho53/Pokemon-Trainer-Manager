from abstract_trainer import AbstractTrainer


class RegularTrainer(AbstractTrainer):
    """ RegularTrainer class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Regular Trainer'
    MOVEMENT_TYPE = ""

    def __init___(self, id, pokemon_team, trainer_class, pokecoins, location,
                  movement, phone_num, have_partner):
        """ Constructor for RegularTrainer """
        self._id = id
        self._pokemon_team = pokemon_team
        self._trainer_class = trainer_class
        self._pokecoins = pokecoins
        self._location = location
        self._movement = movement
        self._phone_num = phone_num
        self._have_partner = have_partner

    def get_type(self):
        """ """
        pass

    def get_movement(self):
        """ """
        pass

    def have_phone_number(self):
        """ """
        pass

    def have_partner(self):
        """ """
        pass

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')

    @staticmethod
    def _boolean_validator(arg):
        """ Validator for boolean input """
        if arg is None or type(arg) != bool:
            return ValueError('Incorrect value: input should be boolean')
