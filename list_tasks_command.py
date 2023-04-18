from typing import List
from task import Task
from command_interface import Command

class ListTasksCommand(Command):

    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def execute(self) -> List[Task]:
        return self.tasks
