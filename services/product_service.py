from typing import List, Dict, Optional, Tuple
from models.product import Product
from repositories.product_repository import ProductRepository
from .base_service import BaseService

class ProductService(BaseService):
    """service layer for product business logic"""
    
    def __init__(self, repository: ProductRepository):
        super().__init__()
        self._repository = repository
    
    def create_product(self, product_id: str, name: str, category: str, price: float, quantity: int, supplier: str = "") -> Product:
        """create a new product"""
        try:
            product = Product(product_id, name, category, price, quantity, supplier)
            self._repository.add(product)
            self.notify_observers('product_created', product)
            return product
        except Exception as e:
            raise Exception(f"Failed to create product: {str(e)}")
    
    def create_product_auto_id(self, name: str, category: str, price: float, quantity: int, supplier: str = "") -> Product:
        """create a new product with auto-generated ID"""
        try:
            
            # get the next available ID from repository
            product_id = self._repository.get_next_id()
            product = Product(product_id, name, category, price, quantity, supplier)
            self._repository.add(product)
            self.notify_observers('product_created', product)
            return product
        except Exception as e:
            raise Exception(f"Failed to create product: {str(e)}")
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """get a product by ID"""
        return self._repository.get_by_id(product_id)
    
    def get_all_products(self) -> List[Product]:
        """get all products"""
        return self._repository.get_all()
    
    def update_product(self, product_id: str, update_data: Dict) -> Product:
        """update a product"""
        product = self._repository.get_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID '{product_id}' not found")
        
        try:
            product.update_from_dict(update_data)
            self._repository.update(product)
            self.notify_observers('product_updated', product)
            return product
        except Exception as e:
            raise Exception(f"Failed to update product: {str(e)}")
    
    def delete_product(self, product_id: str) -> bool:
        """delete a product"""
        try:
            product = self._repository.get_by_id(product_id)
            self._repository.delete(product_id)
            self.notify_observers('product_deleted', product)
            return True
        except Exception as e:
            raise Exception(f"Failed to delete product: {str(e)}")
    
    def search_by_id(self, search_term: str) -> List[Product]:
        """search products by ID pattern"""
        search_lower = search_term.lower()
        return [p for p in self._repository.get_all() 
                if search_lower in p.product_id.lower()]
    
    def search_by_name(self, name_pattern: str) -> List[Product]:
        """search products by name"""
        return self._repository.find_by_name(name_pattern)
    
    def search_by_category(self, category_pattern: str) -> List[Product]:
        """search products by category"""
        return self._repository.find_by_category(category_pattern)
    
    def get_statistics(self) -> Dict:
        """get inventory statistics"""
        products = self._repository.get_all()
        
        if not products:
            return {
                'total_products': 0,
                'total_quantity': 0,
                'total_value': 0.0,
                'categories': {},
                'low_stock_count': 0
            }
        
        total_quantity = sum(p.quantity for p in products)
        total_value = sum(p.get_total_value() for p in products)
        
        categories = {}
        for product in products:
            if product.category not in categories:
                categories[product.category] = 0
            categories[product.category] += 1
        
        low_stock = self._repository.find_low_stock()
        
        return {
            'total_products': len(products),
            'total_quantity': total_quantity,
            'total_value': total_value,
            'categories': categories,
            'low_stock_count': len(low_stock),
            'low_stock_products': low_stock
        }
    
    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """get products with low stock"""
        return self._repository.find_low_stock(threshold)
    
    def adjust_stock(self, product_id: str, amount: int) -> Product:
        """adjust product stock by amount"""
        product = self._repository.get_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID '{product_id}' not found")
        
        try:
            product.adjust_quantity(amount)
            self._repository.update(product)
            self.notify_observers('stock_adjusted', {'product': product, 'amount': amount})
            return product
        except Exception as e:
            raise Exception(f"Failed to adjust stock: {str(e)}")
    
    def product_exists(self, product_id: str) -> bool:
        """check if a product exists"""
        return self._repository.exists(product_id)
    
    def get_total_count(self) -> int:
        """get total product count"""
        return self._repository.count()