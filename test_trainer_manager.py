from unittest import TestCase
from trainer_manager import TrainerManager
from gym_leader import GymLeader
from regular_trainer import RegularTrainer
from trainer_stats import TrainerStats

import sqlite3
import unittest
import time
import inspect
import os


class TestTrainerManager(TestCase):
    ''' Unit Tests for TrainerManager Class '''
    # Gym Leader Parameters
    VALID_GYMLEADER = GymLeader(
        'Brock', {
            'Golem': 55,
            'Rellcanth': 54,
            'Omastar': 56,
            'Kabutops': 55,
            'Onix': 61,
            'Ramparods': 57
        }, GymLeader.TRAINER_CLASS, 6840, 'Kanto', 'Boulder Badge', 'Rock',
        'HM10')

    # Regular Trainer Parameters
    VALID_TRAINER = RegularTrainer('Tom', {
        'Zubat': 21,
        'Ekans': 23
    }, 'Team Rocket Grunt', 540, 'Johto', 'Walking', False, True)

    # General Parameters
    ID_PARAMETER = 1
    DATABASE_FILE_PATH = "./test.sqlite"
    EMPTY_PARAMETER = ''
    UNDEFINED_PARAMETER = None
    TEST_STR_INPUT = 'Test'

    def setUp(self):
        '''Sets up test RegularTrainer class'''
        self.logTrainerManager()

        conn = sqlite3.connect(TestTrainerManager.DATABASE_FILE_PATH)

        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS trainer(
            trainer_id INTEGER PRIMARY KEY ASC,
            name VARCHAR(60) NOT NULL,
            pokemon_team VARCHAR(180) NOT NULL,
            trainer_class VARCHAR(60) NOT NULL,
            type VARCHAR(20) NOT NULL,
            pokecoins INTEGER NOT NULL,
            location VARCHAR(60) NOT NULL,
            movement_type VARCHAR(10),
            phone_num INTEGER,
            have_partner INTEGER,
            badge VARCHAR(20),
            element VARCHAR(20),
            prize VARCHAR(20)
            );
        ''')

        conn.commit()
        conn.close()

        self.trainer_manager = TrainerManager(
            TestTrainerManager.DATABASE_FILE_PATH)

        self.assertIsNotNone(self.trainer_manager)

    def tearDown(self):
        '''Tears down test RegularTrainer class'''
        conn = sqlite3.connect(TestTrainerManager.DATABASE_FILE_PATH)
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS trainer''')
        conn.commit()
        conn.close()

        os.remove(TestTrainerManager.DATABASE_FILE_PATH)

        self.logTrainerManager()

    def logTrainerManager(self):
        '''Creates log info inside console'''
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_valid_init(self):
        '''Tests valid parameters for TrainerManager constructor'''
        self.trainer_manager = TrainerManager(
            TestTrainerManager.DATABASE_FILE_PATH)
        self.assertIsNotNone(self.trainer_manager)

    def test_invalid_init(self):
        '''Tests invalid parameters for TrainerManager constructor'''
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be a valid filepath',
            TrainerManager, TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be a valid filepath',
            TrainerManager, TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be a valid filepath',
            TrainerManager, TestTrainerManager.TEST_STR_INPUT)

    def test_valid_add(self):
        '''Tests if TrainerManager accepts valid AbstractTrainer objects'''
        self.assertEqual(
            1, self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER))
        self.assertEqual(
            2, self.trainer_manager.add(TestTrainerManager.VALID_TRAINER))
        self.assertEqual(2, len(self.trainer_manager.get_all()))

    def test_invalid_add(self):
        '''Tests if TrainerManager rejects invalid AbstractTrainer objects'''
        self.assertRaisesRegex(
            TypeError, 'Incorrect value: input should be a AbstractTrainer',
            self.trainer_manager.add, TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertEqual(0, len(self.trainer_manager.get_all()))

    def test_valid_get_trainer_by_id(self):
        '''Tests if TrainerManager returns trainer by id'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.assertEqual(
            TestTrainerManager.VALID_GYMLEADER,
            self.trainer_manager.get_trainer_by_id(
                TestTrainerManager.ID_PARAMETER))

    def test_invalid_get_trainer_by_id(self):
        '''Tests if get_trainer_by_id rejects invalid parameters'''
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be an int',
                               self.trainer_manager.get_trainer_by_id,
                               TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be an int',
                               self.trainer_manager.get_trainer_by_id,
                               TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertIsNone(self.trainer_manager.get_trainer_by_id(999))

    def test_get_all(self):
        '''Tests if TrainerManager returns all trainers'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        get_all_object = self.trainer_manager.get_all()
        self.assertEqual(2, len(self.trainer_manager.get_all()))
        self.assertEqual(TestTrainerManager.VALID_GYMLEADER, get_all_object[0])
        self.assertEqual(TestTrainerManager.VALID_TRAINER, get_all_object[1])

    def test_valid_get_all_by_type(self):
        '''Tests if TrainerManager returns trainers by type'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        # Store results in variables
        get_all_gym_leader_obj = self.trainer_manager.get_all_by_type(
            GymLeader.TRAINER_TYPE)
        get_all_trainer_obj = self.trainer_manager.get_all_by_type(
            RegularTrainer.TRAINER_TYPE)
        # Matching results
        self.assertEqual(3, len(get_all_gym_leader_obj))
        self.assertEqual(2, len(get_all_trainer_obj))
        self.assertEqual(TestTrainerManager.VALID_GYMLEADER,
                         get_all_gym_leader_obj[0])
        self.assertEqual(TestTrainerManager.VALID_TRAINER,
                         get_all_trainer_obj[1])

    def test_invalid_get_all_by_type(self):
        '''Tests if TrainerManager.get_all_by_type() rejects invalid parameters'''
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_type,
                               TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_type,
                               TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_type,
                               TestTrainerManager.ID_PARAMETER)

    def test_valid_get_all_by_location(self):
        '''Tests if TrainerManager returns trainers by location'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        # Store results in variables
        get_all_gym_leader_obj = self.trainer_manager.get_all_by_location(
            'Kanto')
        get_all_trainer_obj = self.trainer_manager.get_all_by_location('Johto')
        # Matching results
        self.assertEqual(3, len(get_all_gym_leader_obj))
        self.assertEqual(2, len(get_all_trainer_obj))
        self.assertEqual(TestTrainerManager.VALID_GYMLEADER,
                         get_all_gym_leader_obj[0])
        self.assertEqual(TestTrainerManager.VALID_TRAINER,
                         get_all_trainer_obj[1])

    def test_invalid_get_all_by_location(self):
        '''Tests if TrainerManager.get_all_by_location() rejects invalid parameters'''
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_location,
                               TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_location,
                               TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_location,
                               TestTrainerManager.ID_PARAMETER)

    def test_valid_update(self):
        '''Tests if TrainerManager.update() updates via id'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        new_gym_leader = GymLeader(
            'Twink', {
                'Golem': 55,
                'Rellcanth': 54,
                'Omastar': 56,
                'Kabutops': 55,
                'Onix': 61,
                'Ramparods': 57
            }, GymLeader.TRAINER_CLASS, 6840, 'Kanto', 'Boulder Badge', 'Rock',
            'HM10')
        new_gym_leader.id = 0
        self.trainer_manager.update(new_gym_leader)
        self.assertEqual(new_gym_leader, self.trainer_manager.get_all()[0])

    def test_invalid_update(self):
        '''Tests if TrainerManager.update() rejects invalid parameters'''
        self.assertRaisesRegex(
            TypeError, 'Incorrect value: input should be a AbstractTrainer',
            self.trainer_manager.update, None)
        new_gym_leader = GymLeader(
            'Twink', {
                'Golem': 55,
                'Rellcanth': 54,
                'Omastar': 56,
                'Kabutops': 55,
                'Onix': 61,
                'Ramparods': 57
            }, GymLeader.TRAINER_CLASS, 6840, 'Kanto', 'Boulder Badge', 'Rock',
            'HM10')
        new_gym_leader.id = 20
        self.assertRaisesRegex(ValueError, 'ID not found in database',
                               self.trainer_manager.update, new_gym_leader)

    def test_valid_delete(self):
        '''Tests if TrainerManager.delete() deletes via id'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.trainer_manager.delete(0)
        self.assertEqual(1, len(self.trainer_manager.get_all()))

    def test_invalid_delete(self):
        '''Tests if TrainerManager.delete() rejects invalid parameters'''
        self.assertRaisesRegex(ValueError,
                               'Incorrect value: input should be an int',
                               self.trainer_manager.delete,
                               TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: id not in use',
                               self.trainer_manager.delete, 15)
        self.assertRaisesRegex(ValueError, 'Incorrect value: id not in use',
                               self.trainer_manager.delete, -15)

    def test_get_stats(self):
        '''Tests if TrainerManager.get_stats() displays correct output'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.assertTrue(
            isinstance(self.trainer_manager.get_stats(), TrainerStats))

        self.assertEqual(
            3,
            self.trainer_manager.get_stats().get_num_regular_trainer())
        self.assertEqual(3,
                         self.trainer_manager.get_stats().get_num_gym_leader())
        self.assertEqual(6,
                         self.trainer_manager.get_stats().get_num_trainers())
        self.assertEqual(
            3,
            self.trainer_manager.get_stats().get_num_trainer_have_partner())
        self.assertEqual(
            dict,
            type(self.trainer_manager.get_stats().get_num_per_location()))
        self.assertEqual(
            {
                'Johto': 3,
                'Kanto': 3
            },
            self.trainer_manager.get_stats().get_num_per_location())


if __name__ == "__main__":
    unittest.main()
