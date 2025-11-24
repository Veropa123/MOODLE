# ---------------- INVENTORY MODULE ----------------


import csv

inventory = {
    1: {"name": "Laptop X100", "brand": "Acer", "category": "Laptops", "price": 700, "stock": 10, "warranty": 12},
    2: {"name": "Smart TV 50", "brand": "Samsung", "category": "TV", "price": 400, "stock": 15, "warranty": 24},
    3: {"name": "Bluetooth Headset", "brand": "Sony", "category": "Audio", "price": 60, "stock": 30, "warranty": 6},
    4: {"name": "Gaming Mouse", "brand": "Logitech", "category": "Accessories", "price": 25, "stock": 50, "warranty": 12},
    5: {"name": "Tablet T10", "brand": "Lenovo", "category": "Tablets", "price": 250, "stock": 20, "warranty": 12},
}

# ---------------- CRUD ----------------

def add_product():
    try:
        new_id = max(inventory.keys()) + 1
        name = input("Product name: ")
        brand = input("Brand: ")
        category = input("Category: ")
        price = float(input("Unit price: "))
        stock = int(input("Stock quantity: "))
        warranty = int(input("Warranty (months): "))

        inventory[new_id] = {
            "name": name,
            "brand": brand,
            "category": category,
            "price": price,
            "stock": stock,
            "warranty": warranty
        }

        print("Product added successfully.")
    except Exception:
        print("Invalid input. Product not added.")

def view_products():
    print("\n--- INVENTORY LIST ---")
    for pid, data in inventory.items():
        print(pid, "->", data)

def update_product_simple():
    try:
        keyword = input("Enter product name or keyword: ").lower()
        match_id = None

        for pid, product in inventory.items():
            if keyword in product["name"].lower():
                match_id = pid
                break

        if match_id is None:
            print("Product not found.")
            return

        print(f"Found: {inventory[match_id]['name']} (ID: {match_id})")

        field = input("Field to update (name/brand/category/price/stock/warranty): ").lower()
        if field not in inventory[match_id]:
            print("Invalid field.")
            return

        if field == "price":
            inventory[match_id][field] = float(input("New price: "))
        elif field in ("stock", "warranty"):
            inventory[match_id][field] = int(input(f"New {field}: "))
        else:
            inventory[match_id][field] = input(f"New {field}: ")

        print("Product updated successfully.")

    except Exception:
        print("Error updating product.")

def delete_product():
    try:
        keyword = input("Enter product name or keyword to delete: ").lower()
        match_id = None

        for pid, product in inventory.items():
            if keyword in product["name"].lower():
                match_id = pid
                break

        if match_id is None:
            print("Product not found.")
            return

        del inventory[match_id]
        print("Product deleted.")

    except:
        print("Error deleting product.")

# ---------------- CSV EXPORT / IMPORT ----------------

def save_inventory_csv(ruta="inventory.csv"):
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "brand", "category", "price", "stock", "warranty"])

            for pid, p in inventory.items():
                writer.writerow([pid, p["name"], p["brand"], p["category"], p["price"], p["stock"], p["warranty"]])

        print("Inventory saved successfully.")
    except Exception:
        print("Error saving inventory file.")

import csv

def load_inventory_csv(path="inventory.csv"):
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            inventory = []
            for row in reader:
                inventory.append({
                    "name": row["name"],
                    "brand": row["brand"],
                    "category": row["category"],
                    "price": float(row["price"]),
                    "stock": int(row["stock"]),
                    "warranty": int(row["warranty"])
                })
        return inventory
    except FileNotFoundError:
        print("Inventory CSV not found.")
        return []

