from trainer_stats import TrainerStats
from abstract_trainer import AbstractTrainer
from regular_trainer import RegularTrainer
from gym_leader import GymLeader
from os import path
import json


class TrainerManager(AbstractTrainer):
    """ TrainerManager class """

    def __init__(self, filepath):
        """ Constructor for TrainerManager """
        TrainerManager._filepath_validator(filepath)
        self._filepath = filepath

        self._trainers = []
        self._next_available_id = 0

        self._read_entities_from_file()

    def add(self, trainer):
        """ Adds an AbstractTrainer object to trainers list """
        TrainerManager._abstracttrainer_validator(trainer)
        trainer.id = self._next_available_id
        self._trainers.append(trainer)
        self._next_available_id += 1
        self._write_entities_to_file()
        return trainer.id

    def get_trainer_by_id(self, id):
        """ Gets trainer by trainer id """
        TrainerManager._int_validator(id)
        for trainer in self._trainers:
            if id is trainer.id:
                return trainer
        # if no match
        return None

    def get_all(self):
        """ Gets all trainers """
        return self._trainers

    def get_all_by_type(self, type):
        """ Gets all trainers by type """
        TrainerManager._str_validator(type)
        trainer_query = []
        for trainer in self._trainers:
            if type == trainer.get_type():
                trainer_query.append(trainer)
        return trainer_query

    def get_all_by_location(self, location):
        """ Gets all trainers by location """
        TrainerManager._str_validator(location)
        trainer_query = []
        for trainer in self._trainers:
            if location == trainer.get_location():
                trainer_query.append(trainer)
        return trainer_query

    def update(self, trainer):
        """ Updates trainer object """
        # Validation
        TrainerManager._abstracttrainer_validator(trainer)
        for num, current_trainer in enumerate(self._trainers):
            if current_trainer.id is trainer.id:
                self._trainers[num] = trainer
                self._write_entities_to_file()
                return
        raise ValueError('ID not found in database')

    def delete(self, id):
        """ Deletes trainer from trainers """
        TrainerManager._int_validator(id)
        if id > len(self._trainers) - 1 or id < 0:
            raise ValueError('Incorrect value: id not in use')
        for trainer in self._trainers:
            if id is trainer.id:
                self._trainers.remove(trainer)
                self._write_entities_to_file()
                return
        raise ValueError('Incorrect value: id not in use')

    def get_stats(self):
        """ Fetches detailed trainer stats """
        _num_total_trainers = 0
        _num_gym_leaders = 0
        _num_regular_trainers = 0
        _num_trainers_with_partner = 0
        _num_trainer_per_location = {}

        for trainer in self._trainers:
            _num_total_trainers += 1
            if trainer.get_type() == 'Regular Trainer':
                _num_regular_trainers += 1
                if trainer.have_partner() is True:
                    _num_trainers_with_partner += 1
            else:
                _num_gym_leaders += 1

        for trainer in self._trainers:
            if trainer.get_location() in _num_trainer_per_location:
                _num_trainer_per_location[trainer.get_location()] += 1
            else:
                _num_trainer_per_location.update({trainer.get_location(): 1})

        stats_output = TrainerStats(
            _num_total_trainers, _num_gym_leaders, _num_regular_trainers,
            _num_trainers_with_partner, _num_trainer_per_location)

        return stats_output

    def _read_entities_from_file(self):
        """ Reads entities from file """
        try:
            with open(self._filepath, 'r') as json_file:
                json_data = json.load(json_file)
        except Exception:
            json_data = []

        for trainer in json_data:
            if trainer["type"] == "Regular Trainer":
                temp_rt = RegularTrainer(
                    trainer['name'], trainer['pokemon_team'],
                    trainer['trainer_class'], trainer['pokecoins'],
                    trainer['location'], trainer['movement_type'],
                    trainer['phone_num'], trainer['have_partner'])
                temp_rt.id = trainer['id']
                self.add(temp_rt)
            elif trainer["type"] == "Gym Leader":
                temp_gl = GymLeader(trainer['name'], trainer['pokemon_team'],
                                    trainer['trainer_class'],
                                    trainer['pokecoins'], trainer['location'],
                                    trainer['badge'], trainer['element'],
                                    trainer['prize'])
                temp_gl.id = trainer['id']
                self.add(temp_gl)
            else:
                raise ValueError("Invalid trainer type")

    def _write_entities_to_file(self):
        """ Writes entities to file """
        temp_list = []

        for trainer in self._trainers:
            temp_list.append(trainer.to_dict())

        with open(self._filepath, "w") as outfile:
            json.dump(temp_list, outfile)

    @staticmethod
    def _abstracttrainer_validator(trainer):
        """ Validator for AbstractTrainer input """
        if not isinstance(trainer, AbstractTrainer):
            raise TypeError(
                'Incorrect value: input should be a AbstractTrainer')

    @staticmethod
    def _int_validator(arg):
        """ Validator for integer input """
        if arg is None or type(arg) != int:
            raise ValueError('Incorrect value: input should be an int')

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or arg is '' or type(arg) != str:
            raise ValueError('Incorrect value: input should be a string')

    @staticmethod
    def _filepath_validator(arg):
        """ Validator for filepath """
        if arg is None or path.exists(arg) is False:
            raise ValueError(
                'Incorrect value: input should be a valid filepath')
