# 🛒 CLI Shop Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-MVC-orange?style=for-the-badge)
![Patterns](https://img.shields.io/badge/Design_Patterns-5%2B-blueviolet?style=for-the-badge)
![Standard Library](https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=for-the-badge)

**A professional, console-based inventory management system built with Python — showcasing clean architecture, SOLID principles, and industry-standard design patterns.**

[Features](#-features) · [Architecture](#️-architecture) · [Getting Started](#-getting-started) · [Usage](#-usage-guide) · [Design Patterns](#-design-patterns) · [Project Structure](#-project-structure)

</div>

---

## 📌 Overview

**CLI Shop Management System** is a fully-featured inventory management application that runs entirely in the terminal. Developed as a **Final Project** for an Object-Oriented Programming course, it demonstrates how real-world software engineering principles — MVC architecture, SOLID design, and multiple design patterns — can be applied to build a clean, maintainable, and extensible system.

> 💡 **No external libraries required.** The entire application is built on Python's standard library only.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Product CRUD** | Add, view, update, and delete products with full validation |
| **Smart Search** | Search products by ID, name, or category |
| **Inventory Stats** | Real-time statistics — total value, stock counts, category breakdown |
| **Data Persistence** | Automatic CSV-based storage that survives between sessions |
| **Export** | Export your inventory to JSON or CSV with one command |
| **Low Stock Alerts** | Automatic warnings when product quantity falls below threshold |
| **Input Validation** | Robust validation for all user inputs with clear error messages |
| **Auto-increment IDs** | Product IDs are generated automatically — no manual entry required |

---

## 🏗️ Architecture

This project follows the **MVC (Model-View-Controller)** pattern with layered architecture for clean separation of concerns:

```
┌─────────────────────────────────────────────────────────────────┐
│                         PRESENTATION LAYER                       │
│                      ConsoleView (views/)                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                         CONTROLLER LAYER                         │
│                    ShopController (controllers/)                  │
└──────────┬──────────────────────────────────────────────────────┘
           │
┌──────────▼──────────────────────────────────────────────────────┐
│                         SERVICE LAYER                            │
│          ProductService · ExportService · BaseService            │
└──────────┬──────────────────────────────────────────────────────┘
           │
┌──────────▼──────────────────────────────────────────────────────┐
│                       REPOSITORY LAYER                           │
│                    ProductRepository (CSV)                       │
└──────────┬──────────────────────────────────────────────────────┘
           │
┌──────────▼──────────────────────────────────────────────────────┐
│                          DATA LAYER                              │
│                  shop_data.csv  ·  exports/                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7 or higher**
- No additional packages or pip installs needed

Check your Python version:

```bash
python --version
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/raaaemmm/cli-shop-managements.git
cd cli-shop-managements
```

**2. Run the application**

```bash
python main.py
```

That's it — no virtual environment, no `pip install`, no configuration needed.

---

## 📖 Usage Guide

When you launch the application, you are greeted with an interactive menu:

```
╔══════════════════════════════════════════════════════════════════════╗
║               CLI SHOP MANAGEMENT SYSTEM                            ║
╠══════════════════════════════════════════════════════════════════════╣
║  1. Add Product          6. View Statistics                         ║
║  2. View All Products    7. Save Data                               ║
║  3. Update Product       8. Export to JSON                          ║
║  4. Delete Product       9. Export to CSV                           ║
║  5. Search Products     10. Clear Screen                            ║
║                         11. Exit                                    ║
╚══════════════════════════════════════════════════════════════════════╝
```

### Menu Options

| Option | Action | Description |
|--------|--------|-------------|
| `1` | **Add Product** | Enter name, category, price, quantity, and optional supplier |
| `2` | **View All Products** | Display all inventory in a formatted table |
| `3` | **Update Product** | Modify any field of an existing product by ID |
| `4` | **Delete Product** | Permanently remove a product from inventory |
| `5` | **Search Products** | Find products by ID, name, or category (case-insensitive) |
| `6` | **View Statistics** | See total products, total value, low stock count, and category breakdown |
| `7` | **Save Data** | Manually save current inventory to CSV |
| `8` | **Export to JSON** | Export full inventory as `shop_export.json` |
| `9` | **Export to CSV** | Export full inventory as `shop_export.csv` |
| `10` | **Clear Screen** | Clear the terminal display |
| `11` | **Exit** | Safely close the program |

### Example Workflow

```bash
# Start the system
python main.py

# Add a new product
> Choose option 1
> Name:     Laptop Pro
> Category: Electronics
> Price:    999.99
> Quantity: 15
> Supplier: TechSupply Co.
✅ Product added successfully! [ID: PRD-001]

# Search for it
> Choose option 5
> Search: "Laptop"
✅ Found 1 product matching "Laptop"

# View live statistics
> Choose option 6
📊 Total Products: 1 | Total Inventory Value: $14,999.85 | Low Stock: 0
```

---

## 🎨 Design Patterns

This project implements **6 industry-standard design patterns**:

### 1. 🏛️ MVC — Model-View-Controller
Cleanly separates data, display, and application logic into independent layers that can change without affecting each other.

### 2. 🗃️ Repository Pattern
`ProductRepository` abstracts all CSV read/write operations. The rest of the application never directly touches the file system — it only calls repository methods.

### 3. ⚙️ Strategy Pattern
Export functionality is interchangeable. `IExporter` defines the interface; `JSONExporter` and `CSVExporter` are concrete strategies. Adding a new export format (e.g., XML, Excel) requires zero changes to existing code.

### 4. 💉 Dependency Injection
`ShopController` does not create its own dependencies — they are injected through the constructor. This enables easy swapping, mocking, and testing of components.

### 5. 👁️ Observer Pattern
`BaseService` implements an observer notification system. Registered observers are automatically notified when inventory data changes.

### 6. 🏭 Factory Method
`ExportService` acts as a factory, instantiating the correct exporter class based on the requested format.

---

## 🧱 SOLID Principles

| Principle | Application in This Project |
|---|---|
| **S** — Single Responsibility | Every class has exactly one reason to change (`Product` handles data, `ConsoleView` handles display, `ProductRepository` handles persistence) |
| **O** — Open / Closed | New exporters, validators, or repository backends can be added without touching existing classes |
| **L** — Liskov Substitution | `ProductRepository` can be swapped for any class implementing `IRepository` without breaking the system |
| **I** — Interface Segregation | `IRepository` and `IExporter` are small, focused interfaces — no class is forced to implement methods it doesn't use |
| **D** — Dependency Inversion | High-level modules (`ShopController`) depend on abstractions (`IRepository`), not on concrete implementations |

---

## 📁 Project Structure

```
cli-shop-managements/
│
├── main.py                      # Entry point — wires dependencies via DI
├── config.py                    # Centralized configuration constants
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
│
├── models/                      # Domain models — Entity layer
│   ├── base_model.py            # Abstract base with timestamp tracking
│   └── product.py               # Product entity with properties & validation
│
├── repositories/                # Data access layer — Repository pattern
│   ├── i_repository.py          # Abstract repository interface
│   └── product_repository.py    # CSV-backed persistence implementation
│
├── services/                    # Business logic layer
│   ├── base_service.py          # Base service with Observer pattern
│   ├── product_service.py       # Product operations & business rules
│   ├── i_exporter.py            # Exporter interface (Strategy pattern)
│   └── export_service.py        # JSON & CSV export strategies
│
├── controllers/                 # MVC Controller layer
│   └── shop_controller.py       # Coordinates view, service, and repository
│
├── views/                       # Presentation layer
│   └── console_view.py          # Console UI — all display and user input
│
├── utils/                       # Utility helpers
│   └── input_validator.py       # Reusable input validation functions
│
└── shop_data.csv                # Auto-created persistent data store
```

---

## 🔑 Key Classes

### Models
| Class | Responsibility |
|-------|----------------|
| `BaseModel` | Abstract base with auto-timestamp and `validate()` hook |
| `Product` | Full product entity with property decorators, validation, and stock utilities |

### Views
| Class | Responsibility |
|-------|----------------|
| `ConsoleView` | All console output and user input — zero business logic |

### Controllers
| Class | Responsibility |
|-------|----------------|
| `ShopController` | Orchestrates the flow between view, services, and repository |

### Services
| Class | Responsibility |
|-------|----------------|
| `ProductService` | Business logic — add, update, delete, search, statistics |
| `ExportService` | Format detection and export strategy execution |
| `BaseService` | Observer registration and notification infrastructure |

### Repositories
| Class | Responsibility |
|-------|----------------|
| `IRepository` | Abstract interface defining the data-access contract |
| `ProductRepository` | CSV file reading, writing, and in-memory caching |

### Utils
| Class | Responsibility |
|-------|----------------|
| `InputValidator` | Reusable validation — numbers, strings, price, quantity |

---

## ⚙️ Configuration

All system-wide settings live in `config.py` — no magic numbers scattered in the code:

```python
class Config:
    DEFAULT_DATA_FILE    = "shop_data.csv"
    DEFAULT_EXPORT_JSON  = "shop_export.json"
    DEFAULT_EXPORT_CSV   = "shop_export.csv"
    TABLE_WIDTH          = 120
    LOW_STOCK_THRESHOLD  = 10
```

To change the low-stock warning threshold or default filenames, update `config.py` — no other file needs to change.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute for educational and personal purposes.

---

## 🎓 Course Information

<div align="center">

**Final Project — Object-Oriented Programming Course**

| | |
|---|---|
| 📚 **Course** | Online Python Programming |
| 🏫 **Institution** | JomNum Tech |
| 🗓️ **Schedule** | Monday – Saturday, 9:00 PM – 10:00 PM |
| 👨‍💻 **Instructor** | Ing Davann |
| 📘 **Facebook** | [JomNum Technology](https://web.facebook.com/jomnumtechnology) |
| 💬 **Telegram** | [JomNum Tech](https://t.me/jomnumtech) |

*Moving forward together in the age of technology* 🚀

</div>