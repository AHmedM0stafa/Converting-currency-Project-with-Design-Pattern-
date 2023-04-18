import unittest
from task_list import TaskList
from task_factory import TaskFactory

class TaskListTestCase(unittest.TestCase):
    def setUp(self):
        self.task_factory = TaskFactory()
        self.task = self.task_factory.create_task(title='My Title', description='My Description', category='My Category')
        self.task_list = TaskList()

    def test_add_task(self):
        self.task_list.add_task(self.task)
        self.assertIn(self.task, self.task_list.tasks)

    def test_remove_task(self):
        self.task_list.add_task(self.task)
        self.task_list.remove_task(self.task)
        self.assertNotIn(self.task, self.task_list.tasks)

    def test_mark_task_completed(self):
        self.task_list.add_task(self.task)
        self.task_list.mark_task_completed(self.task)
        self.assertTrue(self.task.completed)
        self.assertFalse(self.task.started)

    def test_mark_task_not_started(self):
        self.task_list.add_task(self.task)
        self.task_list.mark_task_not_started(self.task)
        self.assertFalse(self.task.completed)
        self.assertFalse(self.task.started)

    def test_mark_task_in_progress(self):
        self.task_list.add_task(self.task)
        self.task_list.mark_task_in_progress(self.task)
        self.assertFalse(self.task.completed)
        self.assertTrue(self.task.started)

if __name__ == '__main__':
    unittest.main()
