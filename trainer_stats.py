class TrainerStats:
    """ Trainer stats class """

    def __init__(self, num_trainers, num_gym_leader, num_regular_trainer,
                 num_have_partner, num_per_location):
        """ Constructor for TrainerStats """
        self._num_trainers = num_trainers
        self._num_gym_leaders = num_gym_leader
        self._num_regular_trainer = num_regular_trainer
        self._num_have_partner = num_have_partner
        self._num_per_location = num_per_location

    def get_num_trainers(self):
        """ Return number of trainers """
        return self._num_trainers

    def get_num_gym_leader(self):
        """ Return number of gym leaders """
        return self._num_gym_leaders

    def get_num_regular_trainer(self):
        """ Return number of regular trainers """
        return self._num_regular_trainer

    def get_num_trainer_have_partner(self):
        """ Return number of trainers with partner """
        return self._num_have_partner

    def get_num_per_location(self):
        """ Return number of trainers per location """
        return self._num_per_location
