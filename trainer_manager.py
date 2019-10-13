from trainer_stats import TrainerStats
from abstract_trainer import AbstractTrainer


class TrainerManager(AbstractTrainer):
    """ TrainerManager class """

    def __init__(self, next_available_id, trainers=[]):
        """ Constructor for TrainerManager """

        self._next_available_id = next_available_id
        TrainerManager._abstracttrainer_validator(trainers)
        self._trainers = trainers

    def add(self, AbstractTrainer):
        """ Adds an AbstractTrainer object to trainers list """
        TrainerManager._abstracttrainer_validator(AbstractTrainer)
        self._trainers.append(AbstractTrainer)

    def get_trainer_by_id(self, id):
        """ Gets trainer by trainer id """
        TrainerManager._int_validator(id)
        for trainer in self._trainers:
            if id == trainer._get_id():
                return trainer

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

    def update(self, AbstractTrainer):
        """ Updates trainer object """
        TrainerManager._abstracttrainer_validator(AbstractTrainer)
        pass

    def delete(self, id):
        """ Deletes trainer from trainers """
        TrainerManager._int_validator(id)
        for trainer in self._trainers:
            if id == trainer._get_id():
                self._trainers.remove(trainer)

    def get_stats(self):
        """ Gets trainer stats """
        pass

    @staticmethod
    def _abstracttrainer_validator(arg):
        """ validator for AbstractTrainer input """
        if not isinstance(arg, AbstractTrainer):
            return ValueError(
                'Incorrect value: input should be a AbstractTrainer')

    @staticmethod
    def _int_validator(arg):
        """ Validator for integer input """
        if arg is None or type(arg) != int:
            return ValueError('Incorrect value: input should an int')

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or type(arg) != str:
            return ValueError('Incorrect value: input should be a string')
