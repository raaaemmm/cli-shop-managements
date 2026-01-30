from abc import ABC

class BaseService(ABC):
    """abstract base class for all services"""
    
    def __init__(self):
        self._observers = []
    
    def attach_observer(self, observer):
        """attach an observer (Observer pattern)"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach_observer(self, observer):
        """detach an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self, event_type: str, data=None):
        """notify all observers of an event"""
        for observer in self._observers:
            if hasattr(observer, 'update'):
                observer.update(event_type, data)
