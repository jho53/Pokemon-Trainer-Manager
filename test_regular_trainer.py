from unittest import TestCase
from regular_trainer import RegularTrainer
import unittest
import inspect


class TestRegularTrainer(TestCase):
    ''' Unit Tests for RegularTrainer Class '''
    # Test parameters
    NAME_PARAMETER = 'Tom'
    POKEMON_TEAM_PARAMETER = {'Zubat': 21, 'Ekans': 23}
    TRAINER_CLASS_PARAMETER = 'Team Rocket Grunt'
    LOCATION_PARAMETER = 'Johto'
    POKECOIN_PARAMETER = 540

    MOVEMENT_TYPE_PARAMETER = 'Walking'
    PHONE_NUM_PARAMETER = False
    HAVE_PARTNER_PARAMETER = True

    EMPTY_PARAMETER = ''
    UNDEFINED_PARAMETER = None
    TEST_INT_INPUT = 0
    TEST_STR_INPUT = 'Test'

    def setUp(self):
        '''Sets up test RegularTrainer class'''
        self.logRegularTrainer()
        self.regular_trainer = RegularTrainer(
            TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)
        self.assertIsNotNone(self.regular_trainer)

    def tearDown(self):
        '''Tears down test RegularTrainer class'''
        self.logRegularTrainer()

    def logRegularTrainer(self):
        '''Creates log info inside console'''
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_valid_init(self):
        '''Tests valid parameters for RegularTrainer constructor'''
        self.regular_trainer = RegularTrainer(
            TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)
        self.assertIsNotNone(self.regular_trainer)

    def test_invalid_parameter_init(self):
        '''Tests invalid parameters for RegularTrainer constructor'''
        # Testing movement_type parameter
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be a string',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.EMPTY_PARAMETER,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be a string',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.UNDEFINED_PARAMETER,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be a string',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.TEST_INT_INPUT,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: no match found in database',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.TEST_STR_INPUT,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)

        # Testing phone_num parameter
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be boolean',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            TestRegularTrainer.EMPTY_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be boolean',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            TestRegularTrainer.UNDEFINED_PARAMETER,
            TestRegularTrainer.HAVE_PARTNER_PARAMETER)

        # Testing have_partner parameter
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be boolean',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.EMPTY_PARAMETER)
        self.assertRaisesRegex(
            ValueError, 'Incorrect value: input should be boolean',
            RegularTrainer, TestRegularTrainer.NAME_PARAMETER,
            TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            TestRegularTrainer.LOCATION_PARAMETER,
            TestRegularTrainer.POKECOIN_PARAMETER,
            TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            TestRegularTrainer.PHONE_NUM_PARAMETER,
            TestRegularTrainer.UNDEFINED_PARAMETER)

    def test_get_type(self):
        '''Tests if get_type() returns correct value'''
        self.assertEqual('Regular Trainer', self.regular_trainer.get_type())

    def test_get_details(self):
        '''Tests if get_details() returns correct value'''
        self.assertEqual('Team Rocket Grunt Tom from Johto has 2 pokemon(s)',
                         self.regular_trainer.get_details())

    def test_get_movement_speed(self):
        '''Tests if get_movement_speed returns correct value'''
        self.assertEqual(1.0, self.regular_trainer.get_movement_speed())

    def test_have_phone_number(self):
        '''Tests if have_phone_num returns correct value'''
        self.assertEqual(False, self.regular_trainer.have_phone_number())

    def test_have_partner(self):
        '''Tests if have_partner() returns correct value'''
        self.assertEqual(True, self.regular_trainer.have_partner())

    def test_to_dict(self):
        '''Tests if to_dict() returns expected dictionary format'''
        compare_dict = {
            "id": None,
            "name": TestRegularTrainer.NAME_PARAMETER,
            "pokemon_team": TestRegularTrainer.POKEMON_TEAM_PARAMETER,
            "trainer_class": TestRegularTrainer.TRAINER_CLASS_PARAMETER,
            "pokecoins": TestRegularTrainer.POKECOIN_PARAMETER,
            "location": TestRegularTrainer.LOCATION_PARAMETER,
            "movement_type": TestRegularTrainer.MOVEMENT_TYPE_PARAMETER,
            "phone_num": TestRegularTrainer.PHONE_NUM_PARAMETER,
            "have_partner": TestRegularTrainer.HAVE_PARTNER_PARAMETER,
            "type": RegularTrainer.TRAINER_TYPE
        }
        self.assertDictEqual(compare_dict, self.regular_trainer.to_dict())


if __name__ == "__main__":
    unittest.main()
