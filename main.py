from task import Task
from task_completion_observer import TaskCompletionObserver

if __name__ == '__main__':
    task = Task('Implement Observer Pattern')
    task_observers = [TaskCompletionObserver() for _ in range(3)]
    for observer in task_observers:
        task.register(observer)

    task.complete()
    for observer in task_observers:
        observer.display_completion_message()
