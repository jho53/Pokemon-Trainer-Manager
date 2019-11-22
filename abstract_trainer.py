from sqlalchemy import Column, String, Integer
from base import Base

import json


class AbstractTrainer(Base):
    """ Abstract Trainer class """

    __tablename__ = "trainer"

    trainer_id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    pokemon_team = Column(String(180), nullable=False)
    trainer_class = Column(String(60), nullable=False)
    pokecoins = Column(Integer, nullable=False)
    location = Column(String(60), nullable=False)
    type = Column(String(20), nullable=False)

    def __init__(self, name, pokemon_team, trainer_class, pokecoins, location,
                 type):
        """ Constructor for AbstractTrainer """
        AbstractTrainer._str_validator(name, 60)
        self.name = name

        AbstractTrainer._pokemon_team_validator(pokemon_team)
        self.pokemon_team = json.dumps(pokemon_team)

        AbstractTrainer._str_validator(trainer_class, 60)
        self.trainer_class = trainer_class

        AbstractTrainer._int_validator(pokecoins)
        self.pokecoins = pokecoins

        AbstractTrainer._str_validator(location, 60)
        self.location = location

        if type != "Regular Trainer" and type != "Gym Leader":
            raise ValueError("Type is not supported")
        self.type = type

    def get_details(self):
        """ Abstract method, raises error msg when called in abstract class """
        raise NotImplementedError("Child class must implement method.")

    def to_dict(self):
        """ Child class must implement method """
        raise NotImplementedError("Child class must implement method.")

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
    def _int_validator(arg):
        """ Validator for integer input """
        if arg is None or type(arg) != int:
            return ValueError("Incorrect value: input should an int")

    @staticmethod
    def _pokemon_team_validator(arg):
        """ Validate pokemon team """
        if type(arg) != dict:
            return ValueError("Incorrect value: input should be a dictionary")
