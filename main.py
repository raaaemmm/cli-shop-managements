"""
Shop Management System
Main application entry point with dependency injection
"""

from controllers.shop_controller import ShopController
from repositories.product_repository import ProductRepository
from views.console_view import ConsoleView
from config import Config

def main():
    """
    Main function to run the shop management system
    Demonstrates Dependency Injection and Inversion of Control
    """
    # initialize dependencies
    repository = ProductRepository(Config.DEFAULT_DATA_FILE)
    view = ConsoleView()
    
    # create controller with injected dependencies
    controller = ShopController(repository, view)
    
    # start the application
    controller.start()


if __name__ == "__main__":
    main()