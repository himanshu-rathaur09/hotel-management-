from utils.storage import load, save
from utils.helpers import ask_int, ask_float, print_table

FILE = "menu.json"


def get_menu():
    return load(FILE, [])


def show_menu():
    menu = get_menu()
    print("\n------------- MENU -------------")
    if not menu:
        print("Menu is empty.")
        return
    rows = [[item["id"], item["name"], f"{item['price']:.2f}"] for item in menu]
    print_table(["ID", "Food", "Price"], rows, ["l", "l", "r"])


def add_food():
    menu = get_menu()
    name = input("Food name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    price = ask_float("Price: ")
    if price is None or price <= 0:
        print("Invalid price.")
        return
    new_id = max((i["id"] for i in menu), default=0) + 1
    menu.append({"id": new_id, "name": name, "price": price})
    save(FILE, menu)
    print(f"{name} added with ID {new_id}.")


def update_food():
    menu = get_menu()
    show_menu()
    fid = ask_int("Enter food ID to update: ")
    food = next((f for f in menu if f["id"] == fid), None)
    if not food:
        print("Food not found.")
        return

    name = input(f"New name [{food['name']}]: ").strip()
    price_text = input(f"New price [{food['price']}]: ").strip()

    if name:
        food["name"] = name
    if price_text:
        try:
            food["price"] = float(price_text)
        except ValueError:
            print("Invalid price, keeping the old one.")
    save(FILE, menu)
    print("Food updated.")


def delete_food():
    menu = get_menu()
    show_menu()
    fid = ask_int("Enter food ID to delete: ")
    food = next((f for f in menu if f["id"] == fid), None)
    if not food:
        print("Food not found.")
        return
    menu.remove(food)
    save(FILE, menu)
    print(f"{food['name']} deleted.")
