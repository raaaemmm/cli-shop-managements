from typing import Tuple

class InputValidator:
    """utility helper class for input validation"""
    
    @staticmethod
    def validate_product_id(product_id: str) -> Tuple[bool, str]:
        """validate product ID format"""
        if not product_id or not product_id.strip():
            return False, "Product ID cannot be empty!"
        if len(product_id) > 20:
            return False, "Product ID too long (max 20 characters)!"
        return True, ""
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """validate product name"""
        if not name or not name.strip():
            return False, "Product name cannot be empty!"
        if len(name) > 50:
            return False, "Product name too long (max 50 characters)!"
        return True, ""
    
    @staticmethod
    def validate_price(price_str: str) -> Tuple[bool, str, float]:
        """validate and convert price"""
        try:
            price = float(price_str)
            if price < 0:
                return False, "Price cannot be negative!", None
            return True, "", price
        except ValueError:
            return False, "Invalid price format! Please enter a number.", None
    
    @staticmethod
    def validate_quantity(quantity_str: str) -> Tuple[bool, str, int]:
        """validate and convert quantity"""
        try:
            quantity = int(quantity_str)
            if quantity < 0:
                return False, "Quantity cannot be negative!", None
            return True, "", quantity
        except ValueError:
            return False, "Invalid quantity format! Please enter a whole number.", None
    
    @staticmethod
    def validate_menu_choice(choice: str, min_val: int, max_val: int) -> Tuple[bool, str]:
        """validate menu choice"""
        if not choice or not choice.strip():
            return False, "Please enter a choice."
        
        try:
            choice_int = int(choice)
            if min_val <= choice_int <= max_val:
                return True, ""
            return False, f"Please enter a number between {min_val} and {max_val}."
        except ValueError:
            return False, "Invalid input! Please enter a number."
    
    @staticmethod
    def validate_non_empty(value: str, field_name: str = "Field") -> Tuple[bool, str]:
        """validate that a value is not empty"""
        if not value or not value.strip():
            return False, f"{field_name} cannot be empty!"
        return True, ""