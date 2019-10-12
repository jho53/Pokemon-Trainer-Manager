from abstract_trainer import AbstractTrainer


class RegularTrainer(AbstractTrainer):
    """ RegularTrainer class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Regular Trainer'
    MOVEMENT_TYPE = {
        'On Bike': 2.0,
        'Swimming': 1.5,
        'Walking': 1.0,
        'Running': 1.25
    }

    def __init___(self, id, name, pokemon_team, trainer_class, pokecoins, location,
                  movement_type, phone_num, have_partner):
        """ Constructor for RegularTrainer """
        super().__init__(id, name, pokemon_team, trainer_class, pokecoins, location)
        self._movement_type = movement_type
        self._phone_num = phone_num
        self._have_partner = have_partner

    def get_type(self):
        """ Return the trainer type """
        return RegularTrainer.TRAINER_TYPE

    def get_movement(self):
        """ Return the movement type """
        return RegularTrainer.MOVEMENT_TYPE
    
    def get_movement_speed(self):
        """ """
        pass
      
    def have_phone_number(self):
        """ """
        pass

    def have_partner(self):
        """ Return True if trainer has partner """
        return self._have_partner

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
