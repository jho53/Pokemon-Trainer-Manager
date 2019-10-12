from abstract_trainer import AbstractTrainer


class RegularTrainer(AbstractTrainer):
    """ RegularTrainer class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Regular Trainer'
    MOVEMENT_TYPE = ""

    def __init___(self, id, pokemon_team, trainer_class, pokecoins, location, movement, phone_num, have_partner):
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
        """ Return the trainer type """
        return RegularTrainer.TRAINER_TYPE

    def get_movement(self):
        """ Return the movement type """
        return RegularTrainer.MOVEMENT_TYPE

    def get_phone_number(self):
        """ Return the trainer phone number """
        return self._phone_num

    def have_partner(self):
        """ Return True if trainer has partner """
        return self._have_partner

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
