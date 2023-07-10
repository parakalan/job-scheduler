from abc import ABC, abstractmethod


class Job(ABC):
    """
    This is the parent class that all jobs will extend from.
    It contains the abstract process method that all jobs must implement.
    """
    @abstractmethod
    def process(self, **kwargs):
        pass
