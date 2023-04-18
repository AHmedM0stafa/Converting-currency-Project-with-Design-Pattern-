import unittest
from task import Task

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        self.title = 'My Title'
        self.description = 'My Description'
        self.category = 'My Category'
        self.task = Task(self.title, self.description, self.category)

    def test_task_creation(self):
        self.assertEqual(self.task.title, self.title)
        self.assertEqual(self.task.description, self.description)
        self.assertEqual(self.task.category, self.category)
        self.assertFalse(self.task.completed)

    def test_task_str(self):
        expected_str = f'Title: {self.title}\nDescription: {self.description}\nCategory: {self.category}\nCompleted: False'
        self.assertEqual(str(self.task), expected_str)

if __name__ == '__main__':
    unittest.main()
