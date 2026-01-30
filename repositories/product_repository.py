import csv
import os
from typing import Dict, List, Optional
from .i_repository import IRepository
from models.product import Product
from config import Config

class ProductRepository(IRepository):
    """repository for Product data access with in-memory storage and CSV persistence"""
    
    def __init__(self, filename: str = None):
        self._filename = filename or Config.DEFAULT_DATA_FILE
        self._products: Dict[str, Product] = {}
        self._is_loaded = False
        self._next_id = 1  # tracking next available ID
    
    def get_next_id(self) -> str:
        """generate the next auto-increment product ID"""
        # find the highest existing ID number
        max_id = 0
        for product_id in self._products.keys():
            try:
                # extract numeric part from ID (assumes format like "1", "2"...)
                num = int(product_id)
                if num > max_id:
                    max_id = num
            except ValueError:
                # skip non-numeric IDs
                continue
        
        self._next_id = max_id + 1
        return str(self._next_id)
    
    def get_by_id(self, product_id: str) -> Optional[Product]:
        """retrieve a product by its ID"""
        return self._products.get(product_id)
    
    def get_all(self) -> List[Product]:
        """retrieve all products"""
        return list(self._products.values())
    
    def add(self, product: Product) -> bool:
        """add a new product"""
        if not isinstance(product, Product):
            raise TypeError("Entity must be a Product instance")
        
        if self.exists(product.product_id):
            raise ValueError(f"Product with ID '{product.product_id}' already exists")
        
        is_valid, errors = product.validate()
        if not is_valid:
            raise ValueError(f"Invalid product data: {', '.join(errors)}")
        
        self._products[product.product_id] = product
        return True
    
    def update(self, product: Product) -> bool:
        """update an existing product"""
        if not isinstance(product, Product):
            raise TypeError("Entity must be a Product instance")
        
        if not self.exists(product.product_id):
            raise ValueError(f"Product with ID '{product.product_id}' not found")
        
        is_valid, errors = product.validate()
        if not is_valid:
            raise ValueError(f"Invalid product data: {', '.join(errors)}")
        
        self._products[product.product_id] = product
        return True
    
    def delete(self, product_id: str) -> bool:
        """delete a product by ID"""
        if not self.exists(product_id):
            raise ValueError(f"Product with ID '{product_id}' not found")
        
        del self._products[product_id]
        return True
    
    def exists(self, product_id: str) -> bool:
        """check if a product exists"""
        return product_id in self._products
    
    def count(self) -> int:
        """get total count of products"""
        return len(self._products)
    
    def find_by_name(self, name_pattern: str) -> List[Product]:
        """find products by name pattern (case-insensitive)"""
        pattern = name_pattern.lower()
        return [p for p in self._products.values() if pattern in p.name.lower()]
    
    def find_by_category(self, category_pattern: str) -> List[Product]:
        """find products by category pattern (case-insensitive)"""
        pattern = category_pattern.lower()
        return [p for p in self._products.values() if pattern in p.category.lower()]
    
    def find_low_stock(self, threshold: int = 10) -> List[Product]:
        """find products with quantity below threshold"""
        return [p for p in self._products.values() if p.quantity < threshold]
    
    def get_by_supplier(self, supplier: str) -> List[Product]:
        """get all products from a specific supplier"""
        return [p for p in self._products.values() if p.supplier.lower() == supplier.lower()]
    
    def load(self) -> bool:
        """load products from CSV file"""
        if not os.path.exists(self._filename):
            self._is_loaded = True
            return True
        
        try:
            self._products.clear()
            with open(self._filename, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    product = Product(
                        row['product_id'],
                        row['name'],
                        row['category'],
                        row['price'],
                        row['quantity'],
                        row.get('supplier', '')
                    )
                    product.date_added = row.get('date_added', product.date_added)
                    self._products[product.product_id] = product
            
            self._is_loaded = True
            # update next_id after loading
            self.get_next_id()
            return True
        except Exception as e:
            raise Exception(f"Error loading data from {self._filename}: {str(e)}")
    
    def save(self) -> bool:
        """save products to CSV file"""
        try:
            os.makedirs(os.path.dirname(self._filename) or '.', exist_ok=True)
            
            with open(self._filename, 'w', newline='', encoding='utf-8') as f:
                if self._products:
                    writer = csv.DictWriter(f, fieldnames=Config.PRODUCT_FIELDS)
                    writer.writeheader()
                    for product in self._products.values():
                        writer.writerow(product.to_dict())
            return True
        except Exception as e:
            raise Exception(f"Error saving data to {self._filename}: {str(e)}")
    
    def clear(self):
        """clear all products from memory"""
        self._products.clear()
        self._next_id = 1
    
    @property
    def filename(self):
        return self._filename
    
    @property
    def is_loaded(self):
        return self._is_loaded