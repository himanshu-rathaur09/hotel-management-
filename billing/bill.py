from orders.order import get_orders, show_orders, order_total, FILE
from utils.storage import save
from utils.helpers import ask_int, print_table

GST_RATE = 0.05


def generate_bill():
    orders = get_orders()
    show_orders()
    oid = ask_int("Enter order ID to bill: ")
    order = next((o for o in orders if o["id"] == oid), None)
    if not order:
        print("Order not found.")
        return
    if order["status"] == "Cancelled":
        print("Cannot bill a cancelled order.")
        return
    if order["status"] == "Paid":
        print("This order is already paid.")
        return

    subtotal = order_total(order)
    tax = subtotal * GST_RATE
    total = subtotal + tax

    print(f"\n================ BILL - Order #{order['id']} ================")
    rows = [
        [i["name"], i["qty"], f"{i['price']:.2f}", f"{i['price'] * i['qty']:.2f}"]
        for i in order["items"]
    ]
    print_table(["Item", "Qty", "Price", "Amount"], rows, ["l", "r", "r", "r"])
    print_table(
        ["Summary", "Amount"],
        [
            ["Subtotal", f"{subtotal:.2f}"],
            [f"GST ({int(GST_RATE * 100)}%)", f"{tax:.2f}"],
            ["TOTAL", f"{total:.2f}"],
        ],
        ["l", "r"],
    )

    order["status"] = "Paid"
    save(FILE, orders)