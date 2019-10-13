class TrainerStats:
    """ Trainer stats class """

    def __init__(self, num_trainers, num_gym_leader, num_regular_trainer,
                 num_movement_type, num_have_partner, num_per_location):
        """ Constructor for TrainerStats """
        TrainerStats._int_validator(num_trainers)
        self._num_trainers = num_trainers
        TrainerStats._int_validator(num_gym_leader)
        self._num_gym_leaders = num_gym_leader
        TrainerStats._int_validator(num_regular_trainer)
        self._num_regular_trainer = num_regular_trainer
        TrainerStats._int_validator(num_movement_type)
        self._num_movement_type = num_movement_type
        TrainerStats._int_validator(num_have_partner)
        self._num_have_partner = num_have_partner
        TrainerStats._int_validator(num_per_location)
        self._num_per_location = num_per_location

    def get_num_trainers(self):
        """ Return number of trainers """
        return self._num_trainers

    def get_num_gym_leader(self):
        """ Return number of gym leaders """
        return self._num_gym_leaders

    def get_num_regular_trainer(self):
        """ Return number of regular trainers """
        return self._num_regular_trainer

    def get_num_movement_type(self, type):
        """ Return number of trainers with specific movement type """
        pass

    def get_num_trainer_have_partner(self):
        """ Return number of trainers with partner """
        return self._num_have_partner

    def get_num_per_location(self):
        """ Return number of trainers per location """
        return self._num_per_location

    # FIXME: add validator to UML
    @staticmethod
    def _int_validator(arg):
        """ Validator for integer input """
        if arg is None or type(arg) != int:
            return ValueError('Incorrect value: input should an int')

    # FIXME: add validator to UML
    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')
