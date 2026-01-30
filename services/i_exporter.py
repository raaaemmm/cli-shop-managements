from abc import ABC, abstractmethod
from typing import List, Tuple

class IExporter(ABC):
    """interface for export strategies (strategy pattern)"""
    
    @abstractmethod
    def export(self, data: List, filename: str) -> Tuple[str, int]:
        """
        export data to a file
        returns: (filename, count of items exported)
        """
        pass
    
    @abstractmethod
    def get_default_extension(self) -> str:
        """get the default file extension for this exporter"""
        pass