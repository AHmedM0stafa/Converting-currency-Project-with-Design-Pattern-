class TaskBuilder:
    def __init__(self, title=None, description=None, category=None, completed=False, started=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed
        self.started = started

    def with_title(self, title):
        self.title = title
        return self

    def with_description(self, description):
        self.description = description
        return self

    def with_category(self, category):
        self.category = category
        return self

    def with_completed(self, completed):
        self.completed = completed
        return self

    def with_started(self, started):
        self.started = started
        return self

    def build(self):
        return Task(self.title, self.description, self.category, self.completed, self.started)
