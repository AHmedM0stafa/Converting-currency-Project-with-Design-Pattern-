# Observer Design Pattern
class Observer:
    def update(self):
        pass

class Subject:
    def __init__(self):
        self._observers = set()

    def register(self, observer: Observer) -> None:
        self._observers.add(observer)

    def unregister(self, observer: Observer) -> None:
        self._observers.discard(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()
