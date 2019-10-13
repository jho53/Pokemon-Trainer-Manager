from unittest import TestCase
from trainer_manager import TrainerManager
import unittest
import inspect


class TestRegularTrainer(TestCase):
    ''' Unit Tests for RegularTrainer Class '''

    def setUp(self):
        '''Sets up test RegularTrainer class'''
        self.logRegularTrainer()
        pass

    def teardown(self):
        '''Tears down test RegularTrainer class'''
        self.logRegularTrainer()

    def logRegularTrainer(self):
        '''Creates log info inside console'''
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == "__main__":
    unittest.main()
