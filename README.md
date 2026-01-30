# CLI Shop Management System

A console-based (CLI) inventory management system built with Python, demonstrating Object-Oriented Programming principles and design patterns.

**Final Project - Object-Oriented Programming Course**

## 📋 Overview

This is my final project demonstrating the application of OOP concepts, SOLID principles, and design patterns in a real-world inventory management system. The project showcases clean code architecture and professional software development practices.

## ✨ Features

- Add, view, update, and delete products
- Search products by ID, name, or category
- View inventory statistics
- Export data to JSON or CSV
- Automatic data saving to CSV file
- Input validation
- Low stock alerts

## 🏗️ Design Patterns Used

This project demonstrates several important design patterns:

1. **MVC (Model-View-Controller)**
   - Models: `Product` class (data)
   - Views: `ConsoleView` class (display)
   - Controllers: `ShopController` class (logic)

2. **Repository Pattern**
   - `ProductRepository` separates data access from business logic

3. **Service Layer**
   - `ProductService` contains business logic
   - `ExportService` handles exports

4. **Strategy Pattern**
   - Different export strategies (JSON, CSV)

5. **Dependency Injection**
   - Classes receive their dependencies through constructors

### SOLID Principles

- **Single Responsibility**: Each class has one job
- **Open/Closed**: Can add new features without changing existing code
- **Liskov Substitution**: Interfaces can be swapped
- **Interface Segregation**: Small, focused interfaces
- **Dependency Inversion**: Depend on abstractions, not concrete classes


## 📁 Project Structure

```
shop-management-system/
│
├── main.py                      # Application entry point
├── config.py                    # Configuration settings
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
│
├── models/                      # Domain models (Entity layer)
│   ├── __init__.py
│   ├── base_model.py           # Abstract base model
│   └── product.py              # Product entity with validation
│
├── repositories/                # Data access layer (Repository pattern)
│   ├── __init__.py
│   ├── i_repository.py         # Repository interface
│   └── product_repository.py   # CSV data persistence
│
├── services/                    # Business logic layer (Service pattern)
│   ├── __init__.py
│   ├── base_service.py         # Base service with observer
│   ├── product_service.py      # Product business logic
│   ├── i_exporter.py           # Exporter interface
│   └── export_service.py       # Export strategies (JSON/CSV)
│
├── controllers/                 # Application controllers (MVC)
│   ├── __init__.py
│   └── shop_controller.py      # Main controller coordinating flow
│
├── views/                       # Presentation layer (MVC)
│   ├── __init__.py
│   └── console_view.py         # Console UI
│
├── utils/                       # Utility helpers
│   ├── __init__.py
│   └── input_validator.py      # Input validation
│
└── data/                        # Data storage (auto-created)
    ├── shop_data.csv           # Persistent storage
    ├── shop_export.json        # JSON exports
    └── shop_export.csv         # CSV exports
```

## 📦 Requirements

- Python 3.7 or higher
- No external libraries needed (uses Python standard library)

## 🚀 Installation & Running

1. Make sure Python is installed:
```bash
python --version
```

2. Organize files in this structure:
```
shop-management-system/
├── main.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   └── product.py
├── repositories/
│   ├── __init__.py
│   ├── i_repository.py
│   └── product_repository.py
├── services/
│   ├── __init__.py
│   ├── base_service.py
│   ├── product_service.py
│   ├── i_exporter.py
│   └── export_service.py
├── controllers/
│   ├── __init__.py
│   └── shop_controller.py
├── views/
│   ├── __init__.py
│   └── console_view.py
└── utils/
    ├── __init__.py
    └── input_validator.py
```

3. Run the program:
```bash
python main.py
```

## 💻 How to Use

The program shows a menu with these options:

1. **Add Product** - Create a new product (ID auto-generated)
2. **View All Products** - See all products in a table
3. **Update Product** - Change product information
4. **Delete Product** - Remove a product
5. **Search Products** - Find products by ID, name, or category
6. **View Statistics** - See inventory summary
7. **Save Data** - Manually save to CSV
8. **Export to JSON** - Export all data as JSON
9. **Export to CSV** - Export all data as CSV
10. **Clear Screen** - Clear the display
11. **Exit** - Close the program

### Example Usage

```
# Run the program
python main.py

# Add a product
Choose option 1
Enter: Laptop, Electronics, 999.99, 10, TechSupply

# View all products
Choose option 2

# Search for products
Choose option 5
Search by name: "Laptop"

# Exit
Choose option 11
```

## 🎯 Project Objectives

This final project was developed to demonstrate:

1. **Comprehensive OOP Implementation**
   - Classes and objects
   - Inheritance and polymorphism
   - Encapsulation with properties
   - Abstract classes and interfaces

2. **Design Patterns Mastery**
   - MVC architecture
   - Repository pattern for data access
   - Strategy pattern for flexible exports
   - Dependency injection for loose coupling
   - Observer pattern for event handling

3. **SOLID Principles Application**
   - Each class has a single, well-defined responsibility
   - Code is open for extension but closed for modification
   - Abstractions can be substituted without breaking functionality
   - Interfaces are specific and focused
   - Dependencies are on abstractions, not concrete implementations

4. **Professional Development Practices**
   - Clean, readable code structure
   - Proper error handling and validation
   - Data persistence and file I/O
   - User-friendly console interface

## 🎓 Learning Objectives

This project demonstrates:

- **Object-Oriented Programming**: Classes, inheritance, encapsulation
- **Design Patterns**: MVC, Repository, Strategy, Dependency Injection
- **SOLID Principles**: Writing maintainable code
- **File I/O**: Reading/writing CSV and JSON files
- **Input Validation**: Checking user input
- **Error Handling**: Try-catch blocks and exceptions

## 📝 Key Classes

### Models
- **`Product`** - Product entity with validation and encapsulation
- **`BaseModel`** - Abstract base class for all models

### Views  
- **`ConsoleView`** - Handles all display and user input (Presentation layer)

### Controllers
- **`ShopController`** - Coordinates application flow (MVC Controller)

### Services
- **`ProductService`** - Business logic for product operations
- **`ExportService`** - Export functionality with Strategy pattern
- **`BaseService`** - Base service with Observer pattern support

### Repositories
- **`ProductRepository`** - Data access and CSV persistence (Repository pattern)
- **`IRepository`** - Repository interface for abstraction

### Utils
- **`InputValidator`** - Input validation helpers

## 🏆 Project Highlights

### Design Patterns Implemented
1. **MVC (Model-View-Controller)** - Separation of concerns
2. **Repository Pattern** - Abstracted data access
3. **Strategy Pattern** - Flexible export strategies (JSON/CSV)
4. **Dependency Injection** - Loose coupling between components
5. **Observer Pattern** - Event notification system
6. **Factory Method** - Creating exporters

### SOLID Principles Applied
- ✅ **Single Responsibility** - Each class has one clear purpose
- ✅ **Open/Closed** - Can extend without modifying existing code
- ✅ **Liskov Substitution** - Interfaces are interchangeable
- ✅ **Interface Segregation** - Focused, minimal interfaces
- ✅ **Dependency Inversion** - Depend on abstractions

### Technical Features
- ✅ Object-oriented design with inheritance and polymorphism
- ✅ Encapsulation using Python properties
- ✅ Abstract base classes and interfaces
- ✅ Comprehensive input validation
- ✅ Error handling with try-catch blocks
- ✅ File I/O operations (CSV and JSON)
- ✅ Auto-incrementing IDs
- ✅ Data persistence between sessions
- ✅ Clean console-based user interface

## 📄 License

MIT License - Free to use for educational purposes.

---

## 👨‍🏫 Course Information

**🎓 My Final Project for Object-Oriented Programming Course**  
*Demonstrating clean architecture, design patterns, and SOLID principles*

📚 **Course**: Online Python Programming  
🗓️ **Schedule**: Monday - Saturday, 9:00 PM - 10:00 PM  
🏫 **Institution**: JomNum Tech  
- 📘 Facebook: [JomNum Technology](https://web.facebook.com/jomnumtechnology)  
- 💬 Telegram: [JomNum Tech](https://t.me/jomnumtech)  

👨‍💻 **Instructor**: Ing Davann

---

*Moving forward together in the age of technology* 🚀