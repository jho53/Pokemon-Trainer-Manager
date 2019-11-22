from abstract_trainer import AbstractTrainer
from sqlalchemy import Column, String, Integer

import json


class GymLeader(AbstractTrainer):
    """ GymLeader class (derived from AbstractTrainer) """

    # SQLite Configurations
    badge = Column(String(20))
    element = Column(String(20))
    prize = Column(String(20))

    TRAINER_TYPE = "Gym Leader"
    TRAINER_CLASS = "Gym Leader"

    def __init__(self,
                 name,
                 pokemon_team,
                 trainer_class,
                 pokecoins,
                 location,
                 badge,
                 element,
                 prize,
                 type="Gym Leader"):
        """ Constructor - Initializes the main attributes of GymLeader """
        super().__init__(name, pokemon_team, GymLeader.TRAINER_CLASS,
                         pokecoins, location, type)

        GymLeader._str_validator(badge, 20)
        self.badge = badge

        GymLeader._str_validator(element, 20)
        self.element = element

        GymLeader._str_validator(prize, 20)
        self.prize = prize

    def get_details(self):
        """ Return the trainer details """
        return ("{0} {1} {2} from {3} has {4} pokemon(s)").format(
            self.element, GymLeader.TRAINER_CLASS, self.name, self.location,
            len(self.pokemon_team))

    def to_dict(self):
        """ Returns Python dictionary representation of GymLeader """
        dict = {}

        dict["trainer_id"] = self.trainer_id
        dict["name"] = self.name
        dict["pokemon_team"] = json.loads(self.pokemon_team)
        dict["trainer_class"] = self.trainer_class
        dict["pokecoins"] = self.pokecoins
        dict["location"] = self.location
        dict["badge"] = self.badge
        dict["element"] = self.element
        dict["prize"] = self.prize
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
