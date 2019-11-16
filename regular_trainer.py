from abstract_trainer import AbstractTrainer


class RegularTrainer(AbstractTrainer):
    """ RegularTrainer class (derived from AbstractTrainer) """

    TRAINER_TYPE = 'Regular Trainer'
    MOVEMENT_TYPE_DICT = {
        'On Bike': 2.0,
        'Swimming': 1.5,
        'Walking': 1.0,
        'Running': 1.25
    }

    def __init__(self, name, pokemon_team, trainer_class, pokecoins, location,
                 movement_type, phone_num, have_partner):
        """ Constructor for RegularTrainer """
        super().__init__(name, pokemon_team, trainer_class, pokecoins,
                         location)
        RegularTrainer._str_validator(movement_type)
        if movement_type not in RegularTrainer.MOVEMENT_TYPE_DICT:
            raise ValueError('Incorrect value: no match found in database')
        self._movement_type = movement_type
        RegularTrainer._boolean_validator(phone_num)
        self._phone_num = phone_num
        RegularTrainer._boolean_validator(have_partner)
        self._have_partner = have_partner

    def get_type(self):
        """ Return the trainer type """
        return RegularTrainer.TRAINER_TYPE

    def get_details(self):
        """ Return the trainer details """
        return ('{0} {1} from {2} has {3} pokemon(s)').format(
            self._trainer_class, self._name, self._location,
            len(self._pokemon_team))

    def get_movement_speed(self):
        """ Return the movement speed """
        movement_type = self._movement_type
        movement_speed = RegularTrainer.MOVEMENT_TYPE_DICT.get(movement_type)
        return movement_speed

    def have_phone_number(self):
        """ Returns True if trainer has a phone number """
        return self._phone_num

    def have_partner(self):
        """ Return True if trainer has partner """
        return self._have_partner

    def to_dict(self):
        """ Returns Python dictionary representation of RegularTrainer """
        dict = {}

        dict['id'] = self._id
        dict['name'] = self._name
        dict['pokemon_team'] = self._pokemon_team
        dict['trainer_class'] = self._trainer_class
        dict['pokecoins'] = self._pokecoins
        dict['location'] = self._location
        dict['movement_type'] = self._movement_type
        dict['phone_num'] = self._phone_num
        dict['have_partner'] = self._have_partner
        dict['type'] = self.TRAINER_TYPE

        return dict

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or arg == '' or type(arg) != str:
            raise ValueError('Incorrect value: input should be a string')

    @staticmethod
    def _boolean_validator(arg):
        """ Validator for boolean input """
        if arg is None or arg == '' or type(arg) != bool:
            raise ValueError('Incorrect value: input should be boolean')
