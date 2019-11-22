from trainer_stats import TrainerStats
from abstract_trainer import AbstractTrainer
from regular_trainer import RegularTrainer
from gym_leader import GymLeader

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from base import Base
from os import path
import json


class TrainerManager(AbstractTrainer):
    """ TrainerManager class """

    def __init__(self, db_filename):
        """ Constructor for TrainerManager """
        self._filepath_validator(db_filename)

        engine = create_engine('sqlite:///' + db_filename, poolclass=NullPool)

        # Bind the engine to the metadata of the Base class so that the
        # declaratives can be accessed through a DBSession instance
        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)

    def add(self, trainer):
        """ Adds an AbstractTrainer object to trainers list """
        # Validates Trainer
        TrainerManager._abstracttrainer_validator(trainer)

        session = self._db_session()
        session.add(trainer)
        session.commit()
        db_trainer = session.query(AbstractTrainer).order_by(
            AbstractTrainer.trainer_id.desc()).first()

        session.close()

        return db_trainer.trainer_id

    def get_trainer_by_id(self, id):
        """ Gets trainer by trainer id """
        # Validates id
        TrainerManager._int_validator(id)
        # Database Query
        session = self._db_session()
        existing_trainer = session.query(RegularTrainer).filter(
            RegularTrainer.trainer_id == id).first()
        if _abstracttrainer_validator(
                existing_trainer) and existing_trainer.type == "Gym Leader":
            existing_trainer = None
        if existing_trainer is None:
            existing_trainer = session.query(GymLeader).filter(
                GymLeader.trainer_id == id).first()
        session.close()

        return existing_trainer

    def get_all(self):
        """ Gets all trainers """
        all_trainer_list = []

        session = self._db_session()
        trainers = session.query(AbstractTrainer).all()
        session.close()

        for trainer in trainers:
            all_trainer_list.append(self.get_trainer_by_id(trainer.trainer_id))

        return all_trainer_list

    def get_all_by_type(self, type):
        """ Gets all trainers by type """
        # Validation
        TrainerManager._str_validator(type)

        # Database Query
        session = self._db_session()
        if type == 'Regular Trainer':
            trainer_query = session.query(RegularTrainer).filter(
                RegularTrainer.type == "Regular Trainer").all()
        if type == 'Gym Leader':
            trainer_query = session.query(GymLeader).filter(
                GymLeader.type == "Gym Leader").all()

        return trainer_query

    def get_all_by_location(self, location):
        """ Gets all trainers by location """
        # Validation
        TrainerManager._str_validator(location)

        # Database Query
        all_trainers = self.get_all()
        all_trainers_in_location = []

        for trainer in all_trainers:
            if trainer.location == location:
                all_trainers_in_location.append(trainer)

        return all_trainers_in_location

    def update(self, trainer):
        """ Updates trainer object """
        # Validation
        TrainerManager._abstracttrainer_validator(trainer)

        session = self._db_session()

        old_trainer = session.query(RegularTrainer).filter(
            RegularTrainer.trainer_id == trainer.id).first()

        # Skips first None return to check for Gym Leader
        if old_trainer is None:
            pass
        elif old_trainer.type == "Gym Leader":
            old_trainer = None

        if old_trainer is None:
            old_trainer = session.query(GymLeader).filter(
                GymLeader.trainer_id == trainer.id).first()

        if old_trainer is None:
            session.close()
            raise ValueError('ID not found in database')

        trainer = trainer.to_dict()
        trainer_pokemon_team = str(trainer['pokemon_team'])
        # For some reason, JSON double quotations becomes single quotations
        trainer_pokemon_team = trainer_pokemon_team.replace("\'", "\"")

        if old_trainer.type == 'Regular Trainer':
            session.query(RegularTrainer).filter(
                RegularTrainer.trainer_id == old_trainer.trainer_id).update({
                    'name':
                    str(trainer['name']),
                    'pokemon_team':
                    trainer_pokemon_team,
                    'trainer_class':
                    str(trainer['trainer_class']),
                    'pokecoins':
                    str(trainer['pokecoins']),
                    'location':
                    str(trainer['location']),
                    'movement_type':
                    str(trainer['movement_type']),
                    'phone_num':
                    str(trainer['phone_num']),
                    'have_partner':
                    str(trainer['have_partner'])
                })
        elif old_trainer.type == 'Gym Leader':
            session.query(GymLeader).filter(
                GymLeader.trainer_id == old_trainer.trainer_id).update({
                    'name':
                    str(trainer['name']),
                    'pokemon_team':
                    trainer_pokemon_team,
                    'trainer_class':
                    str(trainer['trainer_class']),
                    'pokecoins':
                    str(trainer['pokecoins']),
                    'location':
                    str(trainer['location']),
                    'badge':
                    str(trainer['badge']),
                    'element':
                    str(trainer['element']),
                    'prize':
                    str(trainer['prize'])
                })

        session.commit()
        session.close()

    def delete(self, id):
        """ Deletes trainer from trainers """
        # Validation
        TrainerManager._int_validator(id)

        # Database Query
        session = self._db_session()

        existing_trainer = session.query(AbstractTrainer).filter(
            AbstractTrainer.trainer_id == id).first()

        if existing_trainer is None:
            session.close()
            raise ValueError('Incorrect value: id not in use')

        session.delete(existing_trainer)
        session.commit()

        session.close()

    def get_stats(self):
        """ Fetches detailed trainer stats """
        session = self._db_session()

        trainers = session.query(AbstractTrainer).all()

        num_total_trainers = 0
        num_gym_leaders = 0
        num_regular_trainers = 0
        num_trainers_with_partner = 0
        num_trainer_per_location = {}

        for trainer in trainers:
            num_total_trainers += 1
            if trainer.type == 'Regular Trainer':
                num_regular_trainers += 1
                if trainer.have_partner is 1:
                    num_trainers_with_partner += 1
            else:
                num_gym_leaders += 1

        for trainer in trainers:
            if trainer.location in num_trainer_per_location:
                num_trainer_per_location[trainer.location] += 1
            else:
                num_trainer_per_location.update({trainer.location: 1})

        stats_output = TrainerStats(
            num_total_trainers, num_gym_leaders, num_regular_trainers,
            num_trainers_with_partner, num_trainer_per_location)

        return stats_output

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
