from abstract_trainer import AbstractTrainer
from sqlalchemy import Column, String, Integer

import json


class RegularTrainer(AbstractTrainer):
    """ RegularTrainer class (derived from AbstractTrainer) """

    # SQLite Configurations
    movement_type = Column(String(10))
    phone_num = Column(Integer)
    have_partner = Column(Integer)

    # Class Variables
    BOOLEAN_FALSE = 0
    BOOLEAN_TRUE = 1

    TRAINER_TYPE = "Regular Trainer"
    MOVEMENT_TYPE_DICT = {
        "On Bike": 2.0,
        "Swimming": 1.5,
        "Walking": 1.0,
        "Running": 1.25
    }

    def __init__(self,
                 name,
                 pokemon_team,
                 trainer_class,
                 pokecoins,
                 location,
                 movement_type,
                 phone_num,
                 have_partner,
                 type="Regular Trainer"):
        """ Constructor for RegularTrainer """
        super().__init__(name, pokemon_team, trainer_class, pokecoins,
                         location, type)

        RegularTrainer._str_validator(movement_type, 10)
        if movement_type not in RegularTrainer.MOVEMENT_TYPE_DICT:
            raise ValueError("Incorrect value: no match found in database")
        self.movement_type = movement_type

        RegularTrainer._boolean_validator(phone_num)
        if phone_num:
            self.phone_num = RegularTrainer.BOOLEAN_TRUE
        else:
            self.phone_num = RegularTrainer.BOOLEAN_FALSE

        RegularTrainer._boolean_validator(have_partner)
        if have_partner:
            self.have_partner = RegularTrainer.BOOLEAN_TRUE
        else:
            self.have_partner = RegularTrainer.BOOLEAN_FALSE

    def get_details(self):
        """ Return the trainer details """
        return ("{0} {1} from {2} has {3} pokemon(s)").format(
            self.trainer_class, self.name, self.location,
            len(self.pokemon_team))

    def get_movement_speed(self):
        """ Return the movement speed """
        movement_speed = RegularTrainer.MOVEMENT_TYPE_DICT.get(
            self.movement_type)
        return movement_speed

    def to_dict(self):
        """ Returns Python dictionary representation of RegularTrainer """
        dict = {}

        dict["trainer_id"] = self.trainer_id
        dict["name"] = self.name
        dict["pokemon_team"] = json.loads(self.pokemon_team)
        dict["trainer_class"] = self.trainer_class
        dict["pokecoins"] = self.pokecoins
        dict["location"] = self.location
        dict["movement_type"] = self.movement_type
        dict["phone_num"] = self.phone_num
        dict["have_partner"] = self.have_partner
        dict["type"] = self.TRAINER_TYPE

        return dict

    @staticmethod
    def _str_validator(arg, max_length):
        """ Validator for string input """
        if arg is None or arg == "" or type(arg) != str:
            raise ValueError("Incorrect value: input should be a string")
        if len(arg) > max_length:
            raise OverflowError(
                "Exceeded length: input should be 0 - %d characters long" %
                max_length)

    @staticmethod
    def _boolean_validator(arg):
        """ Validator for boolean input """
        if arg is None or arg == "" or type(arg) != bool:
            raise ValueError("Incorrect value: input should be boolean")
