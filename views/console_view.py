import os
from typing import List
from config import Config
from models.product import Product

class ConsoleView:
    """view class for console-based UI (separation of concerns)"""
    
    def __init__(self):
        self._table_width = Config.TABLE_WIDTH
        self._separator = Config.SEPARATOR_CHAR
        self._line = Config.LINE_CHAR
    
    def clear_screen(self):
        """clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self, title: str, width: int = 60):
        """display a formatted header"""
        print(f"\n{self._separator * width}")
        print(title.center(width))
        print(f"{self._separator * width}")
    
    def display_separator(self, width: int = None):
        """display a line separator"""
        width = width or self._table_width
        print(self._line * width)
    
    def display_success(self, message: str):
        """display success message"""
        print(f"✓ {message}")
    
    def display_error(self, message: str):
        """display error message"""
        print(f"✗ {message}")
    
    def display_info(self, message: str):
        """display info message"""
        print(f"ℹ {message}")
    
    def display_warning(self, message: str):
        """display warning message"""
        print(f"⚠ {message}")
    
    def display_menu(self):
        """display the main menu"""
        self.display_header("SHOP MANAGEMENT SYSTEM")
        options = [
            "1. Add Product",
            "2. View All Products",
            "3. Update Product",
            "4. Delete Product",
            "5. Search Products",
            "6. View Statistics",
            "7. Save Data",
            "8. Export to JSON",
            "9. Export to CSV",
            "10. Clear Screen",
            "11. Exit"
        ]
        for option in options:
            print(option)
        print(f"{self._separator * 60}")
    
    def display_products_table(self, products: List[Product]):
        """display products in a formatted table"""
        if not products:
            self.display_info("No products found.")
            return
        
        print(f"\nTotal Products: {len(products)}\n")
        self.display_separator()
        
        # header
        header = f"{'ID':<10} {'Name':<20} {'Category':<15} {'Price':<10} {'Qty':<8} {'Supplier':<20} {'Date Added':<20}"
        print(header)
        self.display_separator()
        
        # rows
        for product in products:
            row = (f"{product.product_id:<10} {product.name:<20} {product.category:<15} "
                   f"${product.price:<9.2f} {product.quantity:<8} "
                   f"{product.supplier:<20} {product.date_added:<20}")
            print(row)
        
        self.display_separator()
    
    def display_statistics(self, stats: dict):
        """display inventory statistics"""
        self.display_header("INVENTORY STATISTICS")
        
        if stats['total_products'] == 0:
            self.display_info("No products available for statistics.")
            return
        
        print(f"\nTotal Products: {stats['total_products']}")
        print(f"Total Items in Stock: {stats['total_quantity']}")
        print(f"Total Inventory Value: ${stats['total_value']:,.2f}")
        
        print(f"\nProducts by Category:")
        for category, count in sorted(stats['categories'].items()):
            print(f"  {category}: {count}")
        
        if stats['low_stock_count'] > 0:
            print(f"\n⚠ Low Stock Alert ({stats['low_stock_count']} products):")
            for product in stats.get('low_stock_products', []):
                print(f"  {product.product_id} - {product.name}: {product.quantity} units")
    
    def get_input(self, prompt: str, default: str = None) -> str:
        """get user input with optional default value"""
        if default:
            full_prompt = f"{prompt} [{default}]: "
        else:
            full_prompt = f"{prompt}: "
        
        value = input(full_prompt).strip()
        return value if value else (default if default is not None else "")
    
    def get_confirmation(self, message: str) -> bool:
        """get yes/no confirmation from user"""
        response = input(f"\n{message} (yes/no): ").strip().lower()
        return response in ['yes', 'y']
    
    def wait_for_enter(self):
        """Wait for user to press enter"""
        input("\nPress Enter to continue...")
    
    def display_product_details(self, product: Product):
        """display detailed information about a product"""
        print(f"\nProduct Details:")
        print(f"  ID: {product.product_id}")
        print(f"  Name: {product.name}")
        print(f"  Category: {product.category}")
        print(f"  Price: ${product.price:.2f}")
        print(f"  Quantity: {product.quantity}")
        print(f"  Supplier: {product.supplier}")
        print(f"  Date Added: {product.date_added}")
        print(f"  Total Value: ${product.get_total_value():.2f}")