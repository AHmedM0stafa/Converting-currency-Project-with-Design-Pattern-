from dataclasses import dataclass
from typing import Optional

class Task:
    def __init__(self, title: str, description: Optional[str]=None, category: Optional[str]=None, completed: bool=False, started: bool=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
        self.started = started

    @classmethod
    def from_builder(cls, builder):
        return cls(
            title=builder.title,
            description=builder.description,
            category=builder.category,
            completed=builder.completed,
            started=builder.started
        )

    def __repr__(self):
        return f'<Task title={self.title}>'


from observer import Subject

class Task(Subject):
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.observers = set()

    def __str__(self):
        return f'{self.description}, completed: {self.completed}'
    
    def complete(self):
        self.completed = True
        self.notify()
    
    def register(self, observer):
        self.observers.add(observer)
    
    def unregister(self, observer):
        self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self)
