from typing import Optional
from services.product_service import ProductService
from services.export_service import ExportService, JsonExporter, CsvExporter
from views.console_view import ConsoleView
from utils.input_validator import InputValidator
from repositories.product_repository import ProductRepository

class ShopController:
    """
    main controller for shop management operation flows
    MVC pattern - coordinates between Model, View, and Services
    """
    
    def __init__(self, repository: ProductRepository, view: ConsoleView):
        self._repository = repository
        self._view = view
        self._product_service = ProductService(repository)
        self._validator = InputValidator()
        self._running = True
    
    def start(self):
        """start the application"""
        self._view.display_header("WELCOME TO SHOP MANAGEMENT SYSTEM")
        self._load_initial_data()
        self._run_main_loop()
    
    def _load_initial_data(self):
        """load initial data from storage"""
        try:
            self._repository.load()
            count = self._repository.count()
            self._view.display_success(f"Loaded {count} products from {self._repository.filename}")
        except Exception as e:
            self._view.display_error(str(e))
            self._view.display_info("Starting with empty inventory.")
    
    def _run_main_loop(self):
        """main application loop"""
        while self._running:
            self._view.display_menu()
            choice = self._view.get_input("\nEnter your choice (1-11)")
            
            is_valid, error = self._validator.validate_menu_choice(choice, 1, 11)
            
            if not is_valid:
                self._view.display_error(error)
                self._view.wait_for_enter()
                continue
            
            self._handle_menu_choice(int(choice))
            
            if self._running:
                self._view.wait_for_enter()
    
    def _handle_menu_choice(self, choice: int):
        """handle menu selection"""
        menu_actions = {
            1: self.add_product,
            2: self.view_all_products,
            3: self.update_product,
            4: self.delete_product,
            5: self.search_products,
            6: self.view_statistics,
            7: self.save_data,
            8: self.export_to_json,
            9: self.export_to_csv,
            10: self.clear_screen,
            11: self.exit_application
        }
        
        action = menu_actions.get(choice)
        if action:
            action()
    
    def add_product(self):
        """add a new product with auto-generated ID"""
        self._view.display_header("ADD NEW PRODUCT")
        
        try:
            # # get next auto-generated product ID
            # next_id = self._repository.get_next_id()
            # self._view.display_info(f"Auto-generated Product ID: {next_id}")
            
            # get and validate name
            name = self._view.get_input("Product Name")
            is_valid, error = self._validator.validate_name(name)
            if not is_valid:
                self._view.display_error(error)
                return
            
            # get category
            category = self._view.get_input("Category")
            
            # get and validate price
            price_str = self._view.get_input("Price ($)")
            is_valid, error, price = self._validator.validate_price(price_str)
            if not is_valid:
                self._view.display_error(error)
                return
            
            # get and validate quantity
            quantity_str = self._view.get_input("Quantity")
            is_valid, error, quantity = self._validator.validate_quantity(quantity_str)
            if not is_valid:
                self._view.display_error(error)
                return
            
            # get supplier
            supplier = self._view.get_input("Supplier (optional)", "")
            
            # create product with auto-generated ID
            product = self._product_service.create_product_auto_id(
                name, category, price, quantity, supplier
            )
            
            self._view.display_success(f"Product '{name}' added successfully with ID: {product.product_id}!")
            
            # auto-save after adding product
            try:
                self._repository.save()
                self._view.display_success("Data automatically saved!")
            except Exception as save_error:
                self._view.display_warning(f"Product added but auto-save failed: {str(save_error)}")
            
        except Exception as e:
            self._view.display_error(f"Error adding product: {str(e)}")
    
    def view_all_products(self):
        """view all products"""
        self._view.display_header("ALL PRODUCTS")
        products = self._product_service.get_all_products()
        self._view.display_products_table(products)
    
    def update_product(self):
        """update an existing product"""
        self._view.display_header("UPDATE PRODUCT")
        
        if self._product_service.get_total_count() == 0:
            self._view.display_info("No products available to update.")
            return
        
        product_id = self._view.get_input("Enter Product ID to update")
        product = self._product_service.get_product(product_id)
        
        if not product:
            self._view.display_error(f"Product ID '{product_id}' not found!")
            return
        
        self._view.display_product_details(product)
        print("\nEnter new values (press Enter to keep current value):")
        
        try:
            update_data = {}
            
            # name
            name = self._view.get_input("Name", product.name)
            if name and name != product.name:
                is_valid, error = self._validator.validate_name(name)
                if is_valid:
                    update_data['name'] = name
                else:
                    self._view.display_error(error + " Keeping old value.")
            
            # category
            category = self._view.get_input("Category", product.category)
            if category and category != product.category:
                update_data['category'] = category
            
            # price
            price_str = self._view.get_input("Price", str(product.price))
            if price_str and price_str != str(product.price):
                is_valid, error, price = self._validator.validate_price(price_str)
                if is_valid:
                    update_data['price'] = price
                else:
                    self._view.display_error(error + " Keeping old value.")
            
            # quantity
            quantity_str = self._view.get_input("Quantity", str(product.quantity))
            if quantity_str and quantity_str != str(product.quantity):
                is_valid, error, quantity = self._validator.validate_quantity(quantity_str)
                if is_valid:
                    update_data['quantity'] = quantity
                else:
                    self._view.display_error(error + " Keeping old value.")
            
            # supplier
            supplier = self._view.get_input("Supplier", product.supplier)
            if supplier and supplier != product.supplier:
                update_data['supplier'] = supplier
            
            if update_data:
                updated_product = self._product_service.update_product(product_id, update_data)
                self._view.display_success(f"Product '{updated_product.name}' updated successfully!")
                
                # auto-save after updating product
                try:
                    self._repository.save()
                    self._view.display_success("Data automatically saved!")
                except Exception as save_error:
                    self._view.display_warning(f"Product updated but auto-save failed: {str(save_error)}")
            else:
                self._view.display_info("No changes made.")
            
        except Exception as e:
            self._view.display_error(f"Error updating product: {str(e)}")
    
    def delete_product(self):
        """delete a product"""
        self._view.display_header("DELETE PRODUCT")
        
        if self._product_service.get_total_count() == 0:
            self._view.display_info("No products available to delete.")
            return
        
        product_id = self._view.get_input("Enter Product ID to delete")
        product = self._product_service.get_product(product_id)
        
        if not product:
            self._view.display_error(f"Product ID '{product_id}' not found!")
            return
        
        self._view.display_product_details(product)
        
        if self._view.get_confirmation("Are you sure you want to delete this product?"):
            try:
                self._product_service.delete_product(product_id)
                self._view.display_success("Product deleted successfully!")
                
                # auto-save after deleting product
                try:
                    self._repository.save()
                    self._view.display_success("Data automatically saved!")
                except Exception as save_error:
                    self._view.display_warning(f"Product deleted but auto-save failed: {str(save_error)}")
            except Exception as e:
                self._view.display_error(f"Error deleting product: {str(e)}")
        else:
            self._view.display_info("Deletion cancelled.")
    
    def search_products(self):
        """search products by various criteria"""
        self._view.display_header("SEARCH PRODUCTS")
        
        if self._product_service.get_total_count() == 0:
            self._view.display_info("No products available to search.")
            return
        
        print("Search by:")
        print("1. Product ID")
        print("2. Name")
        print("3. Category")
        
        choice = self._view.get_input("\nEnter choice (1-3)")
        search_term = self._view.get_input("Enter search term")
        
        results = []
        
        try:
            if choice == '1':
                results = self._product_service.search_by_id(search_term)
            elif choice == '2':
                results = self._product_service.search_by_name(search_term)
            elif choice == '3':
                results = self._product_service.search_by_category(search_term)
            else:
                self._view.display_error("Invalid choice!")
                return
            
            if results:
                self._view.display_products_table(results)
            else:
                self._view.display_info("No products found matching your search.")
        except Exception as e:
            self._view.display_error(f"Error searching: {str(e)}")
    
    def view_statistics(self):
        """view inventory statistics"""
        try:
            stats = self._product_service.get_statistics()
            self._view.display_statistics(stats)
        except Exception as e:
            self._view.display_error(f"Error getting statistics: {str(e)}")
    
    def save_data(self):
        """save products to file"""
        self._view.display_header("SAVE DATA")
        try:
            self._repository.save()
            self._view.display_success(f"Data saved successfully to {self._repository.filename}")
        except Exception as e:
            self._view.display_error(f"Error saving data: {str(e)}")
    
    def export_to_json(self):
        """export data to JSON"""
        self._view.display_header("EXPORT TO JSON")
        
        if self._product_service.get_total_count() == 0:
            self._view.display_info("No products to export.")
            return
        
        filename = self._view.get_input("Enter JSON filename (default: shop_export.json)", None)
        
        try:
            export_service = ExportService.create_json_exporter()
            products = self._product_service.get_all_products()
            filename, count = export_service.export(products, filename)
            self._view.display_success(f"Exported {count} products to {filename}")
        except Exception as e:
            self._view.display_error(f"Error exporting to JSON: {str(e)}")
    
    def export_to_csv(self):
        """export data to CSV"""
        self._view.display_header("EXPORT TO CSV")
        
        if self._product_service.get_total_count() == 0:
            self._view.display_info("No products to export.")
            return
        
        filename = self._view.get_input("Enter CSV filename (default: shop_export.csv)", None)
        
        try:
            export_service = ExportService.create_csv_exporter()
            products = self._product_service.get_all_products()
            filename, count = export_service.export(products, filename)
            self._view.display_success(f"Exported {count} products to {filename}")
        except Exception as e:
            self._view.display_error(f"Error exporting to CSV: {str(e)}")
    
    def clear_screen(self):
        """clear the screen"""
        self._view.clear_screen()
        self._view.display_success("Screen cleared!")
    
    def exit_application(self):
        """exit the application"""
        self._view.display_header("EXIT")
        
        print("\nThank you for using Shop Management System!")
        print("Goodbye!")
        print("=" * 60 + "\n")
        self._running = False