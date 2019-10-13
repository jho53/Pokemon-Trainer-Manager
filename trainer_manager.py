from trainer_stats import TrainerStats
from abstract_trainer import AbstractTrainer


class TrainerManager(AbstractTrainer):
    """ TrainerManager class """

    def __init__(self, next_available_id, trainers=[]):
        """ Constructor for TrainerManager """
        TrainerManager._int_validator(next_available_id)
        self._next_available_id = next_available_id
        self._trainers = trainers

    def add(self, AbstractTrainer):
        """ Adds an AbstractTrainer object to trainers list """
        TrainerManager._abstracttrainer_validator(AbstractTrainer)
        AbstractTrainer.id = self._next_available_id
        self._trainers.append(AbstractTrainer)
        self._next_available_id += 1

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

    # @FIXME FINISH UPDATE AND DELETE FUNCTIONS

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
    def _abstracttrainer_validator(trainer):
        """ Validator for AbstractTrainer input """
        if not isinstance(trainer, AbstractTrainer):
            raise TypeError(
                'Incorrect value: input should be a AbstractTrainer')

    @staticmethod
    def _int_validator(arg):
        """ Validator for integer input """
        if arg is None or type(arg) != int:
            raise ValueError('Incorrect value: input should an int')

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or arg == '' or type(arg) != str:
            raise ValueError('Incorrect value: input should be a string')
