"""
Exercise 2: Data Exporter
File: 14_data_exporter.py

Rules:
1. Import the necessary tools from 'abc'.
2. Create an abstract class 'DataExporter(ABC)'.
3. Create two abstract methods:
   - 'export(self, data: str) -> str'
   - 'get_extension(self) -> str'
4. Create a concrete class 'JSONExporter'.
   - 'export' should return: "Exporting data to JSON format: [data]"
   - 'get_extension' should return: ".json"
5. Create a concrete class 'CSVExporter'.
   - 'export' should return: "Exporting data to CSV format: [data]"
   - 'get_extension' should return: ".csv"
6. Create instances for both exporters.
7. Print the result of both methods for each instance to prove the contract is fulfilled.
"""

from abc import ABC, abstractmethod

class DataExporter(ABC):

    @abstractmethod
    def export(self, data: str) -> str:
        pass

    @abstractmethod
    def get_extension(self) -> str:
        pass

class JSONExporter(DataExporter):

    def export(self, data):
        return f"Exporting data to JSON format: {data}"
    
    def get_extension(self):
        return ".json"

class CSVExporter(DataExporter):

    def export(self, data):
        return f"Exporting data to CSV format: {data}"
    
    def get_extension(self):
        return ".csv"
    
obj1 = JSONExporter()
obj2 = CSVExporter()
print(f"{obj1.export("Teste")}\n{obj1.get_extension()}")
print(f"{obj2.export("Teste")}\n{obj2.get_extension()}")