# ---------------- REPORTS MODULE ----------------

from sales import sales_history
from inventory import inventory

# Top 3 sold products


def top_products(n=3):
    """
    Prints the top-n products by units sold according to sales_history.
    This function is defensive: it skips malformed sale records.
    """
    if not sales_history:
        print("No sales available.")
        return

    counts = {}
    bad = 0
    for s in sales_history:
        try:
            product = s["product"]
            qty = s["qty"]
            # ensure qty is int
            if not isinstance(qty, int):
                qty = int(qty)
            counts[product] = counts.get(product, 0) + qty
        except Exception:
            bad += 1
            continue

    if not counts:
        print("No valid sales data to compute top products.")
        if bad:
            print(f"Note: {bad} malformed sale records were ignored.")
        return

    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]
    print(f"\n--- TOP {n} PRODUCTS ---")
    for product, qty in top:
        print(f"{product}: {qty} units")
    if bad:
        print(f"\n{bad} malformed sale record(s) were ignored.")
    print()


# Sales by brand
def sales_by_brand():
    brand_data = {}
    for s in sales_history:
        brand_data[s["brand"]] = brand_data.get(s["brand"], 0) + s["total"]

    print("Sales grouped by brand:")
    for brand, total in brand_data.items():
        print(brand, total)

# Income
def income_report():
    if not sales_history:
        print("No sales available.")
        return

    gross = sum(s["qty"] * (s["total"] / (1 - s["discount"])) for s in sales_history)
    net = sum(s["total"] for s in sales_history)

    print("Gross income:", gross)
    print("Net income:", net)

# Inventory performance
def inventory_performance():
    sold = {}
    for s in sales_history:
        sold[s["product"]] = sold.get(s["product"], 0) + s["qty"]

    print("Inventory Performance:")
    for pid, p in inventory.items():
        name = p["name"]
        s = sold.get(name, 0)
        print(f"{name}: Sold {s}, Remaining {p['stock']}")
        
def load_sales_csv(ruta="sales_history.csv"):
    import csv
    from sales import sales_history  # import local reference

    try:
        with open(ruta, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            expected = ["customer", "type", "product", "brand", "qty", "discount", "total"]
            if header != expected:
                print("Invalid header. Expected:", ", ".join(expected))
                return

            sales_history.clear()
            skipped = 0
            for row in reader:
                if len(row) != 7:
                    skipped += 1
                    continue
                try:
                    customer = row[0].strip()
                    cust_type = row[1].strip()
                    product = row[2].strip()
                    brand = row[3].strip()
                    qty = int(row[4])
                    discount = float(row[5])
                    total = float(row[6])

                    sales_history.append({
                        "customer": customer,
                        "type": cust_type,
                        "product": product,
                        "brand": brand,
                        "qty": qty,
                        "discount": discount,
                        "total": total
                    })
                except Exception:
                    skipped += 1
                    continue

            print(f"Sales loaded. {len(sales_history)} records loaded, {skipped} skipped.")

    except FileNotFoundError:
        print("Sales CSV file not found.")
    except Exception as e:
        print(f"Unexpected error loading sales CSV: {e}")


def save_inventory_csv(ruta="inventory.csv"):
    import csv

    if not inventory:
        print("Inventory is empty, cannot save.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Encabezado correcto
            writer.writerow(["id", "name", "brand", "category", "price", "stock", "warranty"])

            for pid, data in inventory.items():
                writer.writerow([
                    pid,
                    data["name"],
                    data["brand"],
                    data["category"],
                    data["price"],
                    data["stock"],
                    data["warranty"]
                ])
        
        print(f"Inventory saved successfully to {ruta}")

    except PermissionError:
        print("Permission denied: cannot write to this location.")
    except Exception as e:
        print(f"Unexpected error while saving: {e}")

