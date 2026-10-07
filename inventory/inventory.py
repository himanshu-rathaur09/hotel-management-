from utils.storage import load, save
from utils.helpers import ask_int, print_table

FILE = "inventory.json"


def show_inventory():
    stock = load(FILE, {})
    print("\n------------- INVENTORY -------------")
    if not stock:
        print("Inventory is empty.")
        return
    rows = [[n, item, qty] for n, (item, qty) in enumerate(stock.items(), 1)]
    print_table(["No", "Item", "Quantity"], rows, ["l", "l", "r"])


def add_stock():
    stock = load(FILE, {})
    item = input("Item name: ").strip().lower()
    if not item:
        print("Item name cannot be empty.")
        return
    qty = ask_int("Quantity to add: ")
    if qty is None or qty <= 0:
        print("Invalid quantity.")
        return
    stock[item] = stock.get(item, 0) + qty
    save(FILE, stock)
    print(f"{item} stock is now {stock[item]}.")


def update_stock():
    stock = load(FILE, {})
    show_inventory()
    item = input("Item to update: ").strip().lower()
    if item not in stock:
        print("Item not found.")
        return
    qty = ask_int("New quantity: ")
    if qty is None or qty < 0:
        print("Invalid quantity.")
        return
    stock[item] = qty
    save(FILE, stock)
    print(f"{item} stock updated to {qty}.")