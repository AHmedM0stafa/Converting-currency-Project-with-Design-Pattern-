class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_completed(self, task):
        task.completed = True

    def mark_task_not_started(self, task):
        task.completed = False
        task.started = False

    def mark_task_in_progress(self, task):
        command = MarkTaskInProgressCommand(task)
        command.execute()
