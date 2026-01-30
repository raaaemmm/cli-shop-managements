from abc import ABC, abstractmethod
from datetime import datetime

class BaseModel(ABC):
    """abstract base class for all models"""
    
    def __init__(self):
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
    
    @abstractmethod
    def to_dict(self):
        """convert model to dictionary - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def validate(self):
        """validate model data - must be implemented by subclasses"""
        pass
    
    def update_timestamp(self):
        """update the last modified timestamp"""
        self._updated_at = datetime.now()
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at