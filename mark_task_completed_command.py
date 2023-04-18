from command import Command

class MarkTaskCompletedCommand(Command):
    def __init__(self, task):
        self.task = task

    def execute(self):
        self.task.completed = True
