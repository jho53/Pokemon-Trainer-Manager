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
        return AbstractTrainer.id

    def get_trainer_by_id(self, id):
        """ Gets trainer by trainer id """
        TrainerManager._int_validator(id)
        for trainer in self._trainers:
            if id == trainer._get_id():
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

    def update(self, id, AbstractTrainer):
        """ Updates trainer object """
        # Validation
        TrainerManager._abstracttrainer_validator(AbstractTrainer)
        TrainerManager._int_validator(id)
        if id > len(self._trainers) - 1 or id < 0:
            raise ValueError('Incorrect value: id not in use')

        for num, trainer in enumerate(self._trainers):
            if trainer.id is id:
                self._trainers[num] = AbstractTrainer
                break

    def delete(self, id):
        """ Deletes trainer from trainers """
        TrainerManager._int_validator(id)
        if id > len(self._trainers) - 1 or id < 0:
            raise ValueError('Incorrect value: id not in use')
        for trainer in self._trainers:
            if id is trainer.id:
                self._trainers.remove(trainer)
                return
        raise ValueError('Incorrect value: id not in use')

    # FIXME: need to get number of trainers per location
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

        stats_output = TrainerStats(_num_total_trainers, _num_gym_leaders,
                                    _num_regular_trainers, _num_trainers_with_partner, _num_trainer_per_location)
        return stats_output

    def _read_entities_from_file(self):
        """ Reads entities from file """

        # TODO: Implementation
        pass

    def _write_entities_to_file(self):
        """ Writes entities to file """

        # TODO: Implementation
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
            raise ValueError('Incorrect value: input should be an int')

    @staticmethod
    def _str_validator(arg):
        """ Validator for string input """
        if arg is None or arg == '' or type(arg) != str:
            raise ValueError('Incorrect value: input should be a string')
