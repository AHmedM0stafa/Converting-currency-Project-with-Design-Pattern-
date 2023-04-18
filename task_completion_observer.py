from observer import Observer

class TaskCompletionObserver(Observer):
    def update(self, task):
        print(f'Task {task.description} is complete!')
