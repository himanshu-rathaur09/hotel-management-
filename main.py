from auth.sign_in import signin

from menu.menu import (
    show_menu,
    add_food,
    update_food,
    delete_food
)

from inventory.inventory import (
    show_inventory,
    add_stock,
    update_stock
)

from orders.order import (
    create_order,
    show_orders,
    update_order,
    cancel_order
)

from table_booking.booking import (
    show_tables,
    book_table,
    cancel_table
)

from billing.bill import generate_bill


def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Show Menu")
        print("2. Add Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Create Order")
        print("6. Show Orders")
        print("7. Update Order")
        print("8. Cancel Order")
        print("9. Generate Bill")
        print("10. Show Inventory")
        print("11. Add Stock")
        print("12. Update Stock")
        print("13. Show Tables")
        print("14. Book Table")
        print("15. Cancel Table")
        print("16. Logout")

        choice = input("Please enter the choice: ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_food()

        elif choice == "3":
            update_food()

        elif choice == "4":
            delete_food()

        elif choice == "5":
            create_order()

        elif choice == "6":
            show_orders()

        elif choice == "7":
            update_order()

        elif choice == "8":
            cancel_order()

        elif choice == "9":
            generate_bill()

        elif choice == "10":
            show_inventory()

        elif choice == "11":
            add_stock()

        elif choice == "12":
            update_stock()

        elif choice == "13":
            show_tables()

        elif choice == "14":
            book_table()

        elif choice == "15":
            cancel_table()

        elif choice == "16":
            print("\nAdmin logged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")
            continue

        input("\nPress Enter to continue...")


def user_menu():

    while True:

        print("\n========== USER MENU ==========")
        print("1. Show Menu")
        print("2. Create Order")
        print("3. Show Tables")
        print("4. Book Table")
        print("5. Cancel Table")
        print("6. Logout")

        choice = input("Please enter the choice: ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            create_order()

        elif choice == "3":
            show_tables()

        elif choice == "4":
            book_table()

        elif choice == "5":
            cancel_table()

        elif choice == "6":
            print("\nUser logged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")
            continue

        input("\nPress Enter to continue...")


def main():

    while True:

        print("\n========================================")
        print("     RESTAURANT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Sign In")
        print("2. Exit")

        choice = input("Please enter your choice: ").strip()

        if choice == "1":

            user = signin()

            if user:

                if user["role"] == "admin":
                    admin_menu()

                elif user["role"] == "user":
                    print("\nWelcome,", user["username"])
                    user_menu()

                else:
                    print("\nUnknown user role.")

        elif choice == "2":
            print("\nThank you for using Restaurant Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()