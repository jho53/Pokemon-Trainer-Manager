from unittest import TestCase
from trainer_manager import TrainerManager
from gym_leader import GymLeader
from regular_trainer import RegularTrainer

import unittest
import inspect


class TestTrainerManager(TestCase):
    ''' Unit Tests for TrainerManager Class '''
    # Gym Leader Parameters
    VALID_GYMLEADER = GymLeader('Brock', {
        'Golem': 55,
        'Rellcanth': 54,
        'Omastar': 56,
        'Kabutops': 55,
        'Onix': 61,
        'Ramparods': 57
    }, GymLeader.TRAINER_CLASS, 6840, 'Kanto', 'Boulder Badge', 'Rock', 'HM10')

    # Regular Trainer Parameters
    VALID_TRAINER = RegularTrainer('Tom', {
        'Zubat': 21,
        'Ekans': 23
    }, 'Team Rocket Grunt', 540, 'Johto', 'Walking', False, True)

    # General Parameters
    ID_PARAMETER = 0
    EMPTY_PARAMETER = ''
    UNDEFINED_PARAMETER = None
    TEST_STR_INPUT = 'Test'

    def setUp(self):
        '''Sets up test RegularTrainer class'''
        self.logTrainerManager()
        self.trainer_manager = TrainerManager(
            TestTrainerManager.ID_PARAMETER, [])
        self.assertIsNotNone(self.trainer_manager)

    def teardown(self):
        '''Tears down test RegularTrainer class'''
        del self.trainer_manager
        self.logTrainerManager()

    def logTrainerManager(self):
        '''Creates log info inside console'''
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_valid_init(self):
        '''Tests valid parameters for TrainerManager constructor'''
        self.trainer_manager = TrainerManager(TestTrainerManager.ID_PARAMETER)
        self.assertIsNotNone(self.trainer_manager)

    def test_invalid_init(self):
        '''Tests invalid parameters for TrainerManager constructor'''
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should an int',
                               TrainerManager, TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should an int',
                               TrainerManager, TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should an int',
                               TrainerManager, TestTrainerManager.TEST_STR_INPUT)

    def test_valid_add(self):
        '''Tests if TrainerManager accepts valid AbstractTrainer objects'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.trainer_manager.add(TestTrainerManager.VALID_TRAINER)
        self.assertEqual(2, len(self.trainer_manager.get_all()))

    def test_invalid_add(self):
        '''Tests if TrainerManager rejects invalid AbstractTrainer objects'''
        self.assertRaisesRegex(TypeError, 'Incorrect value: input should be a AbstractTrainer',
                               self.trainer_manager.add, None)
        self.assertEqual(0, len(self.trainer_manager.get_all()))

    def test_get_trainer_by_id(self):
        '''Tests if TrainerManager returns trainer by id'''
        self.trainer_manager.add(TestTrainerManager.VALID_GYMLEADER)
        self.assertEqual(TestTrainerManager.VALID_GYMLEADER, self.trainer_manager.get_trainer_by_id(
            TestTrainerManager.ID_PARAMETER))

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
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_type, TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_type, TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_type, TestTrainerManager.ID_PARAMETER)

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
        get_all_trainer_obj = self.trainer_manager.get_all_by_location(
            'Johto')
        # Matching results
        self.assertEqual(3, len(get_all_gym_leader_obj))
        self.assertEqual(2, len(get_all_trainer_obj))
        self.assertEqual(TestTrainerManager.VALID_GYMLEADER,
                         get_all_gym_leader_obj[0])
        self.assertEqual(TestTrainerManager.VALID_TRAINER,
                         get_all_trainer_obj[1])

    def test_invalid_get_all_by_location(self):
        '''Tests if TrainerManager.get_all_by_location() rejects invalid parameters'''
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_location, TestTrainerManager.EMPTY_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_location, TestTrainerManager.UNDEFINED_PARAMETER)
        self.assertRaisesRegex(ValueError, 'Incorrect value: input should be a string',
                               self.trainer_manager.get_all_by_location, TestTrainerManager.ID_PARAMETER)

    # @FIXME FINISH UPDATE AND DELETE UNIT TESTS

    def test_valid_update(self):
        '''Tests if TrainerManager.update() updates via id'''

    def test_invalid_update(self):
        '''Tests if TrainerManager.update() rejects invalid parameters'''

    def test_valid_delete(self):
        '''Tests if TrainerManager.delete() deletes via id'''

    def test_invalid_delete(self):
        '''Tests if TrainerManager.delete() rejects invalid parameters'''


if __name__ == "__main__":
    unittest.main()
