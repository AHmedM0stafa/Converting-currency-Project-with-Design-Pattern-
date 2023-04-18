from task import Task
from task_factory import TaskFactory
from command_interface import Command

class CreateTaskCommand(Command):

    def __init__(self, task_factory: TaskFactory, title: str, description: str, category: str):
        self.task_factory = task_factory
        self.title = title
        self.description = description
        self.category = category

    def execute(self):
        new_task = self.task_factory.create_task(self.title, self.description, self.category)
        return new_task
