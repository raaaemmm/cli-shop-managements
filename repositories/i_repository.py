from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class IRepository(ABC):
    """interface for repository pattern - defines contract for data access"""
    
    @abstractmethod
    def get_by_id(self, entity_id: str):
        """retrieve an entity by its ID"""
        pass
    
    @abstractmethod
    def get_all(self) -> List:
        """retrieve all entities"""
        pass
    
    @abstractmethod
    def add(self, entity) -> bool:
        """add a new entity"""
        pass
    
    @abstractmethod
    def update(self, entity) -> bool:
        """update an existing entity"""
        pass
    
    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        """delete an entity by ID"""
        pass
    
    @abstractmethod
    def exists(self, entity_id: str) -> bool:
        """check if an entity exists"""
        pass
    
    @abstractmethod
    def count(self) -> int:
        """get total count of entities"""
        pass
    
    @abstractmethod
    def save(self) -> bool:
        """persist all changes"""
        pass
    
    @abstractmethod
    def load(self) -> bool:
        """load data from storage"""
        pass