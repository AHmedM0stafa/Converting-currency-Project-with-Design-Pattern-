import unittest
from task_factory import TaskFactory
from mark_task_in_progress_command import MarkTaskInProgressCommand

class MarkTaskInProgressCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.task_factory = TaskFactory()
        self.task = self.task_factory.create_task(title='My Title', description='My Description', category='My Category')
        self.command = MarkTaskInProgressCommand(self.task)

    def test_mark_task_in_progress_command(self):
        self.assertFalse(self.task.completed)
        self.assertFalse(self.task.started)
        result = self.command.execute()
        self.assertFalse(self.task.completed)
        self.assertTrue(self.task.started)

if __name__ == '__main__':
    unittest.main()
