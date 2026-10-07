from utils.storage import load, save
from utils.helpers import ask_int, print_table

FILE = "tables.json"

# Change this to change the layout: table type -> table numbers
LAYOUT = {
    "Normal": range(1, 6),
    "VIP": range(6, 9),
    "Premium": range(9, 11),
}


def default_tables():
    tables = {}
    for table_type, numbers in LAYOUT.items():
        for n in numbers:
            tables[str(n)] = {"type": table_type, "guest": None}
    return dict(sorted(tables.items(), key=lambda item: int(item[0])))


def get_tables():
    defaults = default_tables()
    tables = load(FILE, defaults)

    # If the file has a wrong format, rebuild it with the default layout
    if not isinstance(tables, dict) or not all(str(k).isdigit() for k in tables):
        save(FILE, defaults)
        return defaults

    # Upgrade the old format ("1": null or "1": "Guest name") automatically
    changed = False
    for num, value in list(tables.items()):
        if not isinstance(value, dict):
            table_type = defaults.get(num, {"type": "Normal"})["type"]
            tables[num] = {"type": table_type, "guest": value}
            changed = True
    if changed:
        save(FILE, tables)
    return tables


def show_tables():
    tables = get_tables()
    print("\n------------- TABLES -------------")
    rows = []
    for num in sorted(tables, key=int):
        info = tables[num]
        status = "Booked" if info["guest"] else "Available"
        rows.append([num, info["type"], status, info["guest"] or "-"])
    print_table(["Table No", "Type", "Status", "Guest"], rows)


def book_table():
    tables = get_tables()
    show_tables()
    num = ask_int("\nTable number to book: ")
    if num is None or str(num) not in tables:
        print("Invalid table number.")
        return
    info = tables[str(num)]
    if info["guest"]:
        print("That table is already booked.")
        return
    name = input("Guest name: ").strip()
    if not name:
        print("Guest name cannot be empty.")
        return
    info["guest"] = name
    save(FILE, tables)
    print(f"{info['type']} table {num} booked for {name}.")


def cancel_table():
    tables = get_tables()
    show_tables()
    num = ask_int("\nTable number to cancel: ")
    if num is None or str(num) not in tables:
        print("Invalid table number.")
        return
    info = tables[str(num)]
    if not info["guest"]:
        print("That table is not booked.")
        return
    info["guest"] = None
    save(FILE, tables)
    print(f"Booking for {info['type']} table {num} cancelled.")
