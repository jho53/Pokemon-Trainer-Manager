from trainer_stats import TrainerStats
from abstract_trainer import AbstractTrainer


class TrainerManager:
    """ TrainerManager class """

    def __init__(self):
        """ Constructor for TrainerManager """

    def add(self):
        """ """
        pass

    def get_all(self):
        """ """
        pass

    def get_all_by_type(self):
        """ """
        pass

    def get_all_by_location(self):
        """ """
        pass

    def update(self, AbstractTrainer):
        """ """
        pass

    def delete(self, id):
        """ """
        pass

    def get_stats(self):
        """ """
        pass

    @staticmethod
    def _abstracttrainer_validator(arg):
        """ validator for AbstractTrainer input """
        if not isinstance(arg, AbstractTrainer):
            return ValueError(
                'Incorrect value: input should be a AbstractTrainer')
