from menu.menu import get_menu, show_menu
from utils.storage import load, save
from utils.helpers import ask_int, print_table

FILE = "orders.json"
STATUSES = ["Pending", "Preparing", "Served"]


def get_orders():
    return load(FILE, [])


def order_total(order):
    return sum(i["price"] * i["qty"] for i in order["items"])


def _pick_items(menu):
    items = []
    while True:
        fid = ask_int("Food ID (0 to finish): ")
        if fid is None:
            continue
        if fid == 0:
            break
        food = next((f for f in menu if f["id"] == fid), None)
        if not food:
            print("Food not found.")
            continue
        qty = ask_int("Quantity: ")
        if qty is None or qty <= 0:
            print("Invalid quantity.")
            continue
        items.append({"name": food["name"], "price": food["price"], "qty": qty})
    return items


def create_order():
    menu = get_menu()
    if not menu:
        print("Menu is empty. Add food first.")
        return
    show_menu()
    items = _pick_items(menu)
    if not items:
        print("No items selected. Order not created.")
        return
    orders = get_orders()
    new_id = max((o["id"] for o in orders), default=0) + 1
    orders.append({"id": new_id, "items": items, "status": "Pending"})
    save(FILE, orders)
    print(f"\nOrder #{new_id} created.")


def show_orders():
    orders = get_orders()
    print("\n------------- ORDERS -------------")
    if not orders:
        print("No orders yet.")
        return

    rows = []
    for o in orders:
        for n, i in enumerate(o["items"]):
            rows.append([
                o["id"] if n == 0 else "",
                o["status"] if n == 0 else "",
                i["name"],
                i["qty"],
                f"{i['price']:.2f}",
                f"{i['price'] * i['qty']:.2f}",
            ])
        rows.append(["", "", "TOTAL", "", "", f"{order_total(o):.2f}"])
    print_table(
        ["Order", "Status", "Item", "Qty", "Price", "Amount"],
        rows,
        ["l", "l", "l", "r", "r", "r"],
    )


def update_order():
    orders = get_orders()
    show_orders()
    oid = ask_int("Enter order ID to update: ")
    order = next((o for o in orders if o["id"] == oid), None)
    if not order:
        print("Order not found.")
        return
    if order["status"] in ("Paid", "Cancelled"):
        print(f"Order is already {order['status']}.")
        return

    print("1. Add items")
    print("2. Change status")
    choice = input("Choice: ").strip()

    if choice == "1":
        show_menu()
        order["items"].extend(_pick_items(get_menu()))
    elif choice == "2":
        for n, s in enumerate(STATUSES, 1):
            print(f"{n}. {s}")
        pick = ask_int("New status: ")
        if pick is None or not 1 <= pick <= len(STATUSES):
            print("Invalid status.")
            return
        order["status"] = STATUSES[pick - 1]
    else:
        print("Invalid choice.")
        return

    save(FILE, orders)
    print("Order updated.")


def cancel_order():
    orders = get_orders()
    show_orders()
    oid = ask_int("Enter order ID to cancel: ")
    order = next((o for o in orders if o["id"] == oid), None)
    if not order:
        print("Order not found.")
        return
    if order["status"] in ("Paid", "Cancelled"):
        print(f"Order is already {order['status']}.")
        return
    order["status"] = "Cancelled"
    save(FILE, orders)
    print(f"Order #{oid} cancelled.")