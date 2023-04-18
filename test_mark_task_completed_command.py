import unittest
from task_factory import TaskFactory
from mark_task_completed_command import MarkTaskCompletedCommand

class MarkTaskCompletedCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.task_factory = TaskFactory()
        self.task = self.task_factory.create_task(title='My Title', description='My Description', category='My Category')
        self.command = MarkTaskCompletedCommand(self.task)

    def test_mark_task_completed_command(self):
        self.assertFalse(self.task.completed)
        result = self.command.execute()
        self.assertTrue(self.task.completed)

if __name__ == '__main__':
    unittest.main()
