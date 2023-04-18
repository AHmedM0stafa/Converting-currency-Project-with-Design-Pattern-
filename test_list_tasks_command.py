import unittest
from task import Task
from list_tasks_command import ListTasksCommand

class ListTasksCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task('Task 1', 'Description 1', 'Category 1'),
            Task('Task 2', 'Description 2', 'Category 2'),
            Task('Task 3', 'Description 3', 'Category 3'),
        ]
        self.command = ListTasksCommand(self.tasks)

    def test_list_tasks_command(self):
        result = self.command.execute()
        self.assertEqual(result, self.tasks)

if __name__ == '__main__':
    unittest.main()
