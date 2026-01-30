from datetime import datetime
from .base_model import BaseModel

class Product(BaseModel):
    """product class representing a shop item with proper encapsulation"""
    
    def __init__(self, product_id, name, category, price, quantity, supplier=""):
        super().__init__()
        self._product_id = product_id
        self._name = name
        self._category = category
        self._price = float(price)
        self._quantity = int(quantity)
        self._supplier = supplier
        self._date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # property decorators for encapsulation
    @property
    def product_id(self):
        return self._product_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Product name cannot be empty")
        if len(value) > 50:
            raise ValueError("Product name too long (max 50 characters)")
        self._name = value
        self.update_timestamp()
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        self._category = value
        self.update_timestamp()
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        price_val = float(value)
        if price_val < 0:
            raise ValueError("Price cannot be negative")
        self._price = price_val
        self.update_timestamp()
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        qty_val = int(value)
        if qty_val < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = qty_val
        self.update_timestamp()
    
    @property
    def supplier(self):
        return self._supplier
    
    @supplier.setter
    def supplier(self, value):
        self._supplier = value
        self.update_timestamp()
    
    @property
    def date_added(self):
        return self._date_added
    
    @date_added.setter
    def date_added(self, value):
        self._date_added = value
    
    def validate(self):
        """validate product data"""
        errors = []
        
        if not self._product_id or not self._product_id.strip():
            errors.append("Product ID cannot be empty")
        if len(self._product_id) > 20:
            errors.append("Product ID too long (max 20 characters)")
        
        if not self._name or not self._name.strip():
            errors.append("Product name cannot be empty")
        if len(self._name) > 50:
            errors.append("Product name too long (max 50 characters)")
        
        if self._price < 0:
            errors.append("Price cannot be negative")
        
        if self._quantity < 0:
            errors.append("Quantity cannot be negative")
        
        return len(errors) == 0, errors
    
    def to_dict(self):
        """convert product to dictionary"""
        return {
            'product_id': self._product_id,
            'name': self._name,
            'category': self._category,
            'price': self._price,
            'quantity': self._quantity,
            'supplier': self._supplier,
            'date_added': self._date_added
        }
    
    def update_from_dict(self, data):
        """update product attributes from dictionary"""
        if 'name' in data and data['name']:
            self.name = data['name']
        if 'category' in data and data['category']:
            self.category = data['category']
        if 'price' in data and data['price'] is not None:
            self.price = float(data['price'])
        if 'quantity' in data and data['quantity'] is not None:
            self.quantity = int(data['quantity'])
        if 'supplier' in data and data['supplier']:
            self.supplier = data['supplier']
    
    def get_total_value(self):
        """calculate total value of product stock"""
        return self._price * self._quantity
    
    def is_low_stock(self, threshold=10):
        """check if product is low in stock"""
        return self._quantity < threshold
    
    def adjust_quantity(self, amount):
        """adjust quantity by a given amount (positive or negative)"""
        new_quantity = self._quantity + amount
        if new_quantity < 0:
            raise ValueError("Insufficient quantity")
        self.quantity = new_quantity
    
    def __str__(self):
        return f"ID: {self._product_id} | {self._name} | {self._category} | ${self._price:.2f} | Qty: {self._quantity} | Supplier: {self._supplier}"
    
    def __repr__(self):
        return f"Product({self._product_id}, {self._name}, {self._quantity})"
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self._product_id == other._product_id
    
    def __hash__(self):
        return hash(self._product_id)