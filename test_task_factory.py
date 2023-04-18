import unittest
from task import Task
from task_factory import TaskFactory

class TaskFactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = TaskFactory()
        self.title = 'My Title'
        self.description = 'My Description'
        self.category = 'My Category'

    def test_task_creation(self):
        task = self.factory.create_task(self.title, self.description, self.category)
        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, self.title)
        self.assertEqual(task.description, self.description)
        self.assertEqual(task.category, self.category)
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main()
