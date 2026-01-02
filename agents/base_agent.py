from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def can_handle(self, task):
        pass

    @abstractmethod
    def handle(self, task, context):
        pass
