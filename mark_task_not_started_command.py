from command import Command

class MarkTaskNotStartedCommand(Command):
    def __init__(self, task):
        self.task = task

    def execute(self):
        self.task.completed = False
        self.task.started = False
